# CRM da Dra. Brenda Simeão no Twenty (EXP-28)

Versão 2 · 28/10/2026 · Documento de desenho (fase 2: respostas fechadas na triagem e workspace separado). Nada foi criado nem alterado no Twenty, nenhuma mensagem de WhatsApp foi enviada, nada foi publicado.

Base: `dossie-estrategico-funil.md` (seções 2.3, 4.1, 4.2, 4.3, 4.4). Documentos irmãos: `triagem-whatsapp-brenda.md` (fluxo, resgate), `rastreio-e-relatorio-brenda.md` (origem, relatório semanal).

Mudanças da versão 2: removido o campo de queixa em texto livre (`desejo_texto`); `cidade`, `desejo_categoria`, `prazo` e `tratamento_anterior` passam a campos fechados preenchidos pelo próprio lead; decisão de workspace separado tomada pelo Guilherme (seção 3). Cláusulas citadas (7 e 9) conferidas contra `/root/projects/brenda-contrato/contrato.html`.

Marcação: **[OK GUILHERME]** = não ligar antes da aprovação dele.

## 0. O que já existe no Twenty (leitura feita em 28/10)

Consulta somente leitura (SELECT no banco do Twenty, sem API de escrita): 16 pessoas, 13 empresas, 8 oportunidades ativas.

- Já existem **Pessoa "Dra. Brenda Simeão"** e **Empresa "Dra. Brenda Simeão"**: representam a **cliente da Expoente**, não pacientes. Não reaproveitar nem editar. Paciente nunca é vinculado a essa empresa como contato comercial.
- As 8 oportunidades atuais são vendas da própria Expoente (exemplos: um projeto de peças importadas, um de infoprodutos, mais 6 de demonstração/teste). Nenhuma é da Dra. Brenda como paciente/lead.
- Estágios atuais do objeto Oportunidade são os padrão do Twenty: NEW, SCREENING, MEETING, PROPOSAL, CUSTOMER. Não existe nenhum campo personalizado para este funil.
- Pessoa tem só nome, e-mail, telefone, cargo, LinkedIn, empresa. Nenhum campo de origem/UTM.

Consequências para o desenho:
1. Mistura de dados: leads de pacientes (dado pessoal ligado a saúde, LGPD) no mesmo espaço das vendas da Expoente polui o funil comercial e amplia o acesso a dado sensível. **Decisão do Guilherme em 28/10: workspace separado para os pacientes da Dra. Brenda.** Desenho completo na seção 3.
2. Duplicidade: a chave única da Pessoa-paciente é o telefone em E.164. Antes de criar, buscar por telefone; se existir, atualizar. A Pessoa "Dra. Brenda Simeão" existente fica de fora por filtro (`tipo = paciente`).

## 1. Modelo de dados

Dois objetos nativos do Twenty (Pessoa e Oportunidade), com campos personalizados. Um paciente = 1 Pessoa; cada tentativa de tratamento = 1 Oportunidade (permite reentrada futura sem perder histórico).

### 1.1 Pessoa (paciente/lead)

| Campo | Tipo | Observação |
|---|---|---|
| nome | nativo | como o lead se apresentou |
| telefone | nativo, E.164 | **chave única** |
| e-mail | nativo | opcional |
| tipo | select: paciente_lead, outro | filtro para separar da cliente Dra. Brenda |
| cidade | select fechado: goiania, aparecida, regiao_metropolitana, outra, prefere_dra | resposta da pergunta 1 |
| consentimento_contato | booleano + data + versão do aviso | LGPD: ciência após a abertura com link para o aviso de privacidade |
| nao_contatar | booleano | resposta PARAR ou equivalente |
| consentimento_cookies_lp | booleano | veio do banner da LP; se falso, não enviar eventos de navegador |
| ref_code | texto | código curto gerado na LP |
| fbclid, fbc, fbp | texto | atribuição Meta |
| ctwa_clid | texto | anúncio de conversa |
| utm_source, utm_medium, utm_campaign, utm_content, utm_term | texto | |
| pilar_criativo | select: naturalidade, preservacao, escultura, transformacao, indefinido | vem de `utm_content` |
| primeiro_contato_em | data/hora | |

### 1.2 Oportunidade (tratamento)

| Campo | Tipo | Observação |
|---|---|---|
| pessoa | relação | |
| etapa | select (1.3) | |
| score | número 0 a 5 | ver triagem |
| desejo_categoria | select fechado: formato, cor, alinhamento_visual, outro, prefere_dra | escolhido pelo lead na pergunta 2; só entra em contagens agregadas do relatório, nunca vai ao Meta |
| prazo | select fechado: ate_30d, ate_90d, mais_90d, prefere_dra | pergunta 3 |
| tratamento_anterior | select fechado: sim, nao, prefere_dra | pergunta 4, se mantida **[OK GUILHERME]**; não pontua |
| texto_livre_recebido | booleano + data + pergunta em que ocorreu | só o fato; **o conteúdo nunca é gravado** (triagem 2.1) |
| fala_direta | booleano | escolheu "prefiro falar direto com a Dra." ou enviou texto livre; handoff humano |
| aceita_avaliacao_particular | booleano | confirmação no passo final |
| avaliacao_data | data/hora | |
| comparecimento | select: pendente, compareceu, no_show, remarcou | |
| fechou | booleano + data | |
| motivo_perda | select (1.4) | obrigatório ao marcar Perdido |
| tentativas_resgate | número 0 a 2 | ver resgate |
| ultima_msg_cliente_em, ultima_msg_nossa_em | data/hora | base da regra de tempo |
| event_id_lead, event_id_schedule, event_id_realizada, event_id_fechou | texto | idempotência CAPI |
| valor | **não existe**: nenhum campo de valor em reais neste funil | `Purchase` com valor só se autorizado (1.5) |

Removido na versão 2: `desejo_texto` (queixa em texto livre). Não existem, em nenhum objeto, campo de texto livre para o lead, nem campos de condição de saúde, dor, doença, medicação ou histórico clínico. O único campo de texto livre é o `motivo_perda` "Outro", preenchido pela atendente, sem dado de saúde.

### 1.3 Etapas (substitui os 5 estágios padrão na pipeline deste projeto)

Criar as opções de `etapa` no Twenty exige escrita: **[OK GUILHERME]**.

| # | Etapa | Entra quando | Quem move |
|---|---|---|---|
| 1 | Lead | 1ª mensagem recebida (WhatsApp) ou envio do formulário da LP | automático |
| 2 | Qualificado | score 4 ou 5 na triagem | automático por regra de score |
| 3 | Avaliação agendada | data/hora confirmada pelo lead | atendente (ou bot ao confirmar) |
| 4 | Compareceu | presença na avaliação | recepção, no dia |
| 5 | Fechou | aceite do plano apresentado pessoalmente | Dra. |
| 6 | Perdido | encerrado com motivo | atendente/Dra. |

Estados laterais (não são etapas): morno = score 2 ou 3, fica em Lead com tag `nutricao` e retorno em 7 dias; no-show = `comparecimento = no_show`, volta a Perdido só após resgate sem resposta. O dossiê tinha "Em triagem" e "Plano apresentado"; foram fundidos (triagem vira estado de Lead; plano apresentado vira parte de Compareceu) para ficar nas 6 etapas pedidas. **[OK GUILHERME: aceitar a simplificação]**

### 1.4 Motivos de perda (lista fechada)

1. Fora da região (não é de Goiânia/região)
2. Fora de perfil (busca outro procedimento)
3. Só pesquisando, sem prazo
4. Sem resposta após resgate
5. Não aceitou avaliação presencial particular
6. No-show sem retorno
7. Avaliou e não fechou: decisão adiada
8. Avaliou e não fechou: optou por outro profissional
9. Avaliou e não fechou: o plano não era indicado
10. Outro (texto curto, sem dado de saúde)

Os motivos 7 a 9 só descrevem decisão; não registrar a razão clínica.

### 1.5 Etapa para evento Meta (CAPI)

Gatilho: webhook do Twenty "etapa alterada" para o serviço de eventos (dossiê 4.3). Todos os eventos de CRM têm `action_source = system_generated` (ou `chat` quando vem do WhatsApp), `event_id` guardado no campo da oportunidade, `user_data` com telefone e nome em SHA-256, mais `fbc`/`fbp`/`ctwa_clid` quando existirem. Chave de idempotência: telefone + etapa + event_id.

| Etapa | Evento Meta | Observação |
|---|---|---|
| Lead (da LP, formulário) | `Lead` (Pixel + CAPI, mesmo event_id) | só com consentimento de cookies |
| Lead (WhatsApp, clique prévio) | `Contact` já disparado na LP ao clicar; não repetir | |
| Qualificado | `Lead` qualificado, server-side | evento principal de qualidade de lead; distinguir do Lead de formulário com `content_name=lead_qualificado`; sem parâmetro de triagem |
| Avaliação agendada | `Schedule` | sem valor; principal sinal de otimização do conjunto de anúncios |
| Compareceu | nenhum por padrão; fica só no CRM | **[OK GUILHERME]** recomendação: não enviar evento de comparecimento a uma avaliação odontológica ao Meta |
| Fechou | nenhum por padrão. `Purchase` só se a Dra. autorizar enviar valor | **[OK GUILHERME + Dra.]**; sem autorização, enviar evento personalizado `PlanoFechado` sem valor, ou nada (recomendação: nada, para manter dado de tratamento fora do Meta) |
| Perdido | nenhum | não se envia evento negativo |

Parâmetros permitidos nos eventos: `content_name`, `pilar_criativo` (descreve o anúncio) e `event_source_url`. **Proibido enviar** `desejo_categoria`, `tratamento_anterior`, prazo, score, cidade, qualquer texto livre ou qualquer dado de saúde (nada de saúde ao Meta). Ver política em `triagem-whatsapp-brenda.md` seção 3.

Homologação antes de ligar: `test_event_code` do Events Manager, checar deduplicação e qualidade de correspondência. **[OK GUILHERME]** para ativar em produção (Pixel ID, token CAPI e acesso ao Events Manager ainda dependem da Dra.; ver `dominio-e-acessos.md`).

## 2. Lista de tudo que precisa de OK antes de ligar

1. ~~Workspace separado versus mesmo~~ decidido: separado. Falta o OK para o caminho técnico (3.4: instância própria ou modo multi-workspace) e para o nome/subdomínio.
2. Criar workspace, campos personalizados e as 6 etapas no Twenty (1.2, 1.3, seção 3).
3. Simplificação das etapas do dossiê (1.3).
4. Ligar webhook de entrada (LP e WhatsApp) e de saída (CAPI) em produção.
5. Eventos de comparecimento e fechamento ao Meta (recomendação: nenhum; `Purchase` só com valor autorizado pela Dra.).
6. Número e ferramenta de WhatsApp da Dra. (API oficial ou ferramenta de atendimento) e templates de mensagem aprovados.
7. Texto final das perguntas de triagem e da mensagem de resgate (`triagem-whatsapp-brenda.md`).
8. Texto de privacidade/consentimento da LP e cláusula de LGPD do contrato revisada (dado de paciente tratado pela Expoente: papel de operadora, base legal, retenção).
9. Primeiro disparo de qualquer mensagem automática de WhatsApp.
10. Quarto toque da triagem (`tratamento_anterior`), ciência por continuidade como consentimento, e configuração de persistência de mensagens da Evolution API (triagem 2 e 2.1).
11. Seção 3: caminho técnico do workspace, nome, papéis, conta de administradora da Dra. e janela de transferência.

## 3. Workspace separado no Twenty para os pacientes da Dra. Brenda

Somente documentação. Nada foi criado no Twenty. O que há hoje (leitura em 28/10): uma instância Twenty v2.48.0 em Docker (servidor, worker, Postgres, Redis) em `https://21.expoente.marketing`, sem o modo multi-workspace ligado nas variáveis de ambiente do contêiner, com os candidatos e clientes da Expoente.

### 3.1 Por que separar

1. **Papéis da LGPD.** Pelo contrato (7.2), a Dra. é controladora dos dados dos pacientes em potencial e a Expoente é operadora. Cliente da Expoente e candidato são dados da própria Expoente; paciente é dado da Dra. Misturar quebra a fronteira entre controladora e operadora.
2. **Acesso mínimo.** Quem trabalha o funil comercial da Expoente não precisa ver nome e telefone de paciente; no workspace atual, qualquer membro veria.
3. **Entrega e eliminação limpas.** No fim do contrato: CSV da base e eliminação das cópias em até 30 dias (7.6). Com workspace próprio, "exportar e apagar" é uma operação única, sem filtrar registro a registro num banco compartilhado.
4. **Funil próprio.** Etapas, campos e visões deste projeto não poluem o pipeline comercial da Expoente (que usa os estágios padrão).
5. **Propriedade.** Dados e acessos são da Dra. (9.1); o workspace é um ativo dela operado pela Expoente, como a conta de anúncios.

### 3.2 Como a Dra. passa a controlar

| Quem | Papel no workspace | O que pode | O que não pode |
|---|---|---|---|
| Dra. Brenda Simeão | **Administradora** (dona do workspace) | Tudo: ver e editar todos os registros, convidar e remover membros, definir papéis, exportar CSV, gerar e revogar chaves de API e webhooks, apagar o workspace | nada é bloqueado |
| Atendente indicada pela Dra. | Membro (leitura e escrita de pessoas e oportunidades) | Mover etapa, registrar comparecimento e motivo de perda, ver a conversa resumida do lead | Alterar modelo de dados, exportar em massa, gerir membros, ver configurações |
| Expoente (operadora) | Papel restrito "Operadora", conta nominal (não compartilhada) | Ler e escrever registros no limite do necessário para a operação, manter campos, visões, integração e relatório agregado | Gerir membros ou papéis, apagar o workspace, mudar a administradora, usar dado para finalidade própria (7.4) |

Regras:
- **Durante a montagem**, a conta da Expoente nasce como administradora só porque alguém precisa criar os campos e as chaves. **Na entrega ao vivo**, a Dra. é promovida a administradora e a conta da Expoente é rebaixada ao papel restrito. Esse rebaixamento é um item de aceite antes de ligar. **[OK GUILHERME]**
- Rebaixar o papel da Expoente exige que ela mantenha acesso a configuração para operar (campos, webhooks). Se o papel restrito do Twenty v2.48.0 não separar "editar modelo de dados" de "ver registros", a alternativa é conta técnica de integração com chave de API de escopo mínimo e conta humana da Expoente só com leitura. Confirmar o que o papel permite na versão instalada **antes** de prometer a Dra. (os nomes de menu abaixo seguem a versão 2.x e devem ser conferidos na tela).
- **O que a Expoente enxerga como operadora:** os dados necessários para rodar o funil: nome, telefone, faixas e escolhas fechadas, etapa, score, origem, consentimento. A Expoente não recebe conteúdo clínico, porque a triagem não o coleta (7.3). Relatórios para a Expoente e para a Dra. usam contagens e proporções.
- **Limite honesto:** o banco do workspace roda na infraestrutura da Expoente. O papel restrito é controle lógico, não barreira técnica contra quem administra o servidor. O que protege a Dra. nesse ponto é o contrato (7.2 só instruções dela, 7.4 sem finalidade própria, 7.5 aviso de incidente em 48 horas, 8 sigilo) mais o registro de quem acessa. Isso deve estar claro para ela; se ela quiser garantia técnica maior, o caminho é hospedar a instância em conta dela (mesma ideia da migração da LP, 9.3).
- **Direitos do titular (LGPD):** pedido de acesso, correção ou eliminação feito por paciente chega à Dra. (controladora); a Expoente executa a instrução dela no workspace.
- **Fim do contrato:** a Expoente exporta a base em CSV e entrega à Dra. (7.6); remove os próprios acessos (9.2); elimina as cópias que tiver em até 30 dias, incluindo o banco do workspace, backups e arquivos temporários (7.6), e registra a data da eliminação por escrito. A automação e a instalação da Evolution API são da Expoente e podem ser desativadas (9.5). Se a Dra. preferir continuar com o CRM, a administradora é ela e o workspace passa a ser dela.

### 3.3 Modelo de dados: idêntico ao da fase 1

Mesmos objetos (Pessoa = paciente/lead, Oportunidade = tratamento), mesmas 6 etapas (1.3), mesmos motivos de perda (1.4), mesmos eventos (1.5), com as alterações já refletidas na seção 1 desta versão (sem `desejo_texto`; campos fechados). O campo `tipo` da Pessoa deixa de ser necessário para separar da cliente Expoente, já que no workspace novo não existe Pessoa "Dra. Brenda Simeão" cliente; manter só se quiser fim de ambiguidade. As 8 oportunidades e as 16 pessoas do workspace atual **não** são migradas.

### 3.4 Passo a passo para criar (executar só após o OK)

Há dois caminhos, ambos exigem mexer em infraestrutura e por isso estão aqui apenas descritos:

**Caminho A (recomendado): segunda instância Twenty, dedicada.** Isolamento total (banco, Redis e usuários próprios) e eliminação por remoção de volume.
1. Subdomínio novo para a Dra., por exemplo `crm.<dominio-da-dra>` ou `brenda.21.expoente.marketing` (decisão de nome **[OK GUILHERME]**), apontando para a VPS.
2. Novo projeto Docker Compose separado do atual (mesma imagem e versão do Twenty, volumes e banco próprios, portas diferentes, chave `APP_SECRET` nova e `SERVER_URL` do novo subdomínio). Não reaproveitar o banco nem o Redis atuais.
3. Novo site no nginx com certificado TLS para o subdomínio (alteração de nginx, só com o OK).
4. Abrir a URL e criar o primeiro usuário; ele é o administrador inicial. Nome do workspace: "Dra. Brenda Simeão". Usar e-mail de operação da Expoente só no início, depois convidar a Dra.
5. Convidar a Dra. como administradora (Configurações, Membros). Aceitando o convite, promover; só então rebaixar a conta da Expoente ao papel restrito (3.2).
6. Configurar o backup do banco novo e o prazo de retenção (e a eliminação em 30 dias no fim do contrato).

**Caminho B: modo multi-workspace na instância atual.** Exige ligar o modo multi-workspace no servidor (variável de ambiente e subdomínios por workspace, com DNS curinga e nginx), reiniciar o servidor e o worker atuais, e o risco de afetar candidatos e clientes da Expoente. Isolamento lógico, não físico (mesmo banco). Não recomendado.

Criação dos campos (nos dois caminhos, em Configurações, Modelo de dados):
1. Objeto **Pessoa**: criar os campos da tabela 1.1 (`tipo` opcional, `cidade` como seleção com as 5 opções, `consentimento_contato` data e versão, `nao_contatar`, `consentimento_cookies_lp`, `ref_code`, `fbclid`, `fbc`, `fbp`, `ctwa_clid`, cinco `utm_*`, `pilar_criativo`, `primeiro_contato_em`).
2. Objeto **Oportunidade**: criar os campos da tabela 1.2; a seleção `etapa` com as 6 opções da 1.3 na ordem Lead, Qualificado, Avaliação agendada, Compareceu, Fechou, Perdido; `desejo_categoria`, `prazo`, `tratamento_anterior`, `motivo_perda` (10 opções da 1.4) como seleções; `texto_livre_recebido` e `fala_direta`; os quatro `event_id_*`. **Não criar** `desejo_texto` nem campo de valor.
3. Visões: Kanban por `etapa`; lista "Fala direta" (filtro `fala_direta = verdadeiro`); lista "Morno para retorno" (tag `nutricao`, retorno em 7 dias); visão semanal por `pilar_criativo` para o relatório.
4. Papéis (3.2): criar "Operadora" e "Atendente", conferindo na tela o que a versão permite, e testar com uma conta de cada papel em registro fictício.
5. Chave de API de escopo mínimo para a automação (não reutilizar a do workspace atual) e, depois do OK, webhooks de etapa alterada.
6. Teste de aceite com 3 registros fictícios apagados em seguida: criação por webhook, mudança de etapa, exportação CSV pela administradora.

### 3.5 O que se perde e o que se ganha em relação ao workspace atual

| Tema | No workspace atual (Expoente) | No workspace separado |
|---|---|---|
| Integração com a automação (triagem, atribuição) | Já existe infraestrutura de webhooks e chaves usada pela Expoente | **Perde**: nada está ligado; refazer chave de API, URL de webhook e mapeamento dos campos apontando para o novo endereço. **Ganha**: o fluxo desta cliente nasce já com chave própria e escopo mínimo |
| Relatório semanal (`rastreio-e-relatorio-brenda.md`) | Consultaria o banco atual | **Perde**: o script de relatório precisa ler o novo workspace (outra chave e outra URL); sem painel comum com a Expoente. **Ganha**: relatório da Dra. nunca mistura números com os da Expoente |
| Webhooks | Saída para o serviço de eventos (CAPI) poderia reaproveitar a configuração existente | **Perde**: recriar os webhooks de etapa alterada e testar a deduplicação de `event_id`. **Ganha**: um problema de webhook de um lado não derruba o outro |
| Visão única para a Expoente | Todos os clientes num lugar só | **Perde**: a equipe Expoente precisa de login separado; **ganha**: acesso mínimo e fronteira LGPD |
| Entrega e eliminação | Filtrar e apagar registros num banco compartilhado | **Ganha**: exportar CSV e remover o workspace inteiro em um passo |
| Manutenção | Uma instância para atualizar | **Perde** (Caminho A): segunda instância para atualizar e fazer backup. No Caminho B não há esse custo, mas há risco de afetar a instância atual |

### 3.6 Antes de ligar: o que precisa do OK do Guilherme

1. Caminho A ou B e o nome/subdomínio do workspace.
2. Quem cria a conta inicial e o e-mail da Dra. administradora; data da transferência de administração e do rebaixamento da Expoente.
3. Papéis exatos (3.2), depois de conferir o que a versão instalada do Twenty permite.
4. Alteração de nginx, DNS e Docker (nenhuma feita).
5. Política de backup e retenção do workspace novo.
6. Texto para a Dra. explicando o limite do controle lógico (3.2, "Limite honesto").

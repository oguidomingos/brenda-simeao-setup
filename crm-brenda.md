# CRM da Dra. Brenda Simeão no Twenty (EXP-28)

Versão 1 · 28/10/2026 · Documento de desenho. Nada foi criado nem alterado no Twenty, nenhuma mensagem de WhatsApp foi enviada, nada foi publicado.

Base: `dossie-estrategico-funil.md` (seções 2.3, 4.1, 4.2, 4.3, 4.4). Documentos irmãos: `triagem-whatsapp-brenda.md` (fluxo, resgate), `rastreio-e-relatorio-brenda.md` (origem, relatório semanal).

Marcação: **[OK GUILHERME]** = não ligar antes da aprovação dele.

## 0. O que já existe no Twenty (leitura feita em 28/10)

Consulta somente leitura (SELECT no banco do Twenty, sem API de escrita): 16 pessoas, 13 empresas, 8 oportunidades ativas.

- Já existem **Pessoa "Dra. Brenda Simeão"** e **Empresa "Dra. Brenda Simeão"**: representam a **cliente da Expoente**, não pacientes. Não reaproveitar nem editar. Paciente nunca é vinculado a essa empresa como contato comercial.
- As 8 oportunidades atuais são vendas da própria Expoente (exemplos: um projeto de peças importadas, um de infoprodutos, mais 6 de demonstração/teste). Nenhuma é da Dra. Brenda como paciente/lead.
- Estágios atuais do objeto Oportunidade são os padrão do Twenty: NEW, SCREENING, MEETING, PROPOSAL, CUSTOMER. Não existe nenhum campo personalizado para este funil.
- Pessoa tem só nome, e-mail, telefone, cargo, LinkedIn, empresa. Nenhum campo de origem/UTM.

Consequências para o desenho:
1. Mistura de dados: leads de pacientes (dado pessoal ligado a saúde, LGPD) no mesmo espaço das vendas da Expoente polui o funil comercial e amplia o acesso a dado sensível. **Recomendação: workspace separado "Brenda Simeão" no Twenty** (pipeline e campos próprios, acesso só da equipe designada). Alternativa mais barata: mesmo workspace com campo `projeto = brenda` e view filtrada; aceita, porém acesso fica compartilhado. **[OK GUILHERME: escolher workspace separado ou mesmo workspace]**
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
| cidade | texto | resposta da pergunta 1 |
| consentimento_contato | booleano + data | LGPD: ciência de que o contato segue por WhatsApp |
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
| desejo_texto | texto longo, **acesso restrito** | resposta da pergunta 2 em texto livre. Fica só no CRM, nunca sai |
| desejo_categoria | select: cor, formato, alinhamento, outro | categoria genérica, única coisa que pode ir a relatórios |
| prazo | select: ate_30d, ate_90d, mais_90d, sem_prazo | pergunta 3 |
| aceita_avaliacao_particular | booleano | confirmação no passo final |
| avaliacao_data | data/hora | |
| comparecimento | select: pendente, compareceu, no_show, remarcou | |
| fechou | booleano + data | |
| motivo_perda | select (1.4) | obrigatório ao marcar Perdido |
| tentativas_resgate | número 0 a 2 | ver resgate |
| ultima_msg_cliente_em, ultima_msg_nossa_em | data/hora | base da regra de tempo |
| event_id_lead, event_id_schedule, event_id_realizada, event_id_fechou | texto | idempotência CAPI |
| valor | **não existe**: nenhum campo de valor em reais neste funil | `Purchase` com valor só se autorizado (1.5) |

Não existem, em nenhum objeto, campos de condição de saúde, dor, doença, medicação ou histórico clínico.

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
| Qualificado | `Lead` qualificado, server-side | evento principal de qualidade de lead; distinguir do Lead de formulário com `content_name=lead_qualificado` |
| Avaliação agendada | `Schedule` | sem valor; principal sinal de otimização do conjunto de anúncios |
| Compareceu | evento personalizado `AvaliacaoRealizada` | sem parâmetros clínicos; **[OK GUILHERME]** ligar ou deixar só no CRM |
| Fechou | nenhum por padrão. `Purchase` só se a Dra. autorizar enviar valor | **[OK GUILHERME + Dra.]**; sem autorização, enviar evento personalizado `PlanoFechado` sem valor |
| Perdido | nenhum | não se envia evento negativo |

Parâmetros permitidos nos eventos: `content_name`, `pilar_criativo`, `desejo_categoria` (cor, formato, alinhamento) apenas como categoria genérica, `event_source_url`. **Proibido enviar** `desejo_texto`, qualquer campo livre, cidade, ou qualquer dado de saúde. Ver política em `triagem-whatsapp-brenda.md` seção 3.

Homologação antes de ligar: `test_event_code` do Events Manager, checar deduplicação e qualidade de correspondência. **[OK GUILHERME]** para ativar em produção (Pixel ID, token CAPI e acesso ao Events Manager ainda dependem da Dra.; ver `dominio-e-acessos.md`).

## 2. Lista de tudo que precisa de OK antes de ligar

1. Workspace separado versus mesmo workspace (0).
2. Criar campos personalizados e as 6 etapas no Twenty (1.2, 1.3).
3. Simplificação das etapas do dossiê (1.3).
4. Ligar webhook de entrada (LP e WhatsApp) e de saída (CAPI) em produção.
5. Evento `AvaliacaoRealizada` e destino do fechamento (`Purchase` com valor ou `PlanoFechado` sem valor).
6. Número e ferramenta de WhatsApp da Dra. (API oficial ou ferramenta de atendimento) e templates de mensagem aprovados.
7. Texto final das perguntas de triagem e da mensagem de resgate (`triagem-whatsapp-brenda.md`).
8. Texto de privacidade/consentimento da LP e cláusula de LGPD do contrato revisada (dado de paciente tratado pela Expoente: papel de operadora, base legal, retenção).
9. Primeiro disparo de qualquer mensagem automática de WhatsApp.

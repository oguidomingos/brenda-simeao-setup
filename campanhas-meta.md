# Campanhas Meta — Dra. Brenda Simeão (EXP-29)

Versão 1 · 28/10/2026 · Desenho. **Nada foi criado, alterado ou ativado no Meta.** Conta `act_9695520683892802` (CA01 BRENDA SIMEÃO), Business Manager `275891219773948`, pré-paga, abastecida por Pix pela Dra.

Base: `dossie-estrategico-funil.md` (pilares 1.2, checklist CFO 1.3, testes 1.5, dimensionamento 4.5), `tracking.md` (EXP-27), `crm-brenda.md`, `triagem-whatsapp-brenda.md` e `rastreio-e-relatorio-brenda.md` (EXP-28), `roteiros-gravacao.md` (cortes de 15s), `calendario-instagram.md`.

Convenção: **[OK GUILHERME]** = precisa de aprovação antes de executar. **[OK DRA.]** = precisa dela (acesso, pagamento ou texto). Regras do CFO vêm de fontes secundárias (Res. CFO-196/2019): conferir o texto vigente no CFO / CRO-GO antes de ativar. Nenhum valor em reais neste documento; a verba é sempre uma proporção de **V**, a verba mensal que a Dra. definir.

## 0. O que a leitura da conta mostra (somente leitura, 28/10/2026)

| Fato | Leitura | Consequência |
|---|---|---|
| Conta | ativa (status 1), pré-paga, sem motivo de bloqueio | pode veicular assim que houver saldo e limite |
| Saldo disponível | **zero** (fonte de pagamento "Saldo disponível") | nada veicula hoje |
| Limite de gasto da conta | **igual ao total já gasto** | mesmo com saldo por Pix, **nada veicula até o limite ser removido ou elevado** (hipótese forte; confirmar em Configurações de pagamento no Business Manager) |
| Campanha "Campanha trafego no Instagram" (`23854221017180795`) | **ativa**, objetivo Engajamento, criada em 15/04/2026, verba diária própria | assim que entrar saldo e limite, ela volta a gastar sozinha, no objetivo que não gerou conversa |
| Demais 10 campanhas | todas pausadas | nada a fazer, só não reativar |

Histórico (leitura já levantada): funcionaram em 2025 as três campanhas **CBO de facetas com destino WhatsApp ou Direct** (`[CBO] [1-3-3] - ENG - FACETAS [DIRECT] 23/05`, `[CBO] [1-3-3] - ENG - FACETAS [WHATS] 02/06`, `[CBO] [1-2-2] - ENG - FACETAS [WHATS] 26/06`). Foram ruins as de Leads (Site) e a de engajamento do Instagram: muita reação e quase nenhuma conversa. Conclusão que guia este desenho: **conversa no WhatsApp, em CBO, com facetas como único tema**, e não curtida nem lead de formulário.

Ressalva: o histórico serve de direção, não de meta. Os números de 2025 foram de outro momento da conta, sem a triagem, o Pixel novo e o posicionamento atual.

## 1. Estrutura (1 campanha, 2 conjuntos, 5 anúncios)

Seguindo a convenção de nome que a conta já usa: `[CBO] [1-2-5] - CONV - FACETAS [WHATS] <mês>/<ano>` (1 campanha, 2 conjuntos, 5 anúncios).

```
Campanha  [CBO] FACETAS GOIANIA [WHATS]           objetivo Engajamento, destino WhatsApp
 ├─ Conjunto A  Amplo (Advantage+ público, sugestão mulheres 28-50)   5 anúncios
 └─ Conjunto B  Interesses (estética, beleza, moda)                   mesmos 5 anúncios, sem duplicar o arquivo (usar a publicação existente)
```

### 1.1 Campanha

| Item | Definição |
|---|---|
| Objetivo | Engajamento, destino **Aplicativos de mensagens > WhatsApp** (mesmo formato das campanhas de 2025 que funcionaram). Ver 1.5 para a evolução. |
| Orçamento | **CBO** (orçamento no nível da campanha) |
| Verba diária | **V ÷ 30**, no total da campanha, aplicada em duas fases: semanas 1 e 2 a **90% de V ÷ 30** (os 10% restantes de V ficam de reserva para escalar o vencedor); semanas 3 e 4 sobe ao valor cheio **ou** para o máximo de +20% a cada 3 dias, se as regras da seção 6 permitirem. Nunca ultrapassar V no mês. |
| Estratégia de lance | Menor custo, sem teto, nas duas primeiras semanas. Teto de custo só depois de a semana 2 definir o custo por conversa de referência. |
| Categoria especial | Nenhuma (não é crédito, emprego, habitação nem política). Conferir se a Meta classifica como saúde ao criar; se classificar, aceitar as restrições de segmentação. |
| Programação | Contínua, sem data final. Dias e horários: sem restrição na semana 1; a partir da semana 3, excluir horários em que a atendente não responde (ver 6.4). |
| Atribuição | Janela padrão (7 dias após clique, 1 dia após visualização). Decidir por **cliques**, nunca por visualização. |
| Nome da campanha no relatório | Mesmo texto, para casar com `campanha` no Twenty. |

### 1.2 Conjuntos e públicos

Os dois conjuntos usam **Goiânia e região** (raio de cerca de 25 km: Goiânia, Aparecida de Goiânia, Senador Canedo, Trindade, Goianira; **conferir os nomes e o raio no seletor de locais da Meta** antes de criar), pessoas que **moram** ou **estiveram recentemente** na área. Idioma: português.

| | Conjunto A: Amplo | Conjunto B: Interesses |
|---|---|---|
| Para que serve | deixar o criativo triar quem responde | testar se um recorte por interesse reduz conversa fora de perfil |
| Idade e gênero | sugestão de público (não restrição rígida): mulheres de 28 a 50 | mulheres de 28 a 50 |
| Segmentação | Advantage+ público, sem interesses | interesses (hipótese a validar na ferramenta de interesses da Meta): estética, beleza, moda, cuidados com a pele, bem-estar. **Não** usar interesse ligado a condição de saúde, a problema dentário ou a procedimento com preço |
| Exclusões | seguidores atuais do Instagram e da página; quem já conversou no WhatsApp nos últimos 90 dias (público personalizado de engajamento, criar quando houver base) | idem |
| Orçamento | sem limite por conjunto na semana 1; mínimo de gasto de 30% por conjunto para o CBO não abandonar um deles antes de ter dado | idem |
| Quando ligar | semana 1 | semana 1; **se a verba V for menor do que sustenta dois conjuntos (cerca de 3 a 4 conversas por dia por conjunto), começar só com o Conjunto A** e ligar o B na semana 3 [OK GUILHERME] |

Públicos futuros (depois de dados reais, não agora): semelhante a quem agendou avaliação (precisa de volume mínimo de eventos `Schedule` no Pixel, ver seção 5); público de quem enviou mensagem e foi qualificado.

### 1.3 Posicionamentos

| Posicionamento | Decisão | Motivo |
|---|---|---|
| Instagram Reels | ligado | formato principal dos vídeos de 15s |
| Instagram Stories | ligado | mesmo vertical 9:16 |
| Instagram Feed e Explorar | ligado | estáticos 4:5 e carrossel |
| Facebook Feed e Reels | **desligado na semana 1**; testar na semana 3 | a página tem 16 seguidores; público de Goiânia que decide por facetas está no Instagram |
| Messenger, Audience Network, Facebook Stories, colunas | desligado | baixo controle de contexto, risco de aparecer junto de conteúdo inadequado |

Cada criativo precisa de duas versões de formato: **9:16** (Reels e Stories) e **4:5** (Feed). Zona de segurança: nada importante nos 14% superiores e inferiores do 9:16 (a interface cobre).

### 1.4 Otimização

- **Evento de otimização:** conversas por mensagem iniciadas (Engajamento > WhatsApp > "Conversas"). É o que a conta já provou entregar.
- **Chave de sucesso real não é a conversa**, é a conversa qualificada e a avaliação agendada. Por isso o relatório semanal (EXP-28) cruza anúncio e pilar com score, `Schedule` e comparecimento, e as decisões da seção 6 usam essas colunas assim que existirem.
- Volume: com verba mensal pequena, o conjunto não sai da fase de aprendizado (a Meta pede em torno de 50 eventos por semana por conjunto). Aceitar isso: a decisão da semana 1 e 2 é por **comparação entre criativos**, não por performance estável.

### 1.5 Evolução do objetivo (fase 2, não ativar agora)

Quando houver **API oficial do WhatsApp** (ou ferramenta de atendimento que repasse `ctwa_clid`) e pelo menos duas semanas de `Lead` qualificado e `Schedule` enviados por CAPI com `action_source=business_messaging` (ver `rastreio-e-relatorio-brenda.md` 1.2), testar uma segunda campanha otimizando para **conversão de conversa** (qualificada) em vez de conversa iniciada. Só então. **[OK GUILHERME]** confirmar com a documentação vigente da Meta como enviar esses eventos para número em app comum versus API oficial (o app comum não entrega referral completo).

## 2. Destino e mensagem de entrada

Dois caminhos, ambos já desenhados no EXP-28:

| | Caminho B: anúncio de conversa (principal desta campanha) | Caminho A: LP e depois WhatsApp (campanha futura, só após publicar a LP) |
|---|---|---|
| Destino | WhatsApp direto, número da Dra. | LP (`lp/index.html`), depois WhatsApp |
| Atribuição | `ctwa_clid` + `ref_code` fixo do anúncio | UTM + `fbclid` + `ref_code` gerado por sessão |
| Dependência | página e Instagram ligados ao WhatsApp; número definido | LP publicada, domínio verificado, Pixel e CAPI no ar |

**Esta campanha usa o Caminho B** porque é o que a conta provou em 2025 e porque a LP ainda não está publicada. A LP entra como campanha seguinte (seção 8, item 8) ou como destino alternativo de 1 anúncio, sem mexer nesta.

### 2.1 Mensagem pré-preenchida (Caminho B)

Texto fixo por anúncio, com o código curto no fim (padrão da triagem):

> Olá, Dra Brenda! Quero avaliar meu sorriso. (ref CNAT01)

O `ref_code` é **fixo por anúncio** (não gerado por servidor), no formato `C` + pilar de 3 letras + 2 dígitos, com até 8 caracteres:

| Anúncio | `ref_code` |
|---|---|
| Naturalidade, Reel | `CNAT01` |
| Preservação, Reel | `CPRE01` |
| Escultura, Reel | `CESC01` |
| Naturalidade, estático macro | `CNAT02` |
| Dúvida "chiclete", estático tipográfico | `CNAT03` |

Registrar esses cinco códigos na tabela de atribuição do EXP-28 **antes de ativar**, apontando para `campanha`, `conjunto` (por `ctwa_clid`, quando houver) e `pilar_criativo`. Se a pessoa apagar o código, a origem cai em "desconhecida (WhatsApp direto)" ou, com `ctwa_clid`, é recuperada pelo referral. **[OK GUILHERME]** aceitar `ref_code` fixo por anúncio como extensão do desenho (o documento do EXP-28 só descreve código por sessão).

### 2.2 Respostas iniciais do anúncio (ice breakers, opções fechadas)

Até 4 opções, todas neutras (nada de queixa de saúde), alinhadas à triagem de respostas fechadas:

1. Quero saber como funciona a avaliação
2. Quero conhecer o trabalho da Dra. Brenda
3. Tenho uma dúvida sobre facetas em resina
4. Prefiro falar direto com a Dra.

A abertura da triagem (privacidade, três perguntas de escolher opção, handoff por score) é a de `triagem-whatsapp-brenda.md`, seção 2. **Não ligar a campanha sem o aviso de privacidade publicado**, porque a abertura cita a URL dele.

## 3. Anúncios: plano de testes de criativo

### 3.1 Lógica do teste

- **Variável testada:** o gancho (os 3 primeiros segundos ou a primeira linha) e o formato. Público, destino, mensagem e chamada ficam iguais.
- **Hipótese falsificável (dossiê 1.5):** o pilar com maior taxa de **conversa qualificada por clique** vence. Se um pilar tiver a maior taxa de clique e a menor taxa de qualificação, ele **perde**.
- **Mínimos antes de cortar qualquer anúncio:** cerca de 1.500 impressões **e** cerca de 30 cliques. Abaixo disso, nenhuma decisão (exceção: reprovação ou risco CFO, seção 6.3).
- **Janela:** semanas 1 e 2 comparam os 5 anúncios; semanas 3 e 4 dobram no vencedor com 2 variações de gancho e uma versão com depoimento (só se houver paciente com consentimento).

### 3.2 Os 5 criativos iniciais

Ligados às gravações de `roteiros-gravacao.md` (cortes 2.6) e ao acervo do `calendario-instagram.md`. Dois saem **hoje**, com o acervo; três dependem de a Dra. gravar com o celular.

| # | Nome do anúncio | Pilar | Formato | Hook (primeira linha) | Material | Pronto quando |
|---|---|---|---|---|---|---|
| 1 | `naturalidade_reel_A1` | 1 Naturalidade | Reel 9:16, 15s | "Dente natural não é uma cor só." | corte A1 do roteiro 2.6 (gravar só gancho e chamada; macros do acervo `p01.jpg`, `closeup.jpg`) | Dra. grava gancho e chamada |
| 2 | `preservacao_reel_A2` | 2 Preservação | Reel 9:16, 15s | "Faceta estraga o dente?" | corte A2 (Reel R2 falado) | Dra. grava R2 |
| 3 | `escultura_reel_A3` | 3 Escultura | Reel 9:16, 15s | "Cada faceta, esculpida à mão." | corte A3, mãos no modelo (`p16.jpg` como apoio) | Dra. grava R3 ou, como plano B, usar a foto `p16.jpg` em movimento lento (versão de fotos, edição Expoente) |
| 4 | `naturalidade_estatico_macro` | 1 Naturalidade | estático 4:5 (e 9:16) | "Dente natural não é uma cor só." | macro `p01.jpg` ou `closeup.jpg`, sem rosto de paciente | **hoje**, com a checagem de termo de divulgação das imagens macro |
| 5 | `naturalidade_estatico_chiclete` | 1 Naturalidade | estático tipográfico 4:5, sem foto | "Medo de ficar com dente de chiclete?" | arte bege/sálvia/marrom, serifada (a mesma do carrossel P03 do calendário) | **hoje**, só arte |

Por que 3 de naturalidade: é o mito que mais trava a decisão (dossiê 1.2) e é onde o acervo hoje sustenta mais material. O pilar 4 (transformação, com rosto) **não entra na primeira rodada**: depende de TCLE por caso e de a Meta aceitar o comparativo; entra na semana 3 se houver caso liberado (item 4 da seção 3.4).

**Ordem de lançamento:** com a campanha montada em rascunho, os anúncios 4 e 5 já podem rodar na semana 1. Os 3 Reels entram assim que forem entregues, **sem pausar** os estáticos, e a contagem de 1.500 impressões e 30 cliques é por anúncio, de modo que anúncios que entram depois não são julgados antes do tempo.

### 3.3 Variações previstas para a semana 3

- Segundo gancho do vencedor. Candidatos (passam no checklist CFO): "Faceta fica com cara de dente de chiclete?" (pergunta de dúvida, sem criticar ninguém; se a Dra. achar que soa comparativo, usar o gancho do anúncio 1) e "Preparo mínimo ou nenhum desgaste, conforme o caso." (não usar "o melhor preparo": é superlativo).
- Formato: versão estática do Reel vencedor, e Reel do estático vencedor.
- Depoimento sóbrio de 15s (só com consentimento, sem reação emocionada).
- Versão com resultado final com rosto (pilar 4), só com TCLE conferido por nome do caso.

### 3.4 O que depende de material

| Item | Depende de | Responsável |
|---|---|---|
| Anúncios 1, 2, 3 | Dra. gravar com o celular (guia em `roteiros-gravacao.md`, seção 3) | Dra. |
| Anúncios 4, 5 | checagem de termo de divulgação das imagens macro e aprovação por escrito | Dra. |
| Anúncio 4 (transformação, depois) | TCLE do caso e checagem se a Meta aceita comparativo (ter versão sem antes e depois) | Dra. e Guilherme |

## 4. Textos de anúncio prontos

Cada anúncio tem: **texto principal**, **título**, **descrição**, **botão** (Enviar mensagem no WhatsApp) e **mensagem pré-preenchida** (2.1). Pontuação e tom da Dra.: calma, sem exclamação, sem emoji, sem superlativo.

Aprovação: o texto abaixo passa no checklist do CFO da seção 4.6 (conferência feita na redação). A aprovação final é da Dra. por escrito e do Guilherme antes de ativar (o desenho da campanha não depende de a Dra. aprovar de novo cada mudança de botão, mas qualquer mudança de texto volta ao checklist).

### 4.1 Anúncio 1 — `naturalidade_reel_A1`
- **Texto principal:**
  > Dente natural não é de uma cor só. Tem translucidez nas bordas, tom mais quente perto da gengiva, textura e brilho que mudam com a luz.
  >
  > Por isso, na escultura à mão, a cor é trabalhada em camadas, pensando no seu rosto e no seu sorriso.
  >
  > Dra. Brenda Simeão, cirurgiã-dentista, CRO-GO 18788. Avaliação presencial, particular.
- **Título:** Facetas em resina esculpidas à mão
- **Descrição:** Goiânia – GO
- **Botão:** Enviar mensagem

### 4.2 Anúncio 2 — `preservacao_reel_A2`
- **Texto principal:**
  > Faceta estraga o dente?
  >
  > A proposta é ser o mais conservadora possível, com mínimo ou nenhum desgaste, conforme o caso. Só na avaliação a Dra. confirma o que é indicado para você.
  >
  > Dra. Brenda Simeão, cirurgiã-dentista, CRO-GO 18788. Avaliação presencial, particular.
- **Título:** Uma conversa sobre preservar o seu dente
- **Descrição:** Goiânia – GO
- **Botão:** Enviar mensagem

### 4.3 Anúncio 3 — `escultura_reel_A3`
- **Texto principal:**
  > Cada faceta, esculpida à mão, dente por dente.
  >
  > São 5 anos dedicados a facetas em resina, com planejamento individual para o seu rosto.
  >
  > Dra. Brenda Simeão, cirurgiã-dentista, CRO-GO 18788. Avaliação presencial, particular.
- **Título:** Escultura em resina, feita pela própria Dra.
- **Descrição:** Goiânia – GO
- **Botão:** Enviar mensagem

### 4.4 Anúncio 4 — `naturalidade_estatico_macro`
- **Texto principal:**
  > Dente natural não é de uma cor só.
  >
  > Na escultura à mão, textura, brilho e cor são trabalhados em camadas, pensando no seu rosto.
  >
  > Avaliação presencial, particular. Para conversar, toque em Enviar mensagem.
  >
  > Dra. Brenda Simeão, cirurgiã-dentista, CRO-GO 18788.
- **Título:** Facetas em resina com naturalidade
- **Descrição:** Goiânia – GO
- **Botão:** Enviar mensagem
- **Texto na arte (máximo 20% da área, sem selo, sem faixa de oferta):** "Dente natural não é de uma cor só"

### 4.5 Anúncio 5 — `naturalidade_estatico_chiclete`
- **Texto principal:**
  > Medo de ficar com cara de dente de chiclete? É uma preocupação legítima.
  >
  > Por isso cada caso é planejado individualmente: cor, formato e textura pensados para o seu rosto, e não um padrão igual para todos.
  >
  > Avaliação presencial, particular. Dra. Brenda Simeão, cirurgiã-dentista, CRO-GO 18788.
- **Título:** Cada sorriso, planejado para um rosto
- **Descrição:** Goiânia – GO
- **Botão:** Enviar mensagem
- **Texto na arte:** "Medo de ficar com cara de dente de chiclete?"

### 4.6 Checklist CFO aplicado (todas as linhas "sim" em cada anúncio)

| Regra | Anúncio 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Sem preço, parcelamento, promoção, brinde, desconto ou gratuidade | sim | sim | sim | sim | sim |
| Sem "avaliação gratuita", "sem compromisso" ou escassez ("vagas", "só hoje") | sim | sim | sim | sim | sim |
| Sem garantia ou promessa ("garantido", "para sempre", "100%") | sim | sim | sim | sim | sim |
| Sem superlativo ou comparação ("o melhor", "único", "mais natural") | sim | sim | sim | sim | sim |
| Sem crítica a outros profissionais ou ao trabalho alheio | sim | sim | sim | sim | sim |
| Sem "especialista" (consta "cirurgiã-dentista") | sim | sim | sim | sim | sim |
| CRO-GO 18788 presente | sim | sim | sim | sim | sim |
| Sem antes e depois, sem tecido biológico aberto, sem rosto de paciente | sim | sim | sim | sim | sim |
| Sem nome de clínica, endereço ou logo de terceiros | sim | sim | sim | sim | sim |
| Sem dado de saúde, queixa ou condição no texto | sim | sim | sim | sim | sim |
| Pós-graduação não citada (título exato ainda a confirmar) | sim | sim | sim | sim | sim |

Pontos de atenção que o Guilherme precisa conferir: o "5 anos dedicados a facetas em resina" do anúncio 3 vem do dossiê e do que a Dra. diz de si; **[OK DRA.]** confirmar que pode ser dito assim. O anúncio 5 trata de "dente de chiclete" como dúvida e não afirma nada sobre outros profissionais; se a Dra. achar que soa comparativo, usar só o texto do anúncio 4.

## 5. UTMs, ref_code e relação com Pixel/CAPI (EXP-27) e CRM (EXP-28)

### 5.1 O que se aplica a cada caminho

| Marca | Caminho B (esta campanha, WhatsApp direto) | Caminho A (LP, campanha futura) | Link da bio do Instagram |
|---|---|---|---|
| UTM na URL | **não existe** (não há URL de destino) | sim | sim |
| `ref_code` | **fixo por anúncio** (2.1) | gerado por sessão na LP | `IGBIO1` (já definido no calendário) |
| `ctwa_clid` | sim, vem do referral do WhatsApp (API oficial) | não | não |
| `fbclid`, `fbc`, `fbp` | não | sim (só após consentimento) | não |
| Pixel | não dispara (não passa pela LP) | `PageView`, `ViewContent`, `Contact`, `Lead` | não |
| CAPI | `Lead` qualificado e `Schedule` pelo CRM, ligados ao `ctwa_clid` e ao `ref_code` | `Contact`/`Lead` da LP + eventos do CRM com `ref_code` | `Lead` qualificado e `Schedule` pelo CRM |

**Consequência prática:** nesta campanha o Pixel da LP quase não participa; o sinal de conversão vem do CRM por CAPI. Mesmo assim o Pixel e a CAPI precisam estar corretos **antes** da campanha, porque a evolução da seção 1.5 e a campanha da LP dependem deles.

### 5.2 UTMs do Caminho A (LP), para ficarem definidos desde já

Formato fixo, tudo minúsculo, sem acento nem espaço, parâmetros dinâmicos da Meta onde existirem:

```
?utm_source=meta&utm_medium=paid&utm_campaign=facetas_gyn_lp&utm_content={{ad.name}}&utm_term={{adset.name}}
```

- `utm_content` carrega o **nome do anúncio** no padrão `<pilar>_<formato>_<variação>` (ex.: `naturalidade_reel_A1`). O CRM extrai o pilar de `utm_content` (campo `pilar_criativo`).
- Pilares aceitos: `naturalidade`, `preservacao`, `escultura`, `transformacao`.
- Não usar `utm_content` com acento, espaço ou o texto do anúncio.

### 5.3 Relação com o CRM (Twenty, workspace da Dra.)

| Campo no Twenty | Preenchido por | Origem |
|---|---|---|
| `origem` | automação | "Meta" quando há `ctwa_clid` ou `ref_code` de anúncio |
| `campanha`, `conjunto`, `criativo/pilar` | automação | referral do WhatsApp (`ad_id`, `adset_id`, `campaign_id`) e convenção de nome do anúncio |
| `ref_code`, `ctwa_clid` | automação | mensagem de entrada e referral |
| `utm_*`, `fbclid`, `fbc`, `fbp` | automação | só Caminho A |
| `score_qualificacao` | triagem | `triagem-whatsapp-brenda.md`, seção 4 |
| `event_id` | CRM | para CAPI sem duplicar |

Eventos enviados à Meta (de `crm-brenda.md` 1.5, sem mudança): `Lead` qualificado (`content_name=lead_qualificado`) e `Schedule` (`content_name=avaliacao_presencial`). **Sem valor, sem moeda, sem queixa, sem score, sem texto livre.** `Purchase` e comparecimento continuam desligados, salvo decisão em contrário.

### 5.4 Convenção de nomes (uma regra para tudo)

- Campanha: `[CBO] FACETAS GOIANIA [WHATS]`
- Conjunto: `A_amplo` e `B_interesses`
- Anúncio: `<pilar>_<formato>_<variação>`, igual ao `utm_content` e ao registro do `ref_code`.

Mudar o nome de um anúncio depois de ativo quebra a atribuição no CRM. Se mudar, registrar a equivalência na tabela de atribuição.

## 6. Regras de otimização e de pausa

Quem executa: o Guilherme (ou quem ele indicar). Revisão **semanal**, sempre na mesma manhã, com o relatório do EXP-28 aberto. Ajustes de verba no máximo +20% por vez, a cada 3 dias. Mudança de público, texto ou criativo em anúncio com aprendizado reinicia a fase; quando precisar mudar, **duplicar o anúncio em vez de editar**.

### 6.1 Primeiras 72 horas

Não mexer em nada (verba, público, anúncios), exceto as pausas de segurança da 6.3.

### 6.2 Regras de decisão por anúncio (a partir de 1.500 impressões e 30 cliques)

| Situação | Ação |
|---|---|
| Taxa de clique abaixo de metade da mediana dos anúncios da campanha, mesma janela | **pausar** o anúncio |
| Clique alto, mas **zero conversa** no WhatsApp com 30 cliques | **pausar** (reação ou curiosidade sem intenção, o padrão do engajamento que falhou em 2025) |
| Conversa, mas taxa de **qualificado por conversa** abaixo de metade da dos demais por duas semanas | **pausar**; revisar gancho (atrai fora de perfil) |
| Melhor taxa de qualificado por clique e `Schedule` | **manter e criar 2 variações de gancho** (seção 3.3) |
| Frequência acima de 3 em 7 dias no conjunto | trocar o criativo; não aumentar a verba |
| Custo por conversa acima de 2 vezes a mediana da campanha após 30 cliques | pausar |

"Mediana" e "metade" são relativos ao que a própria conta entregar; não há meta de custo definida em reais porque a semana 2 é que cria a referência (dossiê 4.4).

### 6.3 Pausa imediata, sem esperar mínimo de dados

- **Anúncio reprovado ou em análise por tempo anormal:** corrigir o texto ou o motivo, não repetir. Se a Meta reprovar o comparativo de imagem, usar a versão sem antes e depois.
- **Qualquer risco CFO** detectado (texto, comentário ou resposta que prometa preço, resultado, gratuidade, crítica; imagem com tecido aberto; rosto sem TCLE): pausar o anúncio **e** o conjunto se for estrutural, avisar a Dra. e refazer a aprovação.
- **Comentários negativos ou denúncia de paciente** sobre o anúncio: pausar o anúncio e responder de forma privada; não apagar comentário sem ver.
- **Tempo de primeira resposta acima de 15 minutos** na maior parte do dia (do relatório semanal): **pausar a campanha** até a resposta voltar ao normal; verba sem atendimento só queima o lead.
- **Saldo baixo:** a Meta já para quando o saldo zera; mesmo assim, avisar a Dra. quando restar cerca de 3 dias de verba diária (**V ÷ 30 × 3**), para o Pix cair antes.
- **Limite de gasto atingido** ou mudança de forma de pagamento: conferir e avisar.

### 6.4 Regras de verba

- Semanas 1 e 2: 90% de V ÷ 30 por dia; reserva de 10% de V.
- Semana 3 em diante: se o **custo por conversa qualificada** estiver estável por 3 dias e a taxa de resposta estiver no prazo, subir até +20% por vez.
- Se na semana 3 o acumulado do dossiê 4.4 estiver abaixo da meta (menos de 2 pacientes ou menos de 5 avaliações realizadas), **a ordem de revisão é a do dossiê**: (1) tempo de resposta e script, (2) qualidade do lead (pilar e público), (3) oferta e LP, (4) verba. **Verba é a última coisa a mexer.**
- Dias sem atendimento (feriado, viagem da Dra.): pausar a campanha, não reduzir a verba.

### 6.5 O que não se faz

Reativar qualquer campanha antiga. Duplicar a campanha de engajamento. Editar anúncio vencedor depois de ativo. Aumentar verba para compensar baixa taxa de resposta. Segmentar por condição de saúde. Mudar nome de anúncio depois de ativo.

## 7. Ordem de ligação

A ordem pedida era: saldo por Pix, limite de gasto, desativar a campanha de engajamento, Pixel, LP, robô. **Ajustei a ordem de duas etapas**, por um risco real: se o limite for removido e o saldo entrar com a campanha de engajamento ainda ativa, ela volta a gastar sozinha, no objetivo que não gera conversa. Por isso a pausa vem **primeiro**.

| # | Passo | Quem | Precisa de OK | Verificação |
|---|---|---|---|---|
| 0 | Conferir no Business Manager o que a leitura sugeriu: limite de gasto igual ao gasto, saldo zero, quem é o administrador da conta e se a Expoente tem acesso de parceiro com controle da conta e do Pixel | Guilherme | — | print de Configurações de pagamento, limite e papéis |
| 1 | **Pausar a campanha "Campanha trafego no Instagram"** (`23854221017180795`). Pausar, não apagar. | Guilherme | **[OK GUILHERME]** (é a primeira mudança na conta) | status "Pausada" no Gerenciador; leitura posterior confirma |
| 2 | **Saldo por Pix** da Dra.: o valor é decisão dela, a partir de V. Meta, com pré-pago, só veicula com saldo disponível | Dra. | **[OK DRA.]** | "Saldo disponível" maior que zero na conta |
| 3 | **Limite de gasto da conta:** remover ou elevar acima de V. Com pré-pago o saldo já limita o gasto; manter limite só se a Dra. quiser um teto por segurança, e então igual a V | Guilherme ou Dra. | **[OK GUILHERME + DRA.]** | limite maior que o gasto acumulado |
| 4 | **Pixel e CAPI:** usar o Pixel `737211919420986` (decisão do Guilherme, `tracking.md`); conferir atribuição à conta e domínio verificado no BM; endpoint CAPI no ar e testado com `test_event_code`; qualidade de correspondência de partida acima de 6 | Guilherme | **[OK GUILHERME]** para ativar em produção; token CAPI só em variável de ambiente | Events Manager mostra eventos de teste dedupados |
| 5 | **LP publicada** em domínio próprio, aviso de privacidade no ar, `noindex` liberado só depois, e domínio verificado no BM | Guilherme e Dra. | **[OK GUILHERME + DRA.]** | LP abre, consentimento funciona, Pixel só dispara após aceite |
| 6 | **Robô de triagem** (respostas fechadas) em ambiente de teste, com o aviso de privacidade publicado e a ciência do cliente. Número do WhatsApp na API oficial, se for usar a fase 2 | Guilherme | **[OK GUILHERME + DRA.]** (ciência por continuidade basta ou pede "OK" explícito, ver EXP-28) | 3 conversas de teste ponta a ponta: lead, score, handoff, CRM |
| 7 | **Montar a campanha em rascunho/pausada** conforme as seções 1 a 4 e a convenção de nomes (5.4). Registrar os `ref_code`. Zero verba. | Guilherme | **[OK GUILHERME]** para criar (nada foi criado agora) | rascunho conferido contra este documento |
| 8 | **Revisão final** de todos os textos e criativos contra o checklist CFO e aprovação por escrito da Dra. | Guilherme e Dra. | **[OK GUILHERME + DRA.]** | checklist 4.6 preenchido por anúncio |
| 9 | **Ativar** a campanha no horário em que a atendente esteja disponível (manhã de dia útil), com a verba da fase de 90% | Guilherme | **[OK GUILHERME]** | primeira conversa chega ao CRM com origem preenchida |

**O que trava a ativação (passos 0 a 8):** sem saldo, sem limite liberado, sem Pixel testado, sem aviso de privacidade ou sem robô e atendimento prontos, a campanha **não deve ser ativada**. Não é possível "ligar o anúncio e ajustar depois": lead no WhatsApp sem triagem e sem CRM não volta.

## 8. Lista do que precisa de OK

**Guilherme:**
1. Pausar a campanha "Campanha trafego no Instagram" (primeira ação, seção 7, passo 1).
2. Alterar o limite de gasto da conta (com a Dra.).
3. Aceitar `ref_code` fixo por anúncio no Caminho B.
4. Confirmar a documentação vigente da Meta sobre CAPI de mensagem e a API oficial do WhatsApp.
5. Subir os dois conjuntos juntos ou só o A (seção 1.2).
6. Ativar Pixel e CAPI em produção, criar a campanha em rascunho e ativá-la.
7. A decisão da verba V, junto com a Dra.
8. Aprovar a campanha seguinte, do Caminho A (LP), só depois de a LP estar publicada.

**Dra.:**
1. Pix e valor de V (a verba mensal).
2. Aprovar por escrito cada texto de anúncio e cada criativo (checklist CFO).
3. Confirmar "5 anos dedicados a facetas em resina" e o título da pós-graduação (que **não** é citado nos anúncios).
4. Gravar os 3 Reels (guia em `roteiros-gravacao.md`) e o termo de divulgação das imagens macro.
5. Número de WhatsApp, página e Instagram ligados ao WhatsApp.

## 9. Pendências conhecidas

- A varredura da Ads Library (dossiê 1.4) não foi feita: os ângulos dos criativos são hipóteses.
- Os conjuntos e as exclusões foram desenhados sem testar o tamanho do público na ferramenta (leitura só). Estimar o público ao criar o rascunho, evitando um conjunto pequeno demais (em Goiânia e raio de 25 km o público com 28 a 50 anos é amplo, mas conferir).
- Sem meta de custo definida. A referência sai das semanas 1 e 2.
- Se a conta for usada por outro tráfego depois, rever o nome da campanha e a atribuição.

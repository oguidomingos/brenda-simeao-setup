# CRM da Dra. Brenda Simeão no Twenty




Marcação: **[aprovação pendente]** = não ligar antes da aprovação dele.

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
| tratamento_anterior | select fechado: sim, nao, prefere_dra | pergunta 4, se mantida **[aprovação pendente]**; não pontua |
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

Criar as opções de `etapa` no Twenty exige escrita: **[aprovação pendente]**.

| # | Etapa | Entra quando | Quem move |
|---|---|---|---|
| 1 | Lead | 1ª mensagem recebida (WhatsApp) ou envio do formulário da LP | automático |
| 2 | Qualificado | score 4 ou 5 na triagem | automático por regra de score |
| 3 | Avaliação agendada | data/hora confirmada pelo lead | atendente (ou bot ao confirmar) |
| 4 | Compareceu | presença na avaliação | recepção, no dia |
| 5 | Fechou | aceite do plano apresentado pessoalmente | Dra. |
| 6 | Perdido | encerrado com motivo | atendente/Dra. |

Estados laterais (não são etapas): morno = score 2 ou 3, fica em Lead com tag `nutricao` e retorno em 7 dias; no-show = `comparecimento = no_show`, volta a Perdido só após resgate sem resposta. O dossiê tinha "Em triagem" e "Plano apresentado"; foram fundidos (triagem vira estado de Lead; plano apresentado vira parte de Compareceu) para ficar nas 6 etapas pedidas. **[aprovação pendente]**

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
| Compareceu | nenhum por padrão; fica só no CRM | **[aprovação pendente]** recomendação: não enviar evento de comparecimento a uma avaliação odontológica ao Meta |
| Fechou | nenhum por padrão. `Purchase` só se a Dra. autorizar enviar valor | **[aprovação pendente: Guilherme e Dra.]**; sem autorização, enviar evento personalizado `PlanoFechado` sem valor, ou nada (recomendação: nada, para manter dado de tratamento fora do Meta) |
| Perdido | nenhum | não se envia evento negativo |



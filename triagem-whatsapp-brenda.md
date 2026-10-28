# Triagem no WhatsApp e resgate de cliques (EXP-28)

Versão 1 · 28/10/2026 · Desenho. Nenhuma mensagem foi enviada. Tudo marcado **[OK GUILHERME]** exige aprovação antes de ligar.

Modelo de dados e etapas: `crm-brenda.md`. Este documento substitui, para a automação, o roteiro longo do dossiê (2.3), que tinha perguntas sobre tratamento prévio e queixa em formato de entrevista. O roteiro longo segue valendo só para conversa humana da atendente depois do handoff.

## 1. Regras fixas

- Uma pergunta por mensagem, voz da Dra.: calma, acolhedora, sem exclamação em excesso. No máximo um emoji discreto, ou nenhum (padrão desta versão: nenhum).
- Nunca preço, parcelamento, desconto, promoção, "avaliação gratuita" ou "vagas limitadas". Pergunta de valor usa o bloco padrão do dossiê (2.3, "Pediu valor").
- A automação abre a conversa e coleta 3 respostas; a continuidade é humana. Nunca assinar como "assistente virtual".
- Fora do horário: uma única mensagem de acolhimento (modelo 0 do dossiê), depois silêncio até abrir.

## 2. As 3 perguntas

Mensagem de entrada do lead (pré-preenchida na LP): "Olá, Dra Brenda! Quero avaliar meu sorriso."

**Abertura** (dentro de 15 min no horário comercial)
> Olá, {nome}. Aqui é do consultório da Dra Brenda Simeão. Obrigada pelo seu contato. Para eu te direcionar melhor, vou te fazer três perguntas rápidas.

**Pergunta 1: cidade**
> Em qual cidade você mora?

**Pergunta 2: o que gostaria de mudar** (aberta, no registro estético)
> Como você imagina o seu sorriso ideal? Pode me contar com suas palavras.

**Pergunta 3: prazo**
> Você pensa em fazer isso em quanto tempo: neste mês, nos próximos três meses ou mais para frente?

**Confirmação final (afirmação, não é a 4ª pergunta)**
> A Dra Brenda começa sempre por uma avaliação presencial e particular, em que ela analisa o seu caso com calma. Faz sentido para você começar por aí?

Não perguntar, em nenhum momento: dor, doenças, medicamentos, gestação, alergias, tratamento anterior, estado dos dentes, fotos da boca. Se o lead oferecer esse tipo de informação por conta própria, a atendente humana não aprofunda ("Isso a Dra Brenda avalia com você pessoalmente") e o dado não é copiado para campos estruturados.

**[OK GUILHERME]** texto exato das perguntas, em especial a 2, que é texto livre e pode induzir o lead a descrever situação de saúde. Alternativa mais restrita: oferecer botões (mais natural, mais discreto, ainda não sei) em vez de texto livre. Recomendação: texto livre curto, com tratamento restrito descrito na seção 3.

## 3. O que vai para o CRM e o que não vai

| Dado | CRM | Meta (Pixel/CAPI) | Observação |
|---|---|---|---|
| Nome, telefone | sim | só em hash SHA-256 (telefone E.164, nome minúsculo sem acento) | para correspondência, nunca em claro |
| Cidade | sim | **não** | usada só no score |
| Resposta 2 em texto (`desejo_texto`) | sim, campo restrito | **nunca** | só a Dra. e a atendente veem; nunca em relatório |
| `desejo_categoria` (cor, formato, alinhamento, outro) | sim | sim, só como categoria genérica | preenchida pela atendente, não pelo lead |
| Prazo | sim | **não** | |
| Score | sim | **não** | |
| `ref_code`, `fbclid`, `fbc`, `fbp`, `ctwa_clid`, UTMs | sim | sim (`fbc`, `fbp`, `ctwa_clid` em `user_data`) | atribuição |
| Dado de saúde de qualquer tipo | **não coletado** | **não** | se aparecer espontaneamente, não vira campo estruturado |
| Valor em reais | não existe no funil | só se a Dra. autorizar `Purchase` | ver `crm-brenda.md` 1.5 |

Regras de LGPD do contrato (resumo operacional): imagem e dado ligado a saúde são dados sensíveis; só tratar com consentimento, finalidade definida e acesso restrito; nada clínico sai do CRM para plataforma de anúncio; retenção e exclusão sob pedido do titular. **[OK GUILHERME]** conferir com o texto real da cláusula do contrato antes de ligar, porque este documento resume sem ter o contrato em mãos.

## 4. Score de 0 a 5 e handoff

Cada critério vale 1 ponto (critérios do dossiê 2.3):

| Ponto | Critério | De onde vem |
|---|---|---|
| 1 | Mora em Goiânia ou região | Pergunta 1 |
| 1 | Desejo estético claro | Pergunta 2 (resposta que descreve mudança desejada) |
| 1 | Interesse em facetas/lentes em resina ou abertura para avaliar | Pergunta 2 ou confirmação final |
| 1 | Prazo de até 90 dias | Pergunta 3 |
| 1 | Aceita avaliação presencial particular | Confirmação final |

Classificação:
- **4 a 5: Qualificado.** Etapa muda para Qualificado, dispara `Lead` qualificado, e há **handoff para a Dra.** (ou atendente indicada por ela): notificação interna com nome, telefone, cidade, prazo e o desejo em texto, e a atendente assume para propor dois horários.
- **2 a 3: Morno.** Fica em Lead com tag `nutricao`; a Dra. não é acionada. Mensagem: "Claro, sem pressa. Se quiser, te envio alguns casos e um conteúdo da Dra sobre como funciona. Fico por aqui." Retorno em 7 dias.
- **0 a 1: Fora de perfil.** Encerramento cordial do dossiê ("Obrigada pelo carinho de nos procurar... fico à disposição se mudar de ideia"), motivo de perda registrado.

Score calculado por regra simples (cidade em lista de Goiânia e região, prazo escolhido, resposta sim/não na confirmação); o ponto de "desejo estético claro" é confirmado por humano para não depender de classificador automático sobre texto de saúde. Só o lead qualificado chega à Dra.

## 5. Resgate de cliques sem resposta

Situações: (a) clicou no WhatsApp (evento `Contact`) mas não mandou mensagem; (b) mandou a mensagem de entrada e parou de responder na triagem.

**Caso (a), clique sem conversa:** não existe contato do lead no WhatsApp, então **não se envia nada** (não há telefone nem consentimento). Só registrar no relatório como "cliques sem conversa". Resgate possível apenas via remarketing do anúncio, que é decisão de campanha, fora deste documento.

**Caso (b), conversa iniciada pelo lead que parou:**

| Quando | Ação |
|---|---|
| 24 h sem resposta do lead | 1ª mensagem de retomada |
| 72 h após a 1ª | 2ª e última mensagem de retomada |
| 7 dias sem resposta | encerrar: etapa Perdido, motivo "Sem resposta após resgate" |

- **Limite: 2 tentativas** (a menos que o dossiê mantenha 3 toques; este desenho escolhe 2 por cautela de política do WhatsApp e do tom). **[OK GUILHERME: 2 ou 3 tentativas]**
- Só enviar dentro da janela de 24 h do WhatsApp com mensagem livre. Fora dela, usar modelo (template) aprovado. A 1ª retomada às 24 h pode cair no limite da janela: **templates precisam ser aprovados na Meta antes de ligar**. **[OK GUILHERME]**
- Horário de envio: 9h às 19h, dias úteis e sábado manhã. Nunca à noite.
- Se o lead responder "pare", "não quero" ou equivalente: encerra na hora, marca "não contatar" e não envia mais nada.
- Lead que respondeu depois do resgate volta ao fluxo no ponto onde parou.

**Mensagem de retomada 1 (neutra):**
> Olá, {nome}. Aqui é do consultório da Dra Brenda Simeão. Vi que sua conversa ficou em aberto. Se ainda tiver interesse, é só me responder por aqui e continuamos de onde paramos.

**Mensagem de retomada 2 (última):**
> {nome}, só passando para dizer que fico à disposição. Se quiser retomar mais adiante, é só escrever. Obrigada pelo seu contato.

Proibido nas duas: preço, parcelamento, promoção, desconto, urgência ("últimas vagas"), "avaliação gratuita", menção ao procedimento ou a qualquer condição de saúde, emoji de oferta.

Follow-up pós-agendamento (D-1, 2 horas antes, no-show) segue o dossiê 2.3 passo 8; o no-show usa a mesma regra de 1 retomada neutra e depois encerra.

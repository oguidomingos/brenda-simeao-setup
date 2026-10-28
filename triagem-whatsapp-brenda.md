# Triagem no WhatsApp e resgate de cliques (EXP-28)

Versão 2 · 28/10/2026 · Desenho, fase 2. Nenhuma mensagem foi enviada. Tudo marcado **[OK GUILHERME]** exige aprovação antes de ligar.

Decisão do Guilherme em 28/10: todas as perguntas têm **resposta em opções fechadas** (botões ou números), sem campo de texto livre. Motivo: cláusula 7.3 do contrato, a automação faz apenas a qualificação inicial, sem coletar dados clínicos ou de saúde sensíveis. Esta versão substitui a 1, em que a pergunta 2 era aberta.

Modelo de dados e etapas: `crm-brenda.md`. Este documento substitui, para a automação, o roteiro longo do dossiê (2.3). O roteiro longo segue valendo só para conversa humana da atendente depois do handoff, e a mensagem pré-preenchida "com resumo do formulário (nome, queixa, prazo, tratamento anterior)" citada no dossiê (seção 2.2) **não é usada**: a mensagem de entrada é só a frase padrão.

## 1. Regras fixas

- Uma pergunta por mensagem, voz da Dra.: calma, acolhedora, sem exclamação em excesso, sem emoji.
- Toda pergunta traz as opções numeradas no texto. Com API oficial do WhatsApp, as mesmas opções saem como botões (até 3) ou lista (até 10); em ferramenta sem botões, o lead responde com o número. O sistema só aceita número, identificador do botão ou o texto exato da opção (comparação normalizada, sem interpretar o sentido).
- Toda pergunta tem uma saída: "Prefiro falar direto com a Dra." Quem escolhe vai para atendimento humano e a triagem para ali, sem penalidade de score.
- Nunca preço, parcelamento, desconto, promoção, "avaliação gratuita" ou "vagas limitadas". Pergunta de valor usa o bloco padrão do dossiê (2.3, "Pediu valor"), que é resposta humana.
- A automação abre a conversa e coleta no máximo quatro toques de resposta; a continuidade é humana. Nunca assinar como "assistente virtual".
- Fora do horário: uma única mensagem de acolhimento (modelo 0 do dossiê) com o aviso de privacidade, depois silêncio até abrir.

## 2. Roteiro (opções fechadas)

Mensagem de entrada do lead (pré-preenchida na LP): "Olá, Dra Brenda! Quero avaliar meu sorriso. (ref ABC123)".

**Abertura, com ciência de privacidade** (dentro de 15 min no horário comercial)
> Olá, {nome}. Aqui é do consultório da Dra Brenda Simeão. Obrigada pelo seu contato.
>
> Para te direcionar melhor, vou fazer três perguntas rápidas, todas de escolher uma opção. Vamos usar seu nome, telefone e suas escolhas apenas para organizar o seu atendimento, e o consultório é o responsável por esses dados. Detalhes no aviso de privacidade: {URL_AVISO_PRIVACIDADE}
>
> Não é preciso enviar nenhuma informação de saúde por aqui: isso a Dra conversa com você pessoalmente. Se não quiser continuar, é só responder PARAR.

`{URL_AVISO_PRIVACIDADE}` é o aviso que a LP terá (tarefa separada). **Não ligar a automação enquanto esse link não existir e não estiver publicado.** Registro de ciência: a continuação da conversa após a abertura (resposta à pergunta 1) grava `consentimento_contato = verdadeiro` com data e a versão do texto; resposta PARAR grava "não contatar". **[OK GUILHERME + Dra.]** que a ciência por continuidade basta como mecanismo de ciência/consentimento da 7.3, ou se há pedido de "OK" explícito antes da pergunta 1 (mais seguro, custa um toque).

**Pergunta 1: cidade**
> Em qual cidade você mora?
> 1. Goiânia
> 2. Aparecida de Goiânia
> 3. Outra cidade da região metropolitana de Goiânia
> 4. Outra cidade ou estado
> 5. Prefiro falar direto com a Dra.

**Pergunta 2: o que gostaria de melhorar** (opções neutras e estéticas; sem queixa, dor, doença ou diagnóstico)
> O que você gostaria de melhorar no seu sorriso?
> 1. O formato dos dentes
> 2. A cor
> 3. O alinhamento visual
> 4. Outro aspecto estético
> 5. Prefiro falar direto com a Dra.

**Pergunta 3: prazo**
> Em quanto tempo você pensa em fazer isso?
> 1. Neste mês
> 2. Nos próximos três meses
> 3. Mais para frente
> 4. Prefiro falar direto com a Dra.

**Pergunta 4, toque único: tratamento anterior** (só opção fechada, sem detalhe)
> Você já fez algum tratamento com foco estético antes?
> 1. Sim
> 2. Não
> 3. Prefiro falar direto com a Dra.

Esta pergunta foi pedida pelo Guilherme, mas ela eleva a conta de três para quatro toques. O dado não pontua, não vai ao Meta e fica como `tratamento_anterior` (sim, nao, prefere_dra). **[OK GUILHERME]** manter como quarto toque, juntar com outra ou retirar. Recomendação: manter só se a Dra. disser que usa a informação já no primeiro contato; é a pergunta mais próxima de histórico clínico, então, na dúvida, retirar e deixar para a conversa humana.

**Confirmação final** (afirmação com escolha, não é pergunta de saúde)
> A Dra Brenda começa sempre por uma avaliação presencial e particular, em que ela analisa o seu caso com calma. Podemos ver horários para você?
> 1. Sim, quero ver horários
> 2. Quero pensar um pouco antes
> 3. Prefiro falar direto com a Dra.

Não perguntar, em nenhum momento: dor, doenças, medicamentos, gestação, alergias, estado dos dentes, fotos da boca, nem pedir que a pessoa descreva qualquer coisa com as próprias palavras.

### 2.1 Se a pessoa escrever texto livre (ou mandar foto, áudio, documento)

O robô **não armazena, não interpreta e não repassa** o conteúdo. Mensagem que não for uma das opções (nem o texto exato de uma opção) é tratada assim:

1. O conteúdo da mensagem não é gravado em nenhum campo do CRM, nem em log do serviço de automação, nem na notificação ao humano. O sistema guarda apenas o fato: `texto_livre_recebido = verdadeiro`, data e hora, e a pergunta em que ocorreu. Mídia (foto, áudio, documento) não é baixada.
2. Resposta única, sempre a mesma, sem eco do que a pessoa escreveu:
> Obrigada por compartilhar. Esse assunto a Dra Brenda trata diretamente com você, pessoalmente, e ela vai poder te ouvir com a atenção que merece. Vou encaminhar a sua conversa para a equipe dela continuar por aqui.
3. A triagem para. Etapa Lead, tag `fala_direta`, handoff humano imediato. A notificação à atendente traz nome, telefone e as respostas fechadas já dadas, mais o aviso "recebeu texto livre, ler na conversa". O texto fica apenas dentro da conversa do WhatsApp, que é da Dra. (cláusula 9.1: o número é dela).
4. A atendente humana não aprofunda e não copia para campo estruturado ("Isso a Dra Brenda avalia com você pessoalmente").
5. Exceção: PARAR, "não quero", "sair" e equivalentes encerram, marcam "não contatar" e não geram handoff.

Ponto técnico que precisa de checagem antes de ligar: a ferramenta de mensagens (Evolution API, na VPS da Expoente, cláusula 9.5) pode persistir o conteúdo das mensagens no próprio banco. Para valer a regra acima, a persistência de corpo de mensagem deve ficar desligada ou com expurgo curto, e o log do serviço de triagem não pode registrar o corpo. **[OK GUILHERME]** conferir a configuração real e decidir o prazo de expurgo; este documento não alterou nada.

## 3. O que vai para o CRM e o que não vai ao Meta

| Dado | CRM | Meta (Pixel/CAPI) | Observação |
|---|---|---|---|
| Nome, telefone | sim | só em hash SHA-256 (telefone E.164, nome minúsculo sem acento) | para correspondência, nunca em claro |
| Cidade (faixa: goiania, aparecida, regiao, outra) | sim, campo fechado | **não** | usada só no score |
| Desejo (`desejo_categoria`: formato, cor, alinhamento_visual, outro, prefere_dra) | sim, escolhido pelo lead | **não** | só em contagens agregadas do relatório; nada individual |
| Prazo (ate_30d, ate_90d, mais_90d) | sim | **não** | |
| `tratamento_anterior` (sim, nao, prefere_dra) | sim, se mantido **[OK GUILHERME]** | **não** | não pontua |
| Score | sim | **não** | |
| Texto livre recebido | **só o fato** (`texto_livre_recebido`, data); conteúdo nunca | **nunca** | seção 2.1 |
| `ref_code`, `fbclid`, `fbc`, `fbp`, `ctwa_clid`, UTMs | sim | sim (`fbc`, `fbp`, `ctwa_clid` em `user_data`) | atribuição |
| Consentimento (data, versão do aviso) | sim | **não** | |
| Dado de saúde de qualquer tipo | **não coletado** | **não** | se aparecer espontaneamente, fica só na conversa |
| Valor em reais | não existe no funil | só se a Dra. autorizar `Purchase` | ver `crm-brenda.md` 1.5 |

Regra para o Meta: **nada de saúde e nada do conteúdo da triagem**. Ao Meta vão apenas identificadores de correspondência em hash, os identificadores de clique e anúncio, o nome do evento e o `pilar_criativo` (que descreve o anúncio, não a pessoa). Isto é mais restrito que a versão 1 e que o exemplo do dossiê (4.3, `queixa=cor|formato|alinhamento`): categoria de desejo não sai mais do CRM. **[OK GUILHERME]** confirmar a restrição maior.

Regras de LGPD do contrato (cláusula 7): a Dra. é a controladora e a Expoente a operadora (7.2); a automação não coleta dado clínico (7.3); medidas de segurança e nenhum uso para finalidade própria (7.4); aviso de incidente em até 48 horas (7.5); CSV da base e eliminação das cópias em até 30 dias no fim (7.6). Texto conferido contra `/root/projects/brenda-contrato/contrato.html` em 28/10.

## 4. Score de 0 a 5 e handoff (respostas fechadas)

Cada critério vale 1 ponto e sai só de escolha de opção:

| Ponto | Critério | Regra |
|---|---|---|
| 1 | Mora em Goiânia ou região | Pergunta 1, opções 1 a 3 |
| 1 | Desejo estético escolhido | Pergunta 2, opções 1 a 3 (opção 4 "outro" vale 0) |
| 1 | Prazo de até 90 dias | Pergunta 3, opções 1 ou 2 |
| 1 | Aceita avaliação presencial particular | Confirmação, opção 1 |
| 1 | Entrada por intenção declarada de avaliar o sorriso | Mensagem de entrada com `ref_code` válido (LP) ou anúncio de conversa (`ctwa_clid`) |

O quinto critério substitui o ponto "interesse em facetas/lentes" do dossiê, que dependia de ler texto livre. **[OK GUILHERME]** aceitar esta substituição. A opção "prefiro falar direto com a Dra." não pontua nem penaliza: leva a handoff humano com tag `fala_direta`, e a pessoa não entra em "fora de perfil". Tratamento anterior não pontua.

Classificação:
- **4 a 5: Qualificado.** Etapa muda para Qualificado, dispara `Lead` qualificado ao Meta (sem parâmetros de triagem), e há **handoff para a Dra.** (ou atendente indicada por ela): notificação interna com nome, telefone, faixa de cidade, prazo e categoria de desejo; a atendente assume para propor dois horários.
- **2 a 3: Morno.** Fica em Lead com tag `nutricao`; a Dra. não é acionada. Mensagem: "Claro, sem pressa. Se quiser, te envio alguns casos e um conteúdo da Dra sobre como funciona. Fico por aqui." Retorno em 7 dias.
- **0 a 1: Fora de perfil.** Encerramento cordial do dossiê ("Obrigada pelo carinho de nos procurar... fico à disposição se mudar de ideia"), motivo de perda registrado.
- **Fala direta** (escolha de "prefiro falar direto com a Dra." em qualquer pergunta, ou texto livre): fora do score, handoff humano imediato.

Score por regra simples sobre opções fechadas, sem classificador de texto e sem etapa humana de interpretação. Só o lead qualificado ou de fala direta chega à Dra.

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

**Templates para aprovação na Meta** (categoria utilidade, sem variável além do nome, mesmo texto das retomadas 1 e 2, mais a abertura da seção 2 quando a janela de 24 h estiver fechada). Nomes sugeridos: `retomada_1`, `retomada_2`, `abertura_privacidade`. Texto neutro, sem preço, promoção, desconto, urgência ou "avaliação gratuita". Nenhum template foi submetido. **[OK GUILHERME]** submeter.

Resposta do lead a uma retomada segue as mesmas regras da seção 2: se vier opção fechada ou "continuar", retoma no ponto onde parou; se vier texto livre, aplica-se a seção 2.1 (não armazenar, encaminhar à Dra.).

Proibido nas duas: preço, parcelamento, promoção, desconto, urgência ("últimas vagas"), "avaliação gratuita", menção ao procedimento ou a qualquer condição de saúde, emoji de oferta.

Follow-up pós-agendamento (D-1, 2 horas antes, no-show) segue o dossiê 2.3 passo 8; o no-show usa a mesma regra de 1 retomada neutra e depois encerra.

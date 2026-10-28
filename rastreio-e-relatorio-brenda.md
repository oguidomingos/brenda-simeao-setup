# Rastreio de origem e relatório semanal (EXP-28)

Versão 1 · 28/10/2026 · Desenho. Nada foi ligado. **[OK GUILHERME]** marca o que precisa de aprovação antes de ativar.

Campos mencionados estão definidos em `crm-brenda.md` (1.1). Conformidade de dados em `triagem-whatsapp-brenda.md` (seção 3).

## 1. Rastreio de origem até o registro do lead

Objetivo: cada Pessoa/Oportunidade no Twenty carrega `fbclid`, `utm_*` e `ref_code` (e `fbc`, `fbp`, `ctwa_clid` quando houver) para atribuir lead, agendamento e fechamento ao anúncio e ao pilar criativo certo.

### 1.1 Caminho A: clique do anúncio para a LP e depois WhatsApp

1. O anúncio leva à LP com UTMs fixos por anúncio: `utm_source=meta`, `utm_medium=paid`, `utm_campaign=<nome>`, `utm_content=<pilar>_<variacao>` (pilar: naturalidade, preservacao, escultura, transformacao), `utm_term` opcional. O Meta acrescenta `fbclid` sozinho.
2. A LP (só após consentimento de cookies, **[OK GUILHERME]** texto do banner) lê UTMs, `fbclid`, e os cookies `_fbc` e `_fbp`. Se houver `fbclid` e não houver `_fbc`, monta `fb.1.<timestamp>.<fbclid>`.
3. A LP envia um POST ao serviço do servidor (`/webhook/lp-click`) com esses dados mais IP e user agent. O servidor gera um `ref_code` curto (6 a 8 caracteres, sem significado) e grava a linha `ref_code -> {utm_*, fbclid, fbc, fbp, página, horário}` na tabela de atribuição, com `event_id` do `Contact`.
4. O botão de WhatsApp é aberto com texto pré-preenchido que inclui só o código: "Olá, Dra Brenda! Quero avaliar meu sorriso. (ref ABC123)". Nada de UTM nem fbclid no texto.
5. Quando a primeira mensagem chega ao webhook do WhatsApp, o serviço extrai `ref_code` por regex, busca na tabela, e cria ou atualiza a Pessoa (chave: telefone E.164) copiando `utm_*`, `fbclid`, `fbc`, `fbp`, `ref_code`, `pilar_criativo` (de `utm_content`) e `primeiro_contato_em`. Cria a Oportunidade na etapa Lead.
6. Se o lead apagar o código antes de enviar: sem `ref_code`, a origem fica "desconhecida (WhatsApp direto)". Mitigação secundária: casar por janela de tempo (clique em `Contact` e mensagem recebida em até 10 minutos, único candidato) e marcar `origem_inferida = true`. **[OK GUILHERME]** aceitar a inferência ou deixar como desconhecida.

Alternativa de formulário da LP: o envio do formulário já grava tudo direto (mesmos campos) e gera `Lead` no Pixel com `event_id` dedupado com o CAPI.

### 1.2 Caminho B: anúncio de conversa (click-to-WhatsApp)

1. O anúncio abre o WhatsApp direto, sem LP. A mensagem de entrada traz `ctwa_clid` e metadados do anúncio (ID do anúncio, conjunto, campanha) no webhook de mensagem da API oficial do WhatsApp Business (campo de referral).
2. O serviço grava `ctwa_clid`, `ad_id`, `adset_id`, `campaign_id` e, via nome do anúncio, o `pilar_criativo` (convenção de nome do anúncio: `<pilar>_<variacao>`).
3. Sem `fbclid`, `fbc` ou `ref_code`: a atribuição é por `ctwa_clid`. Eventos CAPI de mensagem usam `action_source = business_messaging` com `ctwa_clid` e `page_id`, ou o fluxo de conversão de conversa da Meta. **[OK GUILHERME]** confirmar com a documentação vigente da Meta e se o número estará na API oficial, porque o app do WhatsApp Business comum não entrega o referral completo.
3b. Dependências: número em API oficial (ou ferramenta de atendimento que repasse o referral), página do Facebook e conta de anúncios vinculadas ao WhatsApp. Ainda não definido pela Dra.; ver `dominio-e-acessos.md`.

### 1.3 Regras comuns

- Dedupe por telefone: o mesmo telefone chegando por A e depois por B atualiza a mesma Pessoa; a origem de primeiro toque fica em `origem_primeiro_toque` e a última em `origem_ultimo_toque` (campo adicional **[OK GUILHERME]**).
- Sem consentimento de cookies: a LP não grava `fbp`/`fbc`; o `ref_code` é gerado sem dado de navegador e a origem fica só com UTM da URL.
- Retenção: tabela de atribuição guarda `ref_code` sem prazo além de 90 dias se não casar com nenhum lead. **[OK GUILHERME]** definir retenção.
- Teste de aceite antes de ligar: 3 cliques de teste em cada caminho, conferir que o registro no Twenty (ambiente de teste) traz os campos e que o `event_id` bate entre navegador e servidor.

## 2. Relatório semanal

Enviado à Dra. e à equipe Expoente toda segunda-feira, cobrindo segunda a domingo anteriores. O texto enviado usa **contagens e proporções, sem nenhum valor em reais**. Nenhum dado de paciente individual nem de saúde aparece.

### 2.1 Métricas

| Métrica | Definição | Fonte |
|---|---|---|
| Leads | Oportunidades criadas na semana (etapa Lead em diante) | Twenty |
| Qualificados | Leads que chegaram à etapa Qualificado; proporção = qualificados / leads | Twenty |
| Avaliações agendadas | Entradas em Avaliação agendada; proporção = agendadas / qualificados | Twenty |
| Avaliações realizadas | Entradas em Compareceu | Twenty |
| Comparecimento | realizadas / agendadas com data na semana | Twenty |
| Fechamentos | Entradas em Fechou; proporção = fechamentos / realizadas | Twenty |
| Custo por avaliação agendada | Investimento da semana / agendadas. **No texto enviado, aparece como índice relativo**, não em reais (2.3) | Meta + Twenty |
| Origem | Distribuição de leads, qualificados e agendadas por pilar criativo e por canal (LP, anúncio de conversa, direto/desconhecido), em porcentagem | Twenty |
| Cliques sem conversa | Eventos `Contact` sem mensagem associada; proporção sobre cliques | LP + Twenty |
| Tempo da 1ª resposta | Mediana em minutos no horário comercial | Twenty |
| Perdas por motivo | Distribuição dos motivos de perda, em porcentagem | Twenty |

Meta de referência (dossiê 4.4): 1 fechamento por semana, 2 avaliações realizadas, 3 agendadas, 6 a 8 qualificados, resposta em até 15 minutos.

### 2.2 Modelo do relatório (texto enviado)

> **Relatório semanal, Dra. Brenda Simeão, semana de {dd/mm} a {dd/mm}**
>
> **Funil**
> - Leads: {n} ({variação} em relação à semana anterior)
> - Qualificados: {n} ({x}% dos leads)
> - Avaliações agendadas: {n} ({x}% dos qualificados)
> - Avaliações realizadas: {n}; comparecimento {x}%
> - Fechamentos: {n} ({x}% das avaliações realizadas)
> - Meta da semana: {atingida / parcial / abaixo}
>
> **Eficiência**
> - Custo por avaliação agendada: índice {i} (semana de referência = 100); {acima/abaixo} da semana anterior
> - Cliques sem conversa: {x}% dos cliques
> - Primeira resposta: mediana de {m} minutos
>
> **Origem**
> - Por pilar: naturalidade {x}%, preservação {x}%, escultura {x}%, transformação {x}% (leads); {pilar} lidera em agendamentos
> - Por canal: LP {x}%, anúncio de conversa {x}%, direto {x}%
>
> **Perdas:** {motivo 1} {x}%, {motivo 2} {x}%, {motivo 3} {x}%
>
> **Leitura da semana e próxima ação:** {2 a 3 linhas: onde o funil travou e o que mudaremos}. Regra do dossiê: se na semana 3 o acumulado estiver abaixo de 2 pacientes ou 5 avaliações realizadas, revisar nesta ordem: resposta e roteiro, qualidade do lead, LP, orçamento.

### 2.3 Custo sem valor em reais

O relatório enviado nunca traz o valor. Cálculo interno (não enviado): investimento da semana dividido pelas avaliações agendadas. No texto: índice relativo (semana-base igual a 100), ou a razão "custo por agendada em relação ao custo por lead". O cálculo interno com valores fica em planilha/painel interno da Expoente. **[OK GUILHERME]** confirmar se a Dra. recebe o relatório sem valor ou se há uma versão interna separada com valores.

### 2.4 Painel e geração

- View do Twenty por semana e por `pilar_criativo` com as contagens acima (leitura).
- Investimento vem do Meta Ads (leitura de insights); a geração do texto é por script que lê Twenty e Meta e preenche o modelo, gerando rascunho para revisão humana. **O envio à Dra. não é automático.** **[OK GUILHERME]** antes de qualquer envio automático, canal e horário.
- Primeira edição só depois de 2 semanas de dado real, para o custo e as proporções terem base.

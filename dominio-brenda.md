# Domínio da Dra. Brenda Simeão: consulta e plano de compra

Documento interno da Expoente. Consulta feita em 29/10/2026. Nada foi comprado, nenhum pedido criado, nenhum DNS ou registro alterado, nenhuma mensagem enviada.

Fontes: API da Hostinger (disponibilidade, catálogo, perfis WHOIS e lista de domínios da conta, só leitura), especificação oficial da API (`developers.hostinger.com/openapi/openapi.json`) e RDAP do Registro.br.

## 0. Correção importante sobre o .med.br

No repositório a Dra. aparece como **cirurgiã-dentista (CRO-GO 18788)**, não médica. O `.med.br` é a categoria de medicina (exige CRM), então **não serve para ela**. A categoria equivalente da odontologia é o **`.odo.br`** (exige CRO). Incluí o `brendasimeao.odo.br` na consulta. A exigência de comprovação de CRM/CRO é regra do Registro.br para essas categorias; **não confirmei hoje** o texto vigente (a página de categorias do Registro.br carrega por script e não abriu pela linha de comando).

## 1. Disponibilidade e preço (Hostinger, 29/10/2026)

Preços da conta Hostinger em BRL, no catálogo da API. "1º ano" é o preço promocional; "renovação" é o preço cheio dos anos seguintes.

| Domínio | Disponível? | Restrição informada pela API | Hostinger vende? | 1º ano | Renovação/ano | Item do catálogo |
|---|---|---|---|---|---|---|
| brendasimeao.com.br | SIM | `requires_cpf_or_cnpj` | SIM | R$ 39,99 | R$ 64,99 | `hostingercombr-domain-combr-brl-1y` |
| brendasimeao.com | SIM | nenhuma | SIM | R$ 49,99 | R$ 94,99 | `hostingercombr-domain-com-brl-1y` |
| brendasimeao.odo.br | SIM | nenhuma informada (ver seção 0) | SIM | R$ 42,99 | R$ 42,99 | `hostingercombr-domain-odobr-brl-1y` |
| brendasimeao.med.br | SIM | nenhuma informada | SIM | R$ 42,99 | R$ 42,99 | `hostingercombr-domain-medbr-brl-1y` (não serve: ela é dentista) |
| drabrendasimeao.com.br | **NÃO** (registrado) | `requires_cpf_or_cnpj` | n/a | n/a | n/a | n/a |

Conferência cruzada no RDAP do Registro.br (29/10): `brendasimeao.com.br`, `brendasimeao.odo.br` e `brendasimeao.med.br` sem registro (404 = livre). `drabrendasimeao.com.br` registrado em 16/12/2025, expira em 16/12/2026, servidores DNS `ns1/ns2.dns-parking.com` (estacionamento padrão da Hostinger). **Não está na nossa conta Hostinger** (conferido na lista de domínios). O titular não aparece no RDAP; só a Dra. pode dizer se é dela.

**A Hostinger registra .com.br, .odo.br e .med.br?** Sim. Os três estão no catálogo de compra da conta, e a conta já tem domínios `.com.br` ativos registrados por ela. Não é preciso ir ao Registro.br. Se mesmo assim preferirmos o Registro.br (titular com conta própria lá, sem intermediário), os links de busca já preenchidos são:

- <https://registro.br/busca-dominio/?fqdn=brendasimeao.com.br>
- <https://registro.br/busca-dominio/?fqdn=brendasimeao.odo.br>

Preço no Registro.br: não consultado hoje (a referência anterior do repositório era cerca de R$ 40/ano para .com.br; conferir na hora).

## 2. Fluxo de compra pela API da Hostinger

Confirmado na especificação oficial, salvo onde marcado.

1. **Catálogo**: `GET /api/billing/v1/catalog?category=DOMAIN` devolve o `item_id` de preço (ex.: `hostingercombr-domain-combr-brl-1y`).
2. **Disponibilidade**: `POST /api/domains/v1/availability` com `domain` e `tlds`. Limite de 90 consultas/minuto.
3. **Perfil WHOIS do titular**: `POST /api/domains/v1/whois` com `tld`, `entity_type` (`individual` ou `organization`), `country` e `whois_details` (obrigatórios) e `tld_details` (opcional na especificação). A especificação **não lista os campos internos** de `whois_details` e `tld_details` (aparecem como objeto livre). Os nomes abaixo vêm dos perfis `.com.br` que já existem na nossa conta (lidos via `GET /api/domains/v1/whois`, sem expor dados).
4. **Pedido de compra**: `POST /api/domains/v1/portfolio` com `domain` e `item_id` (obrigatórios), `domain_contacts` (`owner_id`, `admin_id`, `billing_id`, `tech_id` = IDs de perfis WHOIS), `payment_method_id` (sem ele usa o cartão padrão da conta), `additional_details` (alguns TLDs exigem; a especificação não diz quais campos) e `coupons`.
   - Resposta `202` = pagamento ainda em processamento e domínio **não** registrado; depois é preciso concluir com `POST /api/domains/v1/portfolio/{domain}/setup` (sem nova cobrança).
   - Sem `domain_contacts`, a Hostinger usa o perfil WHOIS **padrão** daquele TLD. Por isso o pedido precisa apontar explicitamente para o perfil da Dra.
5. **Pagamento**: cartão cadastrado na conta. A conta tem um cartão padrão ativo; a API não cria cobrança sem pedido.
6. **Privacidade**: `PUT`/`DELETE /api/domains/v1/portfolio/{domain}/privacy-protection`. O registro via `setup` já ativa privacidade quando o TLD permite. **Para `.com.br` não é permitido**: nossos domínios `.com.br` atuais retornam `is_privacy_protection_allowed = false` (o Registro.br não oferece ocultação). Para `.com` é permitido.
7. **Depois**: `PUT /api/domains/v1/portfolio/{domain}/nameservers` para apontar à LP (fora do escopo agora).

Existe também `POST /api/billing/v1/orders` (pedido genérico), mas ele só cobra e não registra o domínio; para domínio o caminho certo é o item 4.

## 3. Campos do titular

| Campo | Nome na API (perfil `.com.br` existente) | Pessoa física | Pessoa jurídica | Status |
|---|---|---|---|---|
| Tipo | `entity_type` | `individual` | `organization` | confirmado na especificação |
| País | `country` / `country_code` | BR | BR | confirmado |
| Nome | `first_name`, `last_name` | nome completo | nome do responsável | confirmado nos perfis da conta |
| Razão social | `company_name` | vazio | razão social | confirmado nos perfis da conta |
| CPF | `tld_details.vat_person_br` | obrigatório | n/a | confirmado nos perfis da conta + restrição `requires_cpf_or_cnpj` da API |
| CNPJ | `tld_details.vat_company_br` | n/a | obrigatório | confirmado nos perfis da conta |
| Endereço | `address`, `city`, `state_br`, `zip_br` | completo com CEP | completo com CEP | confirmado nos perfis da conta |
| E-mail | `email` | obrigatório | obrigatório | confirmado nos perfis da conta |
| Telefone | `phone_cc` (55), `phone_number` | obrigatório | obrigatório | confirmado nos perfis da conta |
| Data de nascimento | `tld_details.birth_date` | aparece em 1 perfil `.com` | n/a | **não confirmado** se é exigido para `.com.br` |
| Comprovação CRO (`.odo.br`) ou CRM (`.med.br`) | não documentado | | | **não confirmado**: a API não tem campo para isso; regra do Registro.br, provavelmente validada depois do registro |

Para `.com.br` em nome de pessoa física, o Registro.br vincula o domínio ao CPF; o e-mail do titular passa a ser o contato oficial do domínio no Registro.br.

## 4. Quem paga e quem fica como titular

- **Conta que paga**: a conta Hostinger da Expoente (a mesma do token da API e onde já estão `expoente.marketing` e os domínios de outros clientes). Cobrança no cartão padrão dessa conta.
- **Titular sem acessar nossa conta**: sim. Criamos na nossa conta um perfil WHOIS `.com.br` em nome dela (CPF ou CNPJ dela) e apontamos `owner_id` para ele no pedido. Ela fica como titular legal no Registro.br e nunca precisa entrar na Hostinger. A conta já faz isso para outros clientes (há vários perfis `.com.br` de pessoa física cadastrados).
- **Se depois ela quiser o domínio na conta dela**: duas saídas documentadas.
  - Mover para uma conta Hostinger dela: `POST /api/domains/v1/move/outgoing/{domain}` com o e-mail da conta dela; ela aceita do lado dela.
  - Sair da Hostinger: pegar o código de autorização (`GET /api/domains/v1/portfolio/{domain}/auth-code`) e transferir. Para `.com.br`, como ela é a titular pelo CPF, também pode assumir direto no Registro.br com o login dela (**fluxo do Registro.br não verificado hoje**).
- Recomendo `admin_id` e `billing_id` também no perfil dela, e `tech_id` no perfil da Expoente, para que a gente consiga cuidar do DNS sem depender dela.

## 5. Mensagem para a Dra. (rascunho, não enviada)

> Oi, Dra. Brenda! Tudo bem?
>
> Vamos registrar o endereço do seu site, e ele precisa ficar no seu nome, para ser seu de verdade. Pode me mandar estes dados?
>
> 1. Vai ficar no seu nome (CPF) ou da clínica (CNPJ)?
> 2. Nome completo (ou razão social, se for CNPJ)
> 3. CPF ou CNPJ
> 4. Endereço completo com CEP
> 5. E-mail que você acessa sempre (é por ele que chegam os avisos do domínio)
> 6. Telefone com DDD
>
> E uma pergunta: o endereço **drabrendasimeao.com.br** já existe e está registrado por alguém. Foi você que registrou? Se foi, me avisa onde (qual site ou empresa) que a gente aproveita.
>
> Assim que você mandar, eu cuido do resto e te aviso.

## 6. Plano de compra para aprovação do Guilherme (não executado)

| Item | Proposta |
|---|---|
| Domínio | **brendasimeao.com.br** (casa com o @brendasimeao, é o mais fácil de falar e lembrar) |
| Opcional | `brendasimeao.com` para proteger o nome e redirecionar ao `.com.br` (só se quiser; renovação mais cara) |
| Não comprar | `.med.br` (ela é dentista). `.odo.br` só se quiserem reforçar a área; não é necessário |
| Onde | Hostinger, conta da Expoente, via API (`POST /api/domains/v1/portfolio`), item `hostingercombr-domain-combr-brl-1y` |
| Quem paga | Expoente, no cartão padrão da conta Hostinger (repassar à Dra. conforme contrato, se for o caso) |
| Titular | Dra. Brenda (CPF) ou a clínica (CNPJ), via perfil WHOIS `.com.br` criado com os dados dela |
| Contatos | owner, admin e billing = perfil dela; tech = perfil da Expoente |
| Privacidade | não disponível para `.com.br` (os dados do titular ficam no Registro.br, como em qualquer `.com.br`) |
| Falta dela | respostas da mensagem da seção 5 (tipo de titular, nome/razão social, CPF/CNPJ, endereço com CEP, e-mail, telefone) e se `drabrendasimeao.com.br` é dela |
| Falta do Guilherme | OK no domínio, OK no `.com` opcional e OK para a Expoente pagar |
| Depois da compra | apontar DNS para a LP quando ela for publicada (tarefa separada) |
| Atenção | se `drabrendasimeao.com.br` for dela, ele vence em 16/12/2026; decidir se renova e redireciona |

Ordem de execução quando aprovado: criar perfil WHOIS dela → checar disponibilidade de novo → pedido com `domain_contacts` apontando para o perfil dela → se vier `202`, concluir com `setup` → conferir em `GET /api/domains/v1/portfolio/brendasimeao.com.br`.

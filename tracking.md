# Tracking: Pixel + API de Conversões (EXP-27)

Conta de anúncios: `act_9695520683892802` (CA01 BRENDA SIMEÃO), Business Manager "Brenda Simeão" (`275891219773948`). Spec de eventos: `dossie-estrategico-funil.md`, seção 4.

## 1. O que já existe no Meta (consulta só leitura, nada foi criado)

Pixels ligados à conta (via `adspixels`):

| Pixel ID | Nome | Último disparo |
|---|---|---|
| `737211919420986` | Dra Branda Simeão | 2026-01-27 (único que já disparou) |
| `1001051722586234` | Pixel Brenda - Vendas | nunca |
| `1541452300510576` | Pixel Brenda Portfólio | nunca |
| `26245392818443469` | Pixel brendaaa | nunca |

Páginas ligadas à conta: "Brenda Simeão" (`236733703922417`, 16 seguidores) e três páginas alheias (Travassos Imóveis, Thumdra CRM, Vitor Guilherme), que não são dela.

**Recomendação:** usar o `737211919420986` (único com histórico de disparo, nome mais próximo da Dra.), sujeito ao OK do Guilherme. Os outros três são duplicatas sem uso; não apagar nada sem OK. Em Events Manager, conferir se o Pixel escolhido tem a conta de anúncios atribuída e o domínio da LP verificado. Em 2026 o Pixel é criado já como "conjunto de dados"; o ID é o mesmo.

**Nada será criado no Meta sem OK.** Se o Guilherme preferir um Pixel limpo, o que seria criado: 1 conjunto de dados "LP Facetas - Dra. Brenda" no BM `275891219773948`, atribuído à conta `act_9695520683892802`, mais 1 token de acesso de sistema para a CAPI. Domínio da LP a verificar no BM.

## 2. Instalação na LP (`lp/index.html`)

- `window.PIXEL_ID=""` e `window.CAPI_ENDPOINT=""`: preencher na publicação. Vazios = nada dispara (seguro).
- `track(nome, dados)` dispara Pixel e CAPI com o **mesmo `event_id`** (deduplicação).
- Eventos: `PageView`, `ViewContent` (15s ou 50% de scroll), `Contact` (clique em qualquer botão/FAB de WhatsApp, `content_name=cta_whatsapp`), `Lead` (envio do formulário, `content_name=form_triagem`).
- O `Lead` do browser **não leva mais queixa nem prazo** (dado de saúde fora do Meta).
- Atribuição: `utm_source/medium/campaign/content/term` e `fbclid` ficam em `sessionStorage`; `fbp` vem do cookie `_fbp`; `fbc` vem do cookie `_fbc` ou é montado como `fb.1.<ts>.<fbclid>`.
- Código curto `ref` (6 caracteres) gerado por sessão. Vai na mensagem do WhatsApp como `Ref: ABC123` e no payload da CAPI; o servidor guarda `ref` → atribuição, e o CRM recupera a origem quando a conversa começa. A mensagem não leva UTM, fbclid nem dado de saúde.
- **Ainda falta (fora desta tarefa):** banner de consentimento. Hoje o Pixel carregaria ao abrir a página; antes do go-live, só chamar `fbq('init')` após o aceite (LGPD, dossiê 4.1).

## 3. Desenho do endpoint CAPI

**Servidor:** serviço pequeno nosso (Node ou n8n), HTTPS, em subdomínio do domínio da LP ou próprio (ex.: `/capi`). Credenciais só em variáveis de ambiente; nunca no front, nunca em commit.

**Entrada 1, browser (`navigator.sendBeacon`, POST JSON):** `event_name`, `event_id`, `event_time`, `event_source_url`, `custom_data`, `ref`, `attribution` (utm/fbclid), `fbc`, `fbp`. O servidor acrescenta `client_ip_address` e `client_user_agent` dos headers da requisição. CORS restrito ao domínio da LP, limite de requisições por IP, whitelist de `event_name` (`PageView`, `ViewContent`, `Contact`, `Lead`).

**Entrada 2, CRM (webhook de mudança de estágio):** `Lead` qualificado e `Schedule`, com `event_id` gerado no CRM, `action_source=system_generated` (ou `chat` para mensagem de WhatsApp), `ref` para recuperar `fbc`/`fbp` guardados.

**Chamada à Meta:** `POST https://graph.facebook.com/<versão>/<PIXEL_ID>/events` com `access_token` do ambiente. Payload:

```json
{
  "data": [{
    "event_name": "Schedule",
    "event_time": 1790000000,
    "event_id": "crm-<id-agendamento>",
    "action_source": "system_generated",
    "event_source_url": "https://<dominio-da-lp>/",
    "user_data": {
      "ph": ["<sha256 do telefone E.164 sem +>"],
      "em": ["<sha256 do e-mail minúsculo, se houver>"],
      "fbc": "fb.1....", "fbp": "fb.1....",
      "client_ip_address": "...", "client_user_agent": "..."
    },
    "custom_data": { "content_name": "avaliacao_presencial" }
  }],
  "test_event_code": "<só em teste>"
}
```

**Regras:**
- **Hash:** SHA-256 em `ph` e `em` (telefone só dígitos com DDI 55, e-mail minúsculo sem espaços). `fbc`, `fbp`, IP e user agent **não** são hasheados.
- **Sem dado de saúde:** nenhum campo com queixa, diagnóstico, procedimento específico de cada paciente ou texto livre. Só categorias fixas de nosso lado (`content_name`).
- **Sem valor em reais:** não enviar `value` nem `currency`. `Purchase` fica desligado, a menos que a Dra. aprove registrar valor.
- **`Schedule`:** só quando a avaliação presencial é confirmada no CRM; `content_name=avaliacao_presencial`.
- **Idempotência:** chave `telefone + estágio` + `event_id` guardado; nunca reenviar `Schedule` duas vezes para o mesmo agendamento.
- **Resposta:** registrar `events_received` e `fbtrace_id`; retentar com backoff em erro 5xx.
- **Teste:** usar `test_event_code` do Events Manager e conferir deduplicação (evento do browser e do servidor com o mesmo `event_id` aparecem como um só).

## 4. Depende do Guilherme ou da Dra.

**Guilherme:**
1. OK para usar o Pixel `737211919420986` (ou OK para criar um novo).
2. Pedir à Dra. acesso de parceiro ao Business Manager `275891219773948` para a Expoente, com controle sobre o Pixel e a conta de anúncios (se ainda não tiver o nível necessário).
3. Definir onde o endpoint CAPI roda (host/subdomínio) e o domínio final da LP; verificar o domínio no BM.
4. Gerar o token de acesso de sistema para a CAPI (Events Manager, aba Configurações do conjunto de dados) e guardá-lo em variável de ambiente do servidor.

**Dra. Brenda:**
1. Aceitar o convite de parceiro no Business Manager (ou conceder o acesso pelo Configurações do negócio).
2. Se o token vier dela: enviar **somente por canal seguro** (gerenciador de senhas ou link com expiração), **nunca por WhatsApp**.
3. Decidir se aceita registrar valor de fechamento (`Purchase`); por padrão fica desligado.
4. Texto da política de privacidade (LGPD) e aceite do banner de cookies.

Regra: nenhum token ou chave entra neste repositório, em mensagens ou em logs.

# Setup de marketing — Dra Brenda Simeão (Expoente)
Base: `/root/projects/brenda-simeao/auditoria-dra-brenda.md` (preservada, intocada). Novas versões vão em arquivos novos (v2, v3...), sem sobrescrever.

- `lp/index.html` — Landing Page completa (abrir no navegador). Previews: `preview-desktop.png`, `preview-mobile.png`
- `instagram/antes-depois-legendas.html` — 9 posts reais, legenda ANTES/DEPOIS lado a lado (+ `legendas-antes-depois.md`, `antes-depois-preview.png`)
- `apresentacao-comercial/Proposta-Expoente-Dra-Brenda-v1.pdf` — deck de 13 slides (fonte: `deck.html`, gerador `build.py`)

## Pendências antes de publicar / enviar
- WhatsApp oficial: constante `WA` no final de `lp/index.html`
- CRO-GO, endereço/horários reais de atendimento (hoje placeholders `[...]`; clínica Oral Unic não confirmada)
- Autorização de imagem dos pacientes; confirmar "parcelamos" e número de sessões
- Pixel Meta / GA4 (comentário TRACKING no head da LP)
- Ticket médio real (deck usa R$ 4.000 hipotético) e taxas de conversão: tudo é ESTIMATIVA
- Imagens são recortes de screenshots (baixa resolução); trocar pelos originais

## v3 (14/10, feedback mobile)
- Deck agora é HTML responsivo mobile first: `apresentacao-comercial/proposta-v3.html` (gerador `build3.py`). PDF v3 NÃO publicado: o layout de impressão corta slides longos. v1/v2 ficam como histórico.
- LP: nova foto de capa `lp/assets/dra-brenda-hero-v2.jpg` (anterior preservada em `index-v1-hero-antigo.html`).
- Instagram: fontes maiores para leitura no celular.

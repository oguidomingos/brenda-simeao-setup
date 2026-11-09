# Criativos v3 da Dra. Brenda: layout editorial

Versão 09/11. Mesma identidade aprovada (creme, sálvia, marrom; Libre Caslon Text + Inter; ícone e CRO-GO 18788), com layout mais moderno. A v2 continua intacta em `../criativos-v2/`.

Regenerar: `python3 gerar.py` (todas) ou `python3 gerar.py a1-capa a5` (só algumas). Vídeo: `python3 gerar-videos.py`. Lado a lado: `python3 -I comparar.py`. PDF: `python3 -I revisao.py`.
O gerador avisa no terminal se algum texto encosta no rodapé ou passa da margem.

## O que mudou (v2 → v3)

- **Sistema editorial** (referências em `referencias-visuais.md`): cabeçalho com nome à esquerda e tema e número da peça à direita; gancho grande com uma palavra em itálico; apoio curto; cartão de chamada; selos discretos.
- **Uma cor dominante por anúncio:** 1 marrom, 2 sálvia, 3 creme.
- **Ganchos abrem com pergunta ou medo** (benchmark): a1 "Por que alguns sorrisos de resina parecem todos iguais?"; a3 "Já viu uma faceta ser esculpida à mão?"; a4 "Por que dente natural não é de uma cor só?"; a2 e a5 já eram pergunta.
- **Fecho trocado:** em vez de "Avaliação presencial, particular.", o cartão "Toque em Enviar mensagem e conte o que você quer mudar no seu sorriso." (orgânico: "Toque no link da bio…").
- **"Goiânia e região"** em toda capa e todo fecho.
- **Anúncio 5 com foto** (labios-3), não mais só texto.
- **Novos enquadramentos:** foto com anotações (a1-q2), círculo (a2-q2, p02-2, p05-2), arco (a3-q2, p09), numeral gigante "5 anos" (a3-q3), foto nos fechos (a1-q4, a2-q4).
- **Formatos:** cartões de anúncio em 1080x1920; capas 1 a 3 também em 1080x1350 (`a1-feed`, `a2-feed`, `a3-feed`); anúncios 4 e 5 em 1080x1350 e 1080x1920 (`-story`).
- **corte-2:** legenda única "Dente natural não é de uma cor só." do começo ao fim e cartão final novo com o convite (`videos/corte-2.mp4`, 10,4 s).

## Onde está

- `anuncios/`: a1 a a3 (capa, q2, q3, q4; 1080x1920), a1-feed a a3-feed, a4, a5 (1080x1350), a4-story, a5-story
- `alternativas/`: a1-capa-alt (batom), a4-alt (labios-2), a5-alt (d087), a3-q4-sem-foto
- `calendario/`: p01, p02-1..4, p03-1..5, p05-1..5, p09, p14 (1080x1350)
- `videos/`: corte-2.mp4 e capa
- `comparacao/`: v2 x v3 lado a lado, uma JPG por peça (34)
- `revisao-v3.pdf`: revisão curta

## Textos novos que precisam do ok da Dra.

Ela aprovou os textos da v2 em 29/10. Na v3 entraram frases novas, todas para aprovar antes de subir:
1. a1 capa: "Por que alguns sorrisos de resina parecem todos iguais?" (sugestão do benchmark)
2. a1 q2: "Por isso a cor é observada dente por dente, antes de começar." e as anotações "Translucidez nas bordas", "Tom mais quente perto da gengiva", "Textura e brilho" (vêm do texto aprovado do q2)
3. a1 q4: "Esculpidas à mão, para o seu rosto."
4. a3 capa: "Já viu uma faceta ser esculpida à mão?"; a3 q2: "Camada por camada, dente por dente."
5. a4: "Por que dente natural não é de uma cor só?" e "Translucidez, tom e textura, trabalhados à mão."
6. Convite: "Toque em Enviar mensagem e conte o que você quer mudar no seu sorriso."

## Pendências

- **Termo de imagem:** nenhum chegou. O selo "Caso real · imagem autorizada" só pode ir ao ar depois do termo assinado de cada paciente; sem termo, tirar o selo ou não usar a peça.
- **Antes e depois:** fora (regra interna), pendente de conferir com o CRO-GO.
- **Fotos que faltam (espaço marcado nas peças):**
  1. `calendario/p01`: retrato novo da Dra., vertical, luz de janela, fundo claro do consultório (ela recusou a foto atual em 03/11).
  2. `anuncios/a3-q4`: a Dra. na bancada, de perfil, esculpindo (mãos e rosto), luz lateral. Enquanto não houver, usar `alternativas/a3-q4-sem-foto`.
  3. Vídeos com a Dra. falando e escultura em boa resolução: ver `../roteiros-videos.md`.
- **Fotos usadas que já existiam:** dra-a1-sorriso, dra-a1-batom, dra-labios-1/2, labios-3, d090, d076, d077, d087, macro2, macro5, v6066, v6067b, camadas2, esculpida-1/2/3/4, mapeamento. Nenhuma foto nova, nenhum banco de imagem.
- Nada foi publicado, enviado ou subido no Drive.

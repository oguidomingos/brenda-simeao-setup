# Revisão da LP contra o checklist CFO / CRO-GO (EXP-30, 28/10/2026)

Referência: dossie-estrategico-funil.md, seção 1.3.

## Corrigido na LP
- "e todas têm solução" (queixas) -> "e a avaliação define o melhor caminho para cada uma" (promessa de resultado).
- "Um caminho simples, sem surpresas" -> "simples e transparente".
- "orientações para o resultado durar" -> "para cuidar do resultado" (garantia implícita de durabilidade).

## Varredura limpa
Sem preço, parcelamento, promoção, gratuidade, "especialista", "o melhor/único/garantido". A avaliação consta como particular e presencial.

## Precisa de decisão do Guilherme
1. Título do hero "o sorriso que você quer, com a naturalidade que você merece": tom de promessa leve. Sugestão: "um sorriso pensado para você, com naturalidade".
2. "Preparo mínimo, preservando o seu dente" e "Preservação do dente" (faixa): afirmação absoluta; o FAQ já diz "em geral". Sugestão: "Técnica conservadora".
3. "exclusivamente às facetas em resina" / "5 anos só facetas": a galeria mostra "troca de resinas". Confirmar que o texto é fiel.
4. Seção "Resultados reais" com antes e depois: exige TCLE específico de divulgação por caso (checklist 1.2). Confirmar que os dois casos têm TCLE antes de publicar.
5. Imagens "Facetas durante o procedimento" (atendimento.jpg) e "Detalhe técnico do preparo" (preparo.jpg): checklist proíbe procedimento em tecido biológico. Conferir se há campo aberto/sangue.
6. "Na rua do bar do Celsinho" no bloco de endereço: informal e referencia terceiro. Sugestão: remover.
7. Nome do local: autorizado "por enquanto". Se a Dra. mudar de endereço, trocar window.LOCAL_NOME e o endereço.
8. Avaliações Google: a seção não traz depoimentos inventados. Não oferecer brinde ou vantagem por avaliação (política do Google e CFO).

## schema.org
A LP não tinha bloco LocalBusiness/Dentist; não foi criado, conforme o pedido ("se já existir"). Se quiser, adicionar após o domínio definitivo.

## Avaliações (QR)
Preencher window.GOOGLE_REVIEWS_URL no topo de lp/index.html e rodar `tools/gen-qr.py <link>` (gera lp/assets/qr-avaliacoes.svg localmente). Enquanto a URL está vazia, a seção mostra "em breve" sem botão nem QR.

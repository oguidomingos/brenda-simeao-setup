#!/usr/bin/env python3
"""Gera lp/assets/qr-avaliacoes.svg localmente. Uso: tools/gen-qr.py <link-google-meu-negocio>
Depois preencher window.GOOGLE_REVIEWS_URL no topo de lp/index.html com o mesmo link."""
import sys, qrcode, qrcode.image.svg
if len(sys.argv) != 2 or not sys.argv[1].startswith("https://"):
    sys.exit("uso: gen-qr.py https://...")
img = qrcode.make(sys.argv[1], image_factory=qrcode.image.svg.SvgPathImage, box_size=10, border=2)
img.save("lp/assets/qr-avaliacoes.svg")
print("ok: lp/assets/qr-avaliacoes.svg")

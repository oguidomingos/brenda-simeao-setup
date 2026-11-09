# Capturas lado a lado v2 x v3 (uma PNG por peca) em comparacao/. Uso: python3 -I comparar.py
import os
from PIL import Image,ImageDraw,ImageFont
H=os.path.dirname(os.path.abspath(__file__))+'/'; V2=H+'../criativos-v2/'
F='/usr/share/fonts/truetype/dejavu/'
fb=ImageFont.truetype(F+'DejaVuSans-Bold.ttf',30); fr=ImageFont.truetype(F+'DejaVuSans.ttf',24)
PARES=[(f'anuncios/a{n}-{k}.png',f'anuncios/a{n}-{k}.png') for n in (1,2,3) for k in ('capa','q2','q3','q4')]+[
 ('anuncios/a4.png','anuncios/a4.png'),('anuncios/a5.png','anuncios/a5.png'),
 ('alternativas/a1-capa-alt.png','alternativas/a1-capa-alt.png'),('alternativas/a4-alt.png','alternativas/a4-alt.png'),
 ('calendario/p01.png','calendario/p01.png')]+[(f'calendario/p0{n}-{i}.png',)*2 for n,m in ((2,4),(3,5),(5,5)) for i in range(1,m+1)]+[
 ('calendario/p09.png',)*2,('calendario/p14.png',)*2,('videos/capa-corte-2.png','videos/capa-corte-2.png')]
def side(a,b,out,title):
    A=Image.open(V2+a).convert('RGB'); B=Image.open(H+b).convert('RGB'); th=900
    A=A.resize((int(A.width*th/A.height),th)); B=B.resize((int(B.width*th/B.height),th))
    W=A.width+B.width+3*40; s=Image.new('RGB',(W,th+130),(245,242,238)); d=ImageDraw.Draw(s)
    d.text((40,24),title,font=fb,fill=(40,30,25))
    d.text((40,78),'v2 (atual)',font=fr,fill=(120,110,100)); d.text((80+A.width,78),'v3 (novo)',font=fr,fill=(90,58,40))
    s.paste(A,(40,110)); s.paste(B,(80+A.width,110)); s.save(out,quality=88)
for a,b in PARES:
    if os.path.exists(V2+a) and os.path.exists(H+b):
        n=os.path.basename(b).replace('.png','')
        side(a,b,H+f'comparacao/{n}.jpg',n); print(n)

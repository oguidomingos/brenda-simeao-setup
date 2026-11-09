# Gera revisao-brenda.pdf e revisao-brenda-capa.png (folhas de contato: peça + pedido da Dra. + selo)
import os,textwrap
from PIL import Image,ImageDraw,ImageFont
Image.init()
H=os.path.dirname(os.path.abspath(__file__))+'/'
F='/usr/share/fonts/truetype/dejavu/'
fb=lambda s:ImageFont.truetype(F+'DejaVuSans-Bold.ttf',s)
fr=lambda s:ImageFont.truetype(F+'DejaVuSans.ttf',s)
fs=lambda s:ImageFont.truetype(F+'DejaVuSerif.ttf',s)
CREME,SALVIA,MARROM=(247,241,230),(138,154,123),(90,58,40)
OKC,ATC=(70,130,80),(200,110,30)
AP='“Aprovo os anúncios 1 a 5 como estão.” (29/10)'
NAO='Não divulgar: preços, promoções, nome de clínica, reação emocionada. (26/10)'
TERMO='“Todos assinam termo… só posto mediante aprovação do paciente.” (03/11). Termo ainda não chegou.'
P=[ # arquivo, título, pedido, selo, motivo
('anuncios/a1-capa.png','Anúncio 1 · capa','“No anúncio 1 poderia usar alguma dessas imagens.” (09/11)','AT','Foto dela aplicada. Escolher entre sorriso e batom. Termo pendente.'),
('anuncios/a1-q2.png','Anúncio 1 · q2',AP,'OK',''),('anuncios/a1-q3.png','Anúncio 1 · q3',AP,'OK',''),('anuncios/a1-q4.png','Anúncio 1 · q4',AP,'OK',''),
('anuncios/a2-capa.png','Anúncio 2 · capa',AP+' '+'Paciente sem rosto.','AT','Termo pendente.'),
('anuncios/a2-q2.png','Anúncio 2 · q2',AP,'OK',''),('anuncios/a2-q3.png','Anúncio 2 · q3',AP,'OK',''),('anuncios/a2-q4.png','Anúncio 2 · q4',AP,'OK',''),
('anuncios/a3-capa.png','Anúncio 3 · capa','“Essa foto é de preparo para porcelana… tenho fotos onde esculpi, dá para ver as camadas.” (03/11)','AT','Troca feita (resina em camadas). Ela gosta da foto antiga: decidir. Termo pendente.'),
('anuncios/a3-q2.png','Anúncio 3 · q2',AP,'OK',''),
('anuncios/a3-q3.png','Anúncio 3 · q3','“A frase 5 anos dedicados a resina confirmada.” (09/11)','OK',''),
('anuncios/a3-q4.png','Anúncio 3 · q4',AP,'OK',''),
('anuncios/a4.png','Anúncio 4 · feed','“Essa no anúncio 4.” (09/11)','AT','Qual das 3 fotos de lábios? Usei a 1. Termo pendente.'),
('anuncios/a5.png','Anúncio 5 · feed',AP,'OK',''),
('alternativas/a1-capa-alt.png','Alternativa · anúncio 1','“…alguma dessas imagens.” (09/11)','AT','Opção com a foto do batom.'),
('alternativas/a3-capa-alt.png','Alternativa · anúncio 3','“Gosto tanto dessa foto, ela ficou tão bonita.” (09/11)','AT','Foto de porcelana: não usar com a frase de resina.'),
('alternativas/a4-alt.png','Alternativa · anúncio 4','“Essa no anúncio 4.” (09/11)','AT','Opção com outra foto de lábios.'),
('calendario/p01.png','Post 01 · apresentação','“Fiquei muito feia nessa foto, vou procurar uma mais bonitinha.” (03/11)','AT','Foto igual à que ela recusou. Falta o retrato novo.'),
('calendario/p02-1.png','Post 02 · 1',TERMO,'AT','Termo pendente.'),('calendario/p02-2.png','Post 02 · 2',TERMO,'AT','Termo pendente.'),('calendario/p02-3.png','Post 02 · 3',TERMO,'AT','Termo pendente.'),
('calendario/p02-4.png','Post 02 · 4',NAO,'OK',''),
]+[(f'calendario/p03-{i}.png',f'Post 03 · {i}',NAO,'OK','') for i in range(1,6)]+[(f'calendario/p05-{i}.png',f'Post 05 · {i}',NAO,'OK','') for i in range(1,6)]+[
('calendario/p09.png','Post 09 · escultura','“Tenho fotos onde esculpi o dente e dá para ver as camadas.” (03/11)','AT','Foto de camadas aplicada. Termo pendente.'),
('calendario/p14.png','Post 14 · frase','Sem pedido dela. A frase está no calendário, sem aprovação por escrito.','AT','Guilherme decide manter ou trocar.')]
W,Hh=1800,1450; COLS=4; CW=W//COLS
def card(d,pg,x,y,item,th):
    f,t,pedido,sel,mot=item
    im=Image.open(H+f).convert('RGB'); im.thumbnail((CW-40,520))
    pg.paste(im,(x+20,y+20))
    cy=y+20+520+12
    d.text((x+20,cy),t,font=fb(19),fill=MARROM); cy+=30
    for ln in textwrap.wrap(pedido,40)[:4]:
        d.text((x+20,cy),ln,font=fr(15),fill=(70,60,55)); cy+=20
    c=OKC if sel=='OK' else ATC
    d.rounded_rectangle((x+20,y+20,x+20+(60 if sel=='OK' else 98),y+20+30),8,fill=c)
    d.text((x+28,y+25),'OK' if sel=='OK' else 'ATENÇÃO',font=fb(16),fill='white')
    if mot:
        for ln in textwrap.wrap(mot,42)[:3]: d.text((x+20,cy+4),ln,font=fr(14),fill=ATC); cy+=19
pages=[]
def new(title):
    pg=Image.new('RGB',(W,Hh),CREME); d=ImageDraw.Draw(pg); d.text((40,16),title,font=fs(26),fill=MARROM); return pg,d
CAP=[]
ok=sum(1 for p in P if p[3]=='OK'); at=len(P)-ok
# capa
pg,d=new('Revisão Dra. Brenda Simeão · 09/11')
d.rectangle((0,0,W,6),fill=SALVIA)
d.text((60,110),'Painel de revisão',font=fs(64),fill=MARROM)
d.text((60,200),f'{len(P)} peças: {ok} OK, {at} com ATENÇÃO. Cada peça aparece com o pedido da Dra. que ela atende.',font=fr(26),fill=(70,60,55))
dec=['O que depende do Guilherme:','1. Termo de imagem dos pacientes (todas as peças com foto).','2. Anúncio 1: sorriso lateral ou batom vermelho.','3. Anúncio 4: qual das 3 fotos de lábios.','4. Anúncio 3: manter a capa de resina em camadas (decisão dela sobre a foto antiga de porcelana).','5. P09 e P01: foto de camadas confirmada? Retrato novo?','6. P14: manter a frase "Eu faço como se fosse para mim".','Fotos da amiga e vídeos: guardados, não usados.']
y=300
for i,l in enumerate(dec): d.text((60,y),l,font=fb(26) if i==0 else fr(25),fill=MARROM); y+=44
# mini grade de capas
x=60;y=760
for item in [P[0],P[8],P[12],P[17]]:
    im=Image.open(H+item[0]).convert('RGB'); im.thumbnail((380,500)); pg.paste(im,(x,y)); x+=420
d.text((60,1380),'Pasta privada: Brenda Simeão / Criativos (só o Guilherme).',font=fr(20),fill=SALVIA)
pg.save(H+'revisao-brenda-capa.png'); pages.append(pg)
# folhas
secs=[('Anúncios',[p for p in P if p[0].startswith('anuncios')]),('Alternativas',[p for p in P if p[0].startswith('alternativas')]),('Calendário',[p for p in P if p[0].startswith('calendario')])]
for name,items in secs:
    per=COLS*2
    for s in range(0,len(items),per):
        pg,d=new(f'{name}'); 
        for i,it in enumerate(items[s:s+per]): card(d,pg,(i%COLS)*CW,60+(i//COLS)*690,it,None)
        pages.append(pg)
pages[0].save(H+'revisao-brenda.pdf',save_all=True,append_images=pages[1:],resolution=150)
print(len(pages),'paginas',ok,at)

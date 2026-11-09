# Criativos v3 da Dra. Brenda Simeao: layout editorial (cabecalho, gancho grande com italico, apoio curto, cartao de chamada, selos).
# Mesma identidade aprovada (creme, salvia, marrom; Libre Caslon Text + Inter; icone e CRO-GO 18788). Sem foto nova: so o que ja existe.
# Uso: python3 gerar.py   (requer o repo brenda-identidade para fontes, logo e fotos)
import sys,os,base64
sys.path.insert(0,'/root/projects/brenda-identidade/src')
from build_creatives import msvg,NOISE
from common import fontcss
from playwright.sync_api import sync_playwright
H=os.path.dirname(os.path.abspath(__file__))+'/'
C,S,B,SL,TX='#F7F1E6','#8A9A7B','#5A3A28','#B9C4AC','#4a3a30'
IMG=['/root/projects/brenda-identidade/src/img/',H+'../criativos-v2/fotos-dela/']
_cache={}
def img(n):
    if n not in _cache:
        p=next(d+n+'.jpg' for d in IMG if os.path.exists(d+n+'.jpg'))
        _cache[n]='data:image/jpeg;base64,'+base64.b64encode(open(p,'rb').read()).decode()
    return _cache[n]
T={'cream':dict(bg=C,ink=B,body=TX,acc=S,rule=S,mark=(S,S,B),card=B,cardt=C,arrow=S,pill=S),
   'sage': dict(bg=S,ink=C,body=C,acc=C,rule=C,mark=(C,C,C),card=C,cardt=B,arrow=S,pill=C),
   'brown':dict(bg=B,ink=C,body=C,acc=SL,rule=SL,mark=(C,C,C),card=C,cardt=B,arrow=S,pill=SL)}
CTA='Toque em <b>Enviar mensagem</b> e conte o que você quer mudar no seu sorriso.'
CTA_BIO='Toque no <b>link da bio</b> e conte o que você quer mudar no seu sorriso.'
FONTS=fontcss()
ARROW=lambda c:f'<svg width="40" height="40" viewBox="0 0 40 40"><path d="M8 20h22M21 10l10 10-10 10" fill="none" stroke="{c}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'
PIN=lambda c:f'<svg width="18" height="24" viewBox="0 0 18 24"><path d="M9 1C4.6 1 1 4.5 1 8.9 1 15 9 23 9 23s8-8 8-14.1C17 4.5 13.4 1 9 1z" fill="none" stroke="{c}" stroke-width="2"/><circle cx="9" cy="9" r="3" fill="{c}"/></svg>'

def pill(txt,col,bg='transparent',pin=False):
    return f'<span class="pill" style="color:{col};border-color:{col};background:{bg}">{PIN(col) if pin else "<i style=background:"+col+"></i>"}{txt}</span>'
def cta(t,text=CTA,fs=34):
    return f'<div class="cta" style="background:{t["card"]};color:{t["cardt"]};font-size:{fs}px"><span class="ar" style="background:{t["arrow"]}">{ARROW(C)}</span><span>{text}</span></div>'

def page(w,h,theme,inner,head=('',''),pager=None,foot=True,head_on_photo=False,wm=False):
    t=T[theme]; st=h>1500
    m=84; ht=230 if st else 64; fb=300 if st else 44
    hc=C if head_on_photo else t['acc']; hr=C if head_on_photo else t['rule']
    hd=f'''<div class="hd" style="top:{ht}px;color:{hc}"><div class="hrow"><span>DRA. BRENDA SIMEÃO</span><span>{head[1]}</span></div><div class="hl" style="background:{hr}"></div></div>''' if head!=None else ''
    pg=''
    if pager: pg=f'<div class="pg" style="bottom:{fb+110}px">'+''.join(f'<i style="background:{t["acc"]};opacity:{1 if k==pager[0] else .35}"></i>' for k in range(pager[1]))+'</div>'
    ft=f'''<div class="ft" style="bottom:{fb}px"><div class="fr" style="background:{t["rule"]}"></div><div class="fx" style="color:{t["acc"] if theme!="cream" else S}">{msvg(t["mark"],54)}<span>DRA. BRENDA SIMEÃO · CIRURGIÃ-DENTISTA · CRO-GO 18788</span></div></div>''' if foot else ''
    wmk=f'<div class="wm" style="right:-{int(w*.30)}px;bottom:{int(h*.2)}px">{msvg(t["mark"],int(w*1.1))}</div>' if wm else ''
    return f'''<html><head><meta charset="utf-8"><style>{FONTS}
*{{box-sizing:border-box;margin:0;padding:0}} body{{width:{w}px;height:{h}px;overflow:hidden}}
.c{{position:relative;width:{w}px;height:{h}px;overflow:hidden;background:url("{NOISE}"),{t['bg']};color:{t['ink']};font-family:'Libre Caslon Text'}}
.a{{position:absolute}} .ph{{position:absolute;background-size:cover;background-repeat:no-repeat}}
.hd{{position:absolute;left:{m}px;right:{m}px;font-family:Inter;font-weight:500;font-size:{22 if st else 20}px;letter-spacing:.22em;z-index:5}}
.hrow{{display:flex;justify-content:space-between}} .hl{{height:2px;margin-top:20px;opacity:.75}}
h1{{font-weight:400;line-height:1.06;letter-spacing:-.018em}} h1 em{{font-style:italic;letter-spacing:-.01em}}
.ey{{font-family:Inter;font-weight:500;letter-spacing:.24em;text-transform:uppercase}}
.bd{{font-family:Inter;font-weight:400;line-height:1.42}}
.pill{{display:inline-flex;align-items:center;gap:14px;padding:13px 26px 13px 22px;border:2px solid;border-radius:999px;font-family:Inter;font-weight:500;font-size:{22 if st else 20}px;letter-spacing:.16em;text-transform:uppercase;white-space:nowrap}}
.pill i{{width:10px;height:10px;border-radius:50%;display:inline-block}}
.cta{{display:flex;align-items:center;gap:30px;padding:34px 40px 34px 34px;border-radius:30px;font-family:Inter;line-height:1.38}} .cta b{{font-weight:500}}
.ar{{flex:none;width:84px;height:84px;border-radius:50%;display:flex;align-items:center;justify-content:center}}
.ft{{position:absolute;left:{m}px;right:{m}px;z-index:5}} .fr{{height:2px;opacity:.7;margin-bottom:22px}}
.fx{{display:flex;align-items:center;gap:20px;font-family:Inter;font-weight:500;font-size:{19 if st else 20}px;letter-spacing:{'.1em' if st else '.16em'}}}
.pg{{position:absolute;right:{m}px;display:flex;gap:10px;z-index:5}} .pg i{{width:14px;height:14px;border-radius:50%}}
.wm{{position:absolute;opacity:.09;pointer-events:none}}
.tag{{position:absolute;font-family:Inter;font-weight:500;font-size:{20 if st else 18}px;letter-spacing:.16em;text-transform:uppercase;color:{C};background:rgba(58,37,25,.55);backdrop-filter:blur(6px);padding:11px 20px;border-radius:999px;z-index:4}}
.hole{{position:absolute;border:3px dashed {S};border-radius:28px;background:repeating-linear-gradient(135deg,{SL}33 0 18px,transparent 18px 36px);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;font-family:Inter;color:{B};padding:60px}}
.hole b{{font-weight:500;font-size:26px;letter-spacing:.2em;color:{S};margin-bottom:22px}} .hole span{{font-size:30px;line-height:1.45;max-width:640px}}
</style></head><body><div class="c">{wmk}{inner}{hd}{pg}{ft}</div></body></html>'''

# ---------- layouts ----------
def cover(w,h,theme,photo,pos,ey,hook,fs,head,sub='',tag=True,pager=None,block_h=None,cta_on=False):
    """foto em cima sangrando, bloco de cor embaixo com gancho; selo Goiania sobre a costura"""
    t=T[theme]; st=h>1500
    ph_h=block_h or (860 if st else 700)
    pil=f'<div class="a" style="left:84px;top:{ph_h-32}px;z-index:4">{pill("Goiânia e região",t["ink"],t["bg"],pin=True)}</div>'
    tg=f'<div class="tag" style="right:84px;top:{(230 if st else 64)+70}px">Caso real · imagem autorizada</div>' if tag else ''
    sh=f'<div class="a" style="left:0;right:0;top:0;height:{360 if st else 260}px;background:linear-gradient(180deg,rgba(58,37,25,.55),rgba(58,37,25,0));z-index:2"></div>'
    subh=f'<div class="bd" style="font-size:{38 if st else 32}px;color:{t["body"]};margin-top:30px;max-width:860px">{sub}</div>' if sub else ''
    ctah=f'<div style="margin-top:40px">{cta(t,fs=30 if not st else 33)}</div>' if cta_on else ''
    inner=f'''<div class="ph" style="left:0;top:0;width:{w}px;height:{ph_h}px;background-image:url({img(photo)});background-position:{pos}"></div>{sh}{tg}{pil}
<div class="a" style="left:84px;right:84px;top:{ph_h+(78 if st else 64)}px">
<div class="ey" style="font-size:{28 if st else 24}px;color:{t['acc']};margin-bottom:{26 if st else 20}px">{ey}</div>
<h1 style="font-size:{fs}px;color:{t['ink']}">{hook}</h1>{subh}{ctah}</div>'''
    return page(w,h,theme,inner,head,pager,head_on_photo=True)

def annot(w,h,theme,photo,pos,title,fs,body,notes,head,pager=None,ph=(84,700,912,700),size='cover'):
    """foto emoldurada com anotacoes em fio (translucidez, tom, textura); notes=(px,py,lx,ly,texto) relativos a foto"""
    t=T[theme]; x,y,pw,phh=ph
    svg=f'<svg class="a" style="left:{x}px;top:{y}px;z-index:3" width="{pw}" height="{phh}">'
    labels=''
    for (px,py,lx,ly,txt) in notes:
        svg+=f'<line x1="{px}" y1="{py}" x2="{lx}" y2="{ly}" stroke="{C}" stroke-width="2.5"/><circle cx="{px}" cy="{py}" r="12" fill="none" stroke="{C}" stroke-width="3"/><circle cx="{px}" cy="{py}" r="4.5" fill="{C}"/>'
        labels+=f'<div class="a" style="left:{x+lx}px;top:{y+ly}px;transform:translate(-50%,-50%);z-index:4;font-family:Inter;font-weight:500;font-size:27px;color:{B};background:{C};padding:12px 22px;border-radius:999px;white-space:nowrap">{txt}</div>'
    svg+='</svg>'
    inner=f'''<div class="a" style="left:84px;right:84px;top:{330 if h>1500 else 150}px"><h1 style="font-size:{fs}px">{title}</h1></div>
<div class="ph" style="left:{x}px;top:{y}px;width:{pw}px;height:{phh}px;border-radius:30px;background-image:url({img(photo)});background-position:{pos};background-size:{size}"></div>{svg}{labels}
<div class="a" style="left:84px;right:84px;top:{y+phh+52}px"><div class="bd" style="font-size:{36 if h>1500 else 30}px;color:{t['body']}">{body}</div></div>'''
    return page(w,h,theme,inner,head,pager)

def circle(w,h,theme,photo,pos,ey,title,fs,body,head,pager=None,d=560):
    """titulo grande + foto em circulo encostada na borda direita"""
    t=T[theme]; st=h>1500
    cy=880 if st else 500
    inner=f'''<div class="a" style="left:84px;right:84px;top:{340 if st else 160}px">
<div class="ey" style="font-size:{28 if st else 24}px;color:{t['acc']};margin-bottom:26px">{ey}</div><h1 style="font-size:{fs}px">{title}</h1></div>
<div class="ph" style="right:-80px;top:{cy}px;width:{d}px;height:{d}px;border-radius:50%;background-image:url({img(photo)});background-position:{pos};box-shadow:0 0 0 14px {t['bg']},0 0 0 16px {t['rule']}"></div>
<div class="a" style="left:84px;width:{w-84-d+40}px;top:{cy+(110 if st else 70)}px"><div class="bd" style="font-size:{38 if st else 32}px;color:{t['body']}">{body}</div>
<div class="a" style="left:0;top:-40px;width:120px;height:3px;background:{t['acc']}"></div></div>'''
    return page(w,h,theme,inner,head,pager)

def framed(w,h,theme,photo,pos,ey,title,fs,body,head,pager=None,arch=False,top_photo=None,ph_h=None,chips=None,block=True):
    """foto emoldurada (arco ou cantos) com bloco de cor deslocado atras; texto abaixo"""
    t=T[theme]; st=h>1500
    y=top_photo or (340 if st else 150); pw=w-168; phh=ph_h or (860 if st else 600)
    rad=f'{pw//2}px {pw//2}px 30px 30px' if arch else '30px'
    blk=S if theme=='cream' else (C if theme=='sage' else S)
    back=f'<div class="a" style="left:{84+36}px;top:{y+36}px;width:{pw}px;height:{phh}px;border-radius:{rad};background:{blk};opacity:.55"></div>' if block else ''
    ch=''
    if chips: ch='<div style="display:flex;gap:14px;margin-top:34px">'+''.join(pill(c,t['acc']) for c in chips)+'</div>'
    inner=f'''{back}<div class="ph" style="left:84px;top:{y}px;width:{pw}px;height:{phh}px;border-radius:{rad};background-image:url({img(photo)});background-position:{pos}"></div>
<div class="a" style="left:84px;right:84px;top:{y+phh+(76 if st else 58)}px">
{f'<div class="ey" style="font-size:{28 if st else 24}px;color:{t["acc"]};margin-bottom:22px">{ey}</div>' if ey else ''}
<h1 style="font-size:{fs}px">{title}</h1>{f'<div class="bd" style="font-size:{36 if st else 30}px;color:{t["body"]};margin-top:26px">{body}</div>' if body else ''}{ch}</div>'''
    return page(w,h,theme,inner,head,pager)

def number(w,h,theme,big,unit,title,body,head,pager=None):
    """numeral gigante como protagonista"""
    t=T[theme]; st=h>1500
    inner=f'''<div class="a" style="left:70px;top:{330 if st else 120}px;font-size:{620 if st else 440}px;line-height:1;color:{t['ink']};letter-spacing:-.04em">{big}<span style="font-style:italic;font-size:{150 if st else 110}px;letter-spacing:0;margin-left:16px;color:{t['acc']}">{unit}</span></div>
<div class="a" style="left:84px;right:84px;top:{1010 if st else 640}px"><div style="width:120px;height:3px;background:{t['acc']};margin-bottom:44px"></div>
<h1 style="font-size:{96 if st else 78}px">{title}</h1><div class="bd" style="font-size:{38 if st else 32}px;color:{t['body']};margin-top:30px">{body}</div></div>'''
    return page(w,h,theme,inner,head,pager,wm=True)

def statement(w,h,theme,ey,title,fs,body='',head=('',''),pager=None,quote=False,band=None):
    """quadro de texto com faixa de cor no topo e indice grande (organizacao de post)"""
    t=T[theme]; st=h>1500
    bh=band or (0)
    q=f'<div class="a" style="left:66px;top:{300 if st else 110}px;font-size:{420 if st else 320}px;line-height:1;color:{t["acc"]};opacity:.55">“</div>' if quote else ''
    inner=f'''{q}<div class="a" style="left:84px;right:84px;top:0;bottom:{(300+160) if st else 170}px;display:flex;flex-direction:column;justify-content:center;padding-top:{330 if st else 120}px">
{f'<div class="ey" style="font-size:{28 if st else 24}px;color:{t["acc"]};margin-bottom:30px">{ey}</div>' if ey else ''}
<h1 style="font-size:{fs}px">{title}</h1>{f'<div style="width:120px;height:3px;background:{t["acc"]};margin:44px 0 36px"></div><div class="bd" style="font-size:{38 if st else 32}px;color:{t["body"]}">{body}</div>' if body else ''}</div>'''
    return page(w,h,theme,inner,head,pager,wm=True)

def closing(w,h,theme,ey,title,fs,head,pager=None,text=CTA,photo=None,pos='50% 50%',hole_need=None):
    """cartao final: frase + cartao de chamada + selo Goiania"""
    t=T[theme]; st=h>1500
    thumb=f'<div class="ph" style="left:84px;top:{330 if st else 130}px;width:{w-168}px;height:{460 if st else 300}px;border-radius:30px;background-image:url({img(photo)});background-position:{pos}"></div>' if photo else ''
    if hole_need:
        thumb=f'<div class="hole" style="left:84px;top:{330 if st else 130}px;width:{w-168}px;height:{460 if st else 300}px;padding:40px"><b>ESPAÇO PARA FOTO</b><span>{hole_need}</span></div>'; photo='x'
    top=(330+460+76 if photo else 0) if st else (130+300+56 if photo else 0)
    inner=f'''{thumb}<div class="a" style="left:84px;right:84px;{'top:'+str(top)+'px' if photo else 'top:0;bottom:'+str(460 if st else 170)+'px;display:flex;flex-direction:column;justify-content:center;padding-top:'+str(300 if st else 110)+'px'}">
{f'<div class="ey" style="font-size:{28 if st else 24}px;color:{t["acc"]};margin-bottom:26px">{ey}</div>' if ey else ''}
<h1 style="font-size:{fs}px">{title}</h1>
<div style="margin-top:{56 if st else 40}px">{cta(t,text,fs=36 if st else 31)}</div>
<div style="margin-top:34px">{pill("Atendimento em Goiânia e região",t['pill'],pin=True)}</div></div>'''
    return page(w,h,theme,inner,head,pager,wm=not photo)

def hole(w,h,theme,ey,title,fs,need,head,pager=None,body=''):
    """espaco marcado para foto que ainda precisa ser feita"""
    t=T[theme]; st=h>1500; y=340 if st else 150; hh=860 if st else 640
    inner=f'''<div class="hole" style="left:84px;top:{y}px;width:{w-168}px;height:{hh}px"><b>ESPAÇO PARA FOTO</b><span>{need}</span></div>
<div class="a" style="left:84px;right:84px;top:{y+hh+(76 if st else 54)}px">
<div class="ey" style="font-size:{28 if st else 24}px;color:{t['acc']};margin-bottom:22px">{ey}</div><h1 style="font-size:{fs}px">{title}</h1>
{f'<div class="bd" style="font-size:{36 if st else 30}px;color:{t["body"]};margin-top:22px">{body}</div>' if body else ''}</div>'''
    return page(w,h,theme,inner,head,pager)

# ---------- pecas ----------
SW,SH,FW,FH=1080,1920,1080,1350
J=[]  # (subpasta, nome, w, h, html)
def add(sub,name,w,h,html): J.append((sub,name,w,h,html))
A='anuncios'
# Anuncio 1 . Naturalidade (marrom dominante)
add(A,'a1-capa',SW,SH,cover(SW,SH,'brown','dra-a1-sorriso','50% 45%','Naturalidade','Por que alguns sorrisos de resina parecem <em>todos iguais?</em>',112,('', 'NATURALIDADE · 01/04')))
add(A,'a1-q2',SW,SH,annot(SW,SH,'cream','dra-labios-1','50% 50%','Dente natural não é de <em>uma cor só.</em>',104,'Por isso a cor é observada dente por dente, antes de começar.',
    [(456,372,300,620,'Translucidez nas bordas'),(340,250,250,80,'Tom mais quente perto da gengiva'),(600,300,700,560,'Textura e brilho')],('', 'NATURALIDADE · 02/04'),ph=(84,640,912,720),size='170%'))
add(A,'a1-q3',SW,SH,framed(SW,SH,'sage','camadas2','50% 50%','Escultura à mão','Na escultura à mão, a cor é trabalhada <em>em camadas.</em>',88,'Pensando no seu rosto e no seu sorriso.',('', 'NATURALIDADE · 03/04'),ph_h=640))
add(A,'a1-q4',SW,SH,closing(SW,SH,'brown','Facetas em resina','Esculpidas à mão, <em>para o seu rosto.</em>',96,('', 'NATURALIDADE · 04/04'),photo='macro5',pos='50% 45%'))
# Anuncio 2 . Preservacao (salvia dominante)
add(A,'a2-capa',SW,SH,cover(SW,SH,'sage','d090','45% 50%','A dúvida mais comum','Faceta <em>estraga</em> o dente?',132,('', 'PRESERVAÇÃO · 01/04')))
add(A,'a2-q2',SW,SH,circle(SW,SH,'cream','v6067b','50% 40%','Preservação','A proposta é ser o mais <em>conservadora</em> possível.',108,'Com mínimo ou nenhum desgaste, conforme o caso.',('', 'PRESERVAÇÃO · 02/04')))
add(A,'a2-q3',SW,SH,framed(SW,SH,'sage','mapeamento','50% 55%','Planejamento','Cada boca pede uma <em>decisão diferente.</em>',92,'Só na avaliação a Dra. confirma o que é indicado para você.',('', 'PRESERVAÇÃO · 03/04'),ph_h=620))
add(A,'a2-q4',SW,SH,closing(SW,SH,'brown','Avaliação presencial','Uma conversa sobre <em>preservar</em> o seu dente.',96,('', 'PRESERVAÇÃO · 04/04'),photo='v6066',pos='50% 55%'))
# Anuncio 3 . Escultura (creme dominante)
add(A,'a3-capa',SW,SH,cover(SW,SH,'cream','esculpida-3','50% 50%','Escultura à mão','Já viu uma faceta ser <em>esculpida à mão?</em>',116,('', 'ESCULTURA · 01/04')))
add(A,'a3-q2',SW,SH,framed(SW,SH,'cream','esculpida-1','50% 50%','','Camada por camada, <em>dente por dente.</em>',100,'',('', 'ESCULTURA · 02/04'),arch=True,ph_h=680,chips=['Cor','Forma','Textura']))
add(A,'a3-q3',SW,SH,number(SW,SH,'brown','5','anos','dedicados a facetas <em>em resina.</em>','Com planejamento individual para o seu rosto.',('', 'ESCULTURA · 03/04')))
add(A,'a3-q4',SW,SH,closing(SW,SH,'sage','Escultura em resina','Feita pela <em>própria Dra.</em>',112,('', 'ESCULTURA · 04/04'),hole_need='A Dra. na bancada, de perfil, esculpindo uma faceta (mãos e rosto), luz lateral.'))
add('alternativas','a3-q4-sem-foto',SW,SH,closing(SW,SH,'sage','Escultura em resina','Feita pela <em>própria Dra.</em>',120,('', 'ESCULTURA · 04/04')))
# Anuncio 4 . feed + story
for w,h,sfx in [(FW,FH,''),(SW,SH,'-story')]:
    st=h>1500
    add(A,f'a4{sfx}',w,h,cover(w,h,'cream','dra-labios-1','50% 50%','Naturalidade','Por que dente natural <em>não é de uma cor só?</em>',112 if st else 84,('', 'FACETAS EM RESINA'),sub='Translucidez, tom e textura, trabalhados à mão.',cta_on=True,block_h=680 if st else 600))
    add(A,f'a5{sfx}',w,h,cover(w,h,'brown','labios-3','50% 50%','Naturalidade','Medo de ficar com cara de <em>dente de chiclete?</em>',104 if st else 88,('', 'FACETAS EM RESINA'),sub='Cor, formato e textura pensados para o seu rosto.',cta_on=True,block_h=640 if st else 560))
# capas 1 a 3 tambem no feed 4:5
add(A,'a1-feed',FW,FH,cover(FW,FH,'brown','dra-a1-sorriso','50% 40%','Naturalidade','Por que alguns sorrisos de resina parecem <em>todos iguais?</em>',88,('', 'NATURALIDADE'),cta_on=True,block_h=560))
add(A,'a2-feed',FW,FH,cover(FW,FH,'sage','d090','45% 50%','A dúvida mais comum','Faceta <em>estraga</em> o dente?',104,('', 'PRESERVAÇÃO'),cta_on=True,block_h=640))
add(A,'a3-feed',FW,FH,cover(FW,FH,'cream','esculpida-3','50% 50%','Escultura à mão','Já viu uma faceta ser <em>esculpida à mão?</em>',92,('', 'ESCULTURA'),cta_on=True,block_h=560))
# variacoes de foto (Guilherme escolhe)
add('alternativas','a1-capa-alt',SW,SH,cover(SW,SH,'brown','dra-a1-batom','50% 50%','Naturalidade','Por que alguns sorrisos de resina parecem <em>todos iguais?</em>',112,('', 'NATURALIDADE · 01/04')))
add('alternativas','a4-alt',FW,FH,cover(FW,FH,'cream','dra-labios-2','50% 50%','Naturalidade','Por que dente natural <em>não é de uma cor só?</em>',84,('', 'FACETAS EM RESINA'),sub='Translucidez, tom e textura, trabalhados à mão.',cta_on=True,block_h=600))
add('alternativas','a5-alt',FW,FH,cover(FW,FH,'brown','d087','50% 50%','Naturalidade','Medo de ficar com cara de <em>dente de chiclete?</em>',88,('', 'FACETAS EM RESINA'),sub='Cor, formato e textura pensados para o seu rosto.',cta_on=True,block_h=560))
# ---------- calendario (feed 1080x1350) ----------
K='calendario'
add(K,'p01',FW,FH,hole(FW,FH,'cream','Cirurgiã-dentista · CRO-GO 18788','Oi, eu sou a <em>Dra. Brenda Simeão.</em>',76,'Retrato novo da Dra., vertical, luz de janela, fundo claro do consultório, sorriso leve. (A foto atual ela recusou em 03/11.)',('', 'APRESENTAÇÃO')))
p2=[cover(FW,FH,'cream','d076','50% 50%','Naturalidade','Dente natural não é de <em>uma cor só.</em>',88,('', 'NATURALIDADE'),pager=(0,4),block_h=720),
    circle(FW,FH,'sage','d077','50% 40%','Naturalidade','Translucidez nas pontas, <em>cor mais quente</em> perto da gengiva.',84,'',('', 'NATURALIDADE'),pager=(1,4),d=600),
    framed(FW,FH,'cream','v6067b','50% 50%','Escultura','Textura e brilho vêm da escultura <em>camada por camada.</em>',62,'',('', 'NATURALIDADE'),pager=(2,4),ph_h=640),
    closing(FW,FH,'brown','','Cada sorriso é planejado para <em>um rosto.</em>',80,('', 'NATURALIDADE'),pager=(3,4),text=CTA_BIO)]
for i,x in enumerate(p2): add(K,f'p02-{i+1}',FW,FH,x)
p3=[cover(FW,FH,'sage','d087','50% 50%','Você não está sozinha(o)','Medo de ficar com <em>dente de chiclete?</em>',92,('', 'NATURALIDADE'),pager=(0,5),tag=True,block_h=700),
    statement(FW,FH,'cream','De onde vem essa preocupação','Dentes muito brancos, <em>todos iguais.</em>',100,head=('', 'NATURALIDADE'),pager=(1,5)),
    framed(FW,FH,'cream','esculpida-2','50% 50%','O que muda na escultura à mão','Cor, formato e textura pensados para <em>o seu rosto.</em>',66,'',('', 'NATURALIDADE'),pager=(2,5),ph_h=620),
    statement(FW,FH,'sage','Como se começa','Avaliação presencial, para <em>olhar o seu caso.</em>',96,head=('', 'NATURALIDADE'),pager=(3,5)),
    closing(FW,FH,'brown','','Cada sorriso <em>é um.</em>',110,('', 'NATURALIDADE'),pager=(4,5),text=CTA_BIO)]
for i,x in enumerate(p3): add(K,f'p03-{i+1}',FW,FH,x)
p5=[cover(FW,FH,'brown','macro2','50% 50%','A dúvida mais comum','Faceta <em>estraga</em> o dente?',104,('', 'PRESERVAÇÃO'),pager=(0,5),block_h=720),
    circle(FW,FH,'cream','v6066','50% 45%','Preservação','A proposta é ser o mais <em>conservadora</em> possível.',92,'',('', 'PRESERVAÇÃO'),pager=(1,5),d=600),
    statement(FW,FH,'sage','','Mínimo ou <em>nenhum</em> desgaste, conforme o caso.',100,head=('', 'PRESERVAÇÃO'),pager=(2,5)),
    framed(FW,FH,'cream','mapeamento','50% 55%','Planejamento','Cada boca pede uma <em>decisão diferente.</em>',70,'Só na avaliação isso é confirmado.',('', 'PRESERVAÇÃO'),pager=(3,5),ph_h=560),
    closing(FW,FH,'brown','Avaliação presencial','Uma conversa sobre <em>preservar</em> o seu dente.',84,('', 'PRESERVAÇÃO'),pager=(4,5),text=CTA_BIO)]
for i,x in enumerate(p5): add(K,f'p05-{i+1}',FW,FH,x)
add(K,'p09',FW,FH,framed(FW,FH,'cream','esculpida-4','50% 50%','Escultura em resina','Esculpido à mão, <em>dente por dente.</em>',76,'',('', 'ESCULTURA'),arch=True,ph_h=740))
add(K,'p14',FW,FH,statement(FW,FH,'sage','Dra. Brenda Simeão','Eu faço como se fosse <em>para mim.</em>”',104,head=('', 'BASTIDOR'),quote=True))

if __name__=='__main__':
    only=sys.argv[1:]
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=b.new_page(viewport={'width':1080,'height':1920})
        for sub,name,w,h,html in J:
            if only and name not in only: continue
            os.makedirs(H+sub,exist_ok=True)
            pg.set_viewport_size({'width':w,'height':h}); pg.set_content(html); pg.wait_for_timeout(250)
            pg.screenshot(path=f'{H}{sub}/{name}.png')
            r=pg.evaluate('''()=>{const f=document.querySelector('.ft');const ft=f?f.getBoundingClientRect().top:1e9;let m=0,x=0;
              document.querySelectorAll('h1,.bd,.cta,.pill,.hole').forEach(e=>{const b=e.getBoundingClientRect();if(e.closest('.ft'))return;m=Math.max(m,b.bottom);x=Math.max(x,b.right)});
              return [Math.round(m),Math.round(ft),Math.round(x)]}''')
            warn=' <<< SOBREPOE RODAPE' if r[0]>r[1]-20 else ''
            warn+=' <<< PASSA DA MARGEM' if r[2]>w-60 else ''
            print(sub,name,r,warn)
        b.close()

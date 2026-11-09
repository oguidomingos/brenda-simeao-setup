# PDF curto de revisao dos criativos v3 (layout de documento da Expoente: fundo escuro, Inter 200, acento roxo). Uso: python3 -I revisao.py
import os,base64,io
from PIL import Image
from playwright.sync_api import sync_playwright
H=os.path.dirname(os.path.abspath(__file__))+'/'; V2=H+'../criativos-v2/'
FD='/root/projects/brenda-identidade/fonts/node_modules/@fontsource/inter/files/'
def ff(w): return f"@font-face{{font-family:Inter;font-weight:{w};src:url(data:font/woff2;base64,{base64.b64encode(open(f'{FD}inter-latin-{w}-normal.woff2','rb').read()).decode()})}}"
def im(p,h=900):
    i=Image.open(p).convert('RGB'); i.thumbnail((2000,h)); b=io.BytesIO(); i.save(b,'JPEG',quality=82)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
def fig(p,h,cap='',v2=False):
    return f'<figure><img src="{im(p,h*2)}" style="height:{h}px"><figcaption class="{"o" if v2 else ""}">{cap}</figcaption></figure>'
W,HH=1080,1500
CSS=ff(200)+ff(300)+ff(400)+ff(500)+f'''*{{margin:0;padding:0;box-sizing:border-box}}
@page{{size:{W}px {HH}px;margin:0}} body{{background:#050208;color:#fff;font-family:Inter}}
.pg{{width:{W}px;height:{HH}px;padding:72px 64px;position:relative;overflow:hidden;page-break-after:always;
 background:radial-gradient(900px 600px at 85% -10%,rgba(123,44,191,.35),transparent 60%),radial-gradient(700px 500px at -10% 110%,rgba(139,92,246,.18),transparent 60%),#050208}}
.k{{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:#C084FC;display:flex;align-items:center;gap:10px;margin-bottom:22px}}
.k:before{{content:"";width:6px;height:6px;border-radius:50%;background:#C084FC;box-shadow:0 0 10px #A855F7}}
h1{{font-weight:200;font-size:76px;line-height:1.02;letter-spacing:-.045em}} h2{{font-weight:200;font-size:46px;line-height:1.04;letter-spacing:-.045em;margin-bottom:12px}}
.g{{color:#C084FC}}
p,li{{font-weight:300;font-size:19px;line-height:1.6;color:#a5a1ad}} li{{margin-left:22px;margin-bottom:6px}} b{{color:#fff;font-weight:500}}
.card{{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.10);border-radius:28px;padding:30px 34px;margin-top:26px}}
.row{{display:flex;gap:18px;align-items:flex-end;flex-wrap:wrap;margin-top:22px}}
figure img{{display:block;border-radius:12px;border:1px solid rgba(255,255,255,.10)}} figcaption{{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#C084FC;margin-top:10px}}
figcaption.o{{color:#75717e}} .ft{{position:absolute;left:64px;right:64px;bottom:40px;display:flex;justify-content:space-between;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#75717e}}
.vs{{font-weight:200;font-size:40px;color:#75717e;align-self:center}}'''
pages=[]
def page(body,n): pages.append(f'<section class="pg">{body}<div class="ft"><span>Expoente · revisão interna · não enviar à cliente sem aprovação</span><span>{n}</span></div></section>')
A=H+'anuncios/'
page(f'''<div class="k">Dra. Brenda Simeão · criativos v3 · 09/11/2026</div>
<h1>Layouts novos:<br><span class="g">mesma marca, mais destaque.</span></h1>
<div class="card"><p><b>O que mudou.</b></p><ul>
<li>Sistema editorial: cabeçalho com tema e número, gancho grande com itálico, apoio curto, cartão de chamada, selos discretos.</li>
<li>Ganchos abrem com pergunta ou medo; fecho virou convite: <b>"Toque em Enviar mensagem e conte o que você quer mudar no seu sorriso."</b></li>
<li>"Goiânia e região" em toda capa e fecho. Anúncio 5 com foto. Uma cor dominante por anúncio.</li>
<li>Formatos 1080x1920 e 1080x1350 para os 5 anúncios; calendário refeito; corte-2 com legenda única.</li></ul></div>
<div class="row" style="margin-top:34px">{fig(A+'a1-capa.png',470,'a1 capa')}{fig(A+'a2-capa.png',470,'a2 capa')}{fig(A+'a3-capa.png',470,'a3 capa')}</div>''',1)
for n,nome in [(1,'Anúncio 1 · Naturalidade'),(2,'Anúncio 2 · Preservação'),(3,'Anúncio 3 · Escultura')]:
    page(f'''<div class="k">{nome}</div><h2>v2 <span style="color:#75717e">×</span> <span class="g">v3</span></h2>
<div class="row">{fig(V2+f'anuncios/a{n}-capa.png',480,'v2 capa',True)}<span class="vs">→</span>{fig(A+f'a{n}-capa.png',480,'v3 capa')}{fig(A+f'a{n}-feed.png',384,'v3 feed 4:5')}</div>
<div class="row">{''.join(fig(A+f'a{n}-{k}.png',460,'v3 '+k) for k in ('q2','q3','q4'))}</div>''',n+1)
page(f'''<div class="k">Anúncios 4 e 5 · feed e story</div><h2>O 5 deixou de ser <span class="g">só texto.</span></h2>
<div class="row">{fig(V2+'anuncios/a4.png',420,'v2 a4',True)}{fig(A+'a4.png',420,'v3 a4')}{fig(A+'a4-story.png',420,'v3 a4 story')}</div>
<div class="row">{fig(V2+'anuncios/a5.png',420,'v2 a5',True)}{fig(A+'a5.png',420,'v3 a5')}{fig(A+'a5-story.png',420,'v3 a5 story')}</div>''',5)
K=H+'calendario/'
cal=['p01']+[f'p02-{i}' for i in range(1,5)]+[f'p03-{i}' for i in range(1,6)]+[f'p05-{i}' for i in range(1,6)]+['p09','p14']
page(f'''<div class="k">Calendário · 17 peças 1080x1350</div><h2>Mesmo sistema <span class="g">no orgânico.</span></h2>
<div class="row" style="gap:14px">{''.join(fig(K+c+'.png',222,c) for c in cal)}</div>''',6)
import subprocess
fr=[]
for t in (1.5,9.5):
    o=f'/tmp/bv3/rv{t}.png'; subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',H+'videos/corte-2.mp4','-frames:v','1',o],check=True); fr.append(o)
page(f'''<div class="k">Vídeo e pendências</div><h2>corte-2: <span class="g">uma frase só.</span></h2>
<div class="row">{fig(V2+'videos/capa-corte-2.png',380,'v2 corte-2',True)}{fig(fr[0],380,'v3 legenda')}{fig(fr[1],380,'v3 cartão final')}{fig(K+'p01.png',300,'espaço marcado')}</div>
<div class="card"><p><b>Antes de subir</b></p><ul>
<li><b>Textos novos</b> (ganchos e convite) precisam do ok da Dra.: lista em criativos-v3/LEIA-ME.md.</li>
<li><b>Termo de imagem</b>: nenhum chegou. Sem termo, tirar o selo "Caso real · imagem autorizada" ou não usar a peça.</li>
<li><b>Fotos que faltam</b>: retrato novo da Dra. (p01) e a Dra. na bancada esculpindo (a3 q4; até lá, usar a versão sem foto).</li>
<li><b>Vídeos para gravar</b>: 3 roteiros em roteiros-videos.md (medo de dente de chiclete, desgaste, escultura em camadas com revelação no espelho).</li>
<li>Antes e depois segue fora até conferir com o CRO-GO. Nada foi publicado nem enviado.</li></ul></div>''',7)
html=f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox']); pg=b.new_page(viewport={'width':W,'height':HH})
    pg.set_content(html); pg.wait_for_timeout(800); pg.pdf(path=H+'revisao-v3.pdf',width=f'{W}px',height=f'{HH}px',print_background=True); b.close()
print('ok',os.path.getsize(H+'revisao-v3.pdf')//1024,'KB')

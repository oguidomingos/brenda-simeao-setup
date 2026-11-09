# Gera os videos 9:16 (1080x1920) da Dra. Brenda a partir do clipe que ela mandou. Padrao aprovado: creme, salvia, marrom.
# Overlays (legenda e cartao final) em PNG transparente via Chrome; composicao com ffmpeg. Uso: python3 gerar-videos.py
import sys,os,subprocess
sys.path.insert(0,'/root/projects/brenda-identidade/src')
from build_creatives import msvg,TH,NOISE,fontcss
from playwright.sync_api import sync_playwright
H=os.path.dirname(os.path.abspath(__file__))+'/'
SRC=H+'fotos-dela/video-feito-a-mao.mp4'
T=TH['brown']; TMP='/tmp/bv/ov/'; os.makedirs(TMP,exist_ok=True)
CSS=fontcss()+"*{box-sizing:border-box;margin:0;padding:0}body{width:1080px;height:1920px;background:transparent}"
def cap_html(ey,ti,fs=84):
    return f'''<html><head><meta charset="utf-8"><style>{CSS}
.g{{position:absolute;left:0;right:0;top:0;height:900px;background:linear-gradient(180deg,rgba(70,44,30,.92) 0%,rgba(90,58,40,.72) 45%,rgba(90,58,40,0) 100%)}}
.tx{{position:absolute;left:94px;right:94px;top:250px;font-family:'Libre Caslon Text';color:#F7F1E6}}
.ey{{font-family:Inter;font-weight:500;font-size:30px;letter-spacing:.24em;text-transform:uppercase;color:#B9C4AC;margin-bottom:30px}}
h1{{font-weight:400;font-size:{fs}px;line-height:1.1;letter-spacing:-.01em}}</style></head><body>
<div class="g"></div><div class="tx"><div class="ey">{ey}</div><h1>{ti}</h1></div></body></html>'''
def end_html():
    return f'''<html><head><meta charset="utf-8"><style>{CSS}
body{{background:url("{NOISE}"),#5A3A28}}
.c{{position:absolute;left:94px;right:94px;top:0;bottom:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#F7F1E6}}
.n{{font-family:'Libre Caslon Text';font-size:76px;line-height:1.1;margin-top:56px}}
.s{{font-family:Inter;font-weight:500;font-size:28px;letter-spacing:.2em;text-transform:uppercase;color:#B9C4AC;margin-top:30px}}
.r{{width:120px;height:2px;background:#B9C4AC;opacity:.7;margin:54px 0}}
.k{{font-family:Inter;font-size:34px;line-height:1.5;color:#F7F1E6;opacity:.92}}</style></head><body>
<div class="c">{msvg(T['m'],300)}<div class="n">Dra. Brenda Simeão</div><div class="s">Cirurgiã-dentista · CRO-GO 18788</div><div class="r"></div><div class="k">Avaliação presencial, particular.</div></div></body></html>'''
VIDS={ # nome: (ini, fim, [(t0,t1,eyebrow,titulo,fs)], onde usar)
 'reels-mao':(0,16.05,[(0.3,8,'Escultura à mão','Tudo feito à mão.',104),(8,15.8,'Escultura à mão','Cada detalhe, dente por dente.',92)]),
 'corte-1':(0,8,[(0.3,4.2,'Escultura à mão','Cada faceta, esculpida à mão.',92),(4.2,7.8,'Escultura em resina','São 5 anos dedicados a facetas em resina.',84)]),
 'corte-2':(8,16.05,[(0.3,4.2,'Naturalidade','Dente natural não é de uma cor só.',92),(4.2,7.8,'Naturalidade','Na escultura à mão, a cor é trabalhada em camadas.',80)]),
 'corte-3':(3,10,[(0.3,3.4,'Escultura à mão','Cada faceta, esculpida à mão, dente por dente.',84),(3.4,6.7,'Escultura em resina','São 5 anos dedicados a facetas em resina.',84)]),
}
END=2.6; XF=0.5
def shot(p,html,omit):
    pg=p.new_page(viewport={'width':1080,'height':1920}); pg.set_content(html); pg.wait_for_timeout(400)
    return pg
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':1080,'height':1920}); pg.set_content(end_html()); pg.wait_for_timeout(500); pg.screenshot(path=TMP+'end.png')
    for n,(a,z,cs) in VIDS.items():
        for i,(t0,t1,ey,ti,fs) in enumerate(cs):
            pg.set_content(cap_html(ey,ti,fs)); pg.wait_for_timeout(400); pg.screenshot(path=f'{TMP}{n}-{i}.png',omit_background=True)
    b.close()
for n,(a,z,cs) in VIDS.items():
    d=z-a; tot=d+END-XF
    inp=['-ss',str(a),'-t',str(d),'-i',SRC]
    for i in range(len(cs)): inp+=['-loop','1','-framerate','30','-t',str(d),'-i',f'{TMP}{n}-{i}.png']
    inp+=['-loop','1','-framerate','30','-t',str(END),'-i',TMP+'end.png']
    f=f'[0:v]fps=30,scale=1080:1920:flags=lanczos,unsharp=5:5:0.5:5:5:0.0,setsar=1,format=yuv420p[v0];'
    last='v0'
    for i,(t0,t1,*_) in enumerate(cs):
        f+=f'[{i+1}:v]format=rgba,fade=t=in:st={t0}:d=0.4:alpha=1,fade=t=out:st={t1-0.4}:d=0.4:alpha=1[o{i}];[{last}][o{i}]overlay=0:0:format=auto[m{i}];'
        last=f'm{i}'
    e=len(cs)+1
    f+=f'[{e}:v]format=yuv420p,setsar=1[end];[{last}]format=yuv420p[mm];[mm][end]xfade=transition=fade:duration={XF}:offset={d-XF},format=yuv420p[vo];'
    f+=f'[0:a]aresample=44100,afade=t=in:d=0.3,afade=t=out:st={d-0.5}:d=0.5,apad=whole_dur={tot:.2f}[ao]'
    cmd=['ffmpeg','-v','error','-y']+inp+['-filter_complex',f,'-map','[vo]','-map','[ao]','-t',f'{tot:.2f}','-c:v','libx264','-preset','slow','-crf','17','-profile:v','high','-r','30','-c:a','aac','-b:a','128k','-movflags','+faststart',H+f'videos/{n}.mp4']
    subprocess.run(cmd,check=True); print(n,round(tot,1),'s')

# corte-2 v3: mesmo trecho do clipe (8 a 16 s), legenda unica "Dente natural nao e de uma cor so." do inicio ao fim,
# e cartao final no padrao v3 (convite para Enviar mensagem + Goiania e regiao). Uso: python3 gerar-videos.py
import os,subprocess,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import gerar as G
from playwright.sync_api import sync_playwright
H=G.H; SRC=H+'../criativos-v2/fotos-dela/video-feito-a-mao.mp4'; TMP='/tmp/bv3/'; os.makedirs(TMP,exist_ok=True)
CAP=f'''<html><head><meta charset="utf-8"><style>{G.FONTS}*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1920px;background:transparent}}
.g{{position:absolute;left:0;right:0;top:0;height:980px;background:linear-gradient(180deg,rgba(70,44,30,.94) 0%,rgba(90,58,40,.78) 48%,rgba(90,58,40,0) 100%)}}
.hd{{position:absolute;left:84px;right:84px;top:230px;font-family:Inter;font-weight:500;font-size:22px;letter-spacing:.22em;color:#F7F1E6;display:flex;justify-content:space-between}}
.hl{{position:absolute;left:84px;right:84px;top:276px;height:2px;background:#F7F1E6;opacity:.75}}
.tx{{position:absolute;left:84px;right:84px;top:340px;font-family:'Libre Caslon Text';color:#F7F1E6}}
.ey{{font-family:Inter;font-weight:500;font-size:28px;letter-spacing:.24em;text-transform:uppercase;color:#B9C4AC;margin-bottom:26px}}
h1{{font-weight:400;font-size:108px;line-height:1.06;letter-spacing:-.018em}} em{{font-style:italic}}
.pl{{position:absolute;left:84px;bottom:340px;display:inline-flex;align-items:center;gap:14px;padding:13px 26px 13px 22px;border:2px solid #F7F1E6;border-radius:999px;font-family:Inter;font-weight:500;font-size:22px;letter-spacing:.16em;color:#F7F1E6;background:rgba(58,37,25,.45)}}
</style></head><body><div class="g"></div><div class="hd"><span>DRA. BRENDA SIMEÃO</span><span>NATURALIDADE</span></div><div class="hl"></div>
<div class="tx"><div class="ey">Naturalidade</div><h1>Dente natural não é de <em>uma cor só.</em></h1></div>
<div class="pl">{G.PIN('#F7F1E6')}GOIÂNIA E REGIÃO</div></body></html>'''
END=G.closing(1080,1920,'brown','Facetas em resina','Esculpidas à mão, <em>para o seu rosto.</em>',104,('','NATURALIDADE'))
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox']); pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.set_content(CAP); pg.wait_for_timeout(400); pg.screenshot(path=TMP+'cap.png',omit_background=True)
    pg.set_content(END); pg.wait_for_timeout(400); pg.screenshot(path=TMP+'end.png'); b.close()
a,z,E,XF=8,16.05,2.8,0.5; d=z-a; tot=d+E-XF
f=('[0:v]fps=30,scale=1080:1920:flags=lanczos,unsharp=5:5:0.5:5:5:0.0,setsar=1,format=yuv420p[v0];'
   f'[1:v]format=rgba,fade=t=in:st=0.2:d=0.4:alpha=1[o];[v0][o]overlay=0:0:format=auto,format=yuv420p[m];'
   f'[2:v]format=yuv420p,setsar=1[e];[m][e]xfade=transition=fade:duration={XF}:offset={d-XF},format=yuv420p[vo];'
   f'[0:a]aresample=44100,afade=t=in:d=0.3,afade=t=out:st={d-0.5}:d=0.5,apad=whole_dur={tot:.2f}[ao]')
cmd=['ffmpeg','-v','error','-y','-ss',str(a),'-t',str(d),'-i',SRC,'-loop','1','-framerate','30','-t',str(d),'-i',TMP+'cap.png','-loop','1','-framerate','30','-t',str(E),'-i',TMP+'end.png',
     '-filter_complex',f,'-map','[vo]','-map','[ao]','-t',f'{tot:.2f}','-c:v','libx264','-preset','slow','-crf','17','-profile:v','high','-r','30','-c:a','aac','-b:a','128k','-movflags','+faststart',H+'videos/corte-2.mp4']
subprocess.run(cmd,check=True)
subprocess.run(['ffmpeg','-v','error','-y','-ss','1.5','-i',H+'videos/corte-2.mp4','-frames:v','1',H+'videos/capa-corte-2.png'],check=True)
print('corte-2',round(tot,1),'s')

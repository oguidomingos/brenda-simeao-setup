# Gera os criativos v2 no padrao aprovado (molde piece() = modelo-feed/story/capa-reels). Tudo nitido, uma PNG por peca.
# Requer o repo brenda-identidade (fontes, fotos em src/img, funcao piece/render).
import sys,os
sys.path.insert(0,'/root/projects/brenda-identidade/src')
from build_creatives import piece,render,CL
H=os.path.dirname(os.path.abspath(__file__))+'/'
def out(sub,name,w,h,**k):
    assert not any(str(v).endswith('_b') for v in k.values()), 'foto desfocada proibida'
    render(piece(w,h,**k),H+sub+'/'+name+'.png',w,h)
ads={1:[('Naturalidade','Dente natural<br>não é uma cor só.',''),
        ('','Dente natural não é de uma cor só.','Tem translucidez nas bordas, tom mais quente perto da gengiva, textura e brilho que mudam com a luz.'),
        ('','Por isso, na escultura à mão, a cor é trabalhada em camadas.','Pensando no seu rosto e no seu sorriso.')],
     2:[('Preservação do dente','Faceta estraga o dente?',''),
        ('','A proposta é ser o mais conservadora possível.','Com mínimo ou nenhum desgaste, conforme o caso.'),
        ('','Só na avaliação a Dra. confirma o que é indicado para você.','')],
     3:[('Escultura à mão','Cada faceta, esculpida à mão.',''),
        ('','Cada faceta, esculpida à mão, dente por dente.',''),
        ('','São 5 anos dedicados a facetas em resina.','Com planejamento individual para o seu rosto.')]}
cap={1:('dra-a1-sorriso','50% 50%'),2:('d090','50% 50%'),3:('camadas1','50% 45%')}
FIN={1:'Facetas em resina esculpidas à mão',2:'Uma conversa sobre preservar o seu dente',3:'Escultura em resina, feita pela própria Dra.'}
for n,fr in ads.items():
    for i,(ey,ti,bd) in enumerate(fr):
        nm='capa' if i==0 else f'q{i+1}'
        kw=dict(theme='brown' if i==0 else ('cream','sage')[i%2],story=True,eyebrow=ey,title=ti,body=bd,fs=(100 if n==1 else 116) if i==0 else 92,align='center' if i==0 else 'left')
        if i==0: kw.update(bg=cap[n][0],pos=cap[n][1])
        out('anuncios',f'a{n}-{nm}',1080,1920,**kw)
    out('anuncios',f'a{n}-q{len(fr)+1}',1080,1920,theme='brown',story=True,title=FIN[n],fs=88,closing=CL)
# variacao alternativa: capa antiga do anuncio 3 (a Dra. gostou da foto), mesma frase
out('alternativas','a3-capa-alt',1080,1920,theme='brown',story=True,eyebrow='Escultura à mão',title='Cada faceta, esculpida à mão.',fs=116,align='center',bg='bancada',pos='50% 40%')
out('anuncios','a4',1080,1350,theme='cream',photo='dra-labios-1',ph=700,pos='50% 50%',title='Dente natural não é de uma cor só',fs=84,closing='Avaliação presencial, particular.')
out('anuncios','a5',1080,1350,theme='sage',title='Medo de ficar com cara de dente de chiclete?',fs=104,closing='Avaliação presencial, particular.')
out('alternativas','a1-capa-alt',1080,1920,theme='brown',story=True,eyebrow='Naturalidade',title='Dente natural<br>não é uma cor só.',fs=100,align='center',bg='dra-a1-batom',pos='50% 50%')
out('alternativas','a4-alt',1080,1350,theme='cream',photo='dra-labios-2',ph=700,pos='50% 50%',title='Dente natural não é de uma cor só',fs=84,closing='Avaliação presencial, particular.')
C='calendario'
out(C,'p01',1080,1350,theme='cream',photo='retrato2',ph=860,pos='50% 30%',title='Oi, eu sou a Dra. Brenda Simeão.',fs=70,eyebrow='Cirurgiã-dentista · CRO-GO 18788')
P2=[dict(theme='cream',photo='d076',ph=740,pos='50% 50%',title='Dente natural não é de uma cor só',fs=80),
    dict(theme='sage',photo='d077',ph=640,pos='50% 40%',title='Translucidez nas pontas, cor mais quente perto da gengiva',eyebrow='Naturalidade',fs=64),
    dict(theme='cream',photo='v6067b',ph=640,pos='50% 50%',title='Textura e brilho vêm da escultura camada por camada',eyebrow='Escultura',fs=64),
    dict(theme='brown',title='Cada sorriso é planejado para um rosto',body='Avaliação presencial, particular.<br>Para conversar, toque no link da bio.',fs=88)]
for i,k in enumerate(P2): out(C,f'p02-{i+1}',1080,1350,pager=(i,4),**k)
P3=[dict(theme='sage',title='Medo de ficar com dente de chiclete?',body='Você não está sozinha(o).',fs=92),
    dict(theme='cream',eyebrow='De onde vem essa preocupação',title='Dentes muito brancos, todos iguais.',fs=88),
    dict(theme='cream',eyebrow='O que muda na escultura à mão',title='Cor, formato e textura pensados para o seu rosto.',fs=84),
    dict(theme='sage',eyebrow='Como se começa',title='Avaliação presencial, para olhar o seu caso.',fs=84),
    dict(theme='brown',title='Cada sorriso é um.',body='Avaliação presencial, particular.<br>Para conversar, toque no link da bio.',fs=96)]
for i,k in enumerate(P3): out(C,f'p03-{i+1}',1080,1350,pager=(i,5),**k)
P5=[dict(theme='brown',title='Faceta estraga o dente?',fs=104),
    dict(theme='cream',eyebrow='Preservação',title='A proposta é ser o mais conservadora possível.',fs=86),
    dict(theme='sage',title='Mínimo ou nenhum desgaste, conforme o caso.',fs=90),
    dict(theme='cream',title='Cada boca pede uma decisão diferente.',body='Só na avaliação isso é confirmado.',fs=86),
    dict(theme='brown',title='Para conversar, toque no link da bio.',body='Avaliação presencial, particular.',fs=88)]
for i,k in enumerate(P5): out(C,f'p05-{i+1}',1080,1350,pager=(i,5),**k)
out(C,'p09',1080,1350,theme='cream',photo='camadas2',ph=780,pos='50% 50%',title='Esculpido à mão, dente por dente.',fs=76,eyebrow='Escultura em resina')
out(C,'p14',1080,1350,theme='sage',title='“Eu faço como se fosse para mim.”',fs=96,align='center',eyebrow='Dra. Brenda Simeão')

sc=[(2000,20),(3000,20),(5000,22)]
rows=""
for v,c in sc:
    conv=v/c; q=conv*.35; a=q*.40; f=a*.30
    rows+=f"<tr><td><b>R$ {v:,.0f}</b></td><td>R$ {c}</td><td>~{conv:.0f}</td><td>~{q:.0f}</td><td>~{a:.0f}</td><td><b>~{round(f)}</b></td><td>R$ {round(f)*4000/1000:.0f} mil</td></tr>".replace(",",".")
def S(cls,inner):return f'<section class="s {cls}"><div class="in">{inner}</div></section>'
def head(k,t):return f'<div class="k">{k}</div><h2>{t}</h2>'
chk=lambda l:"".join(f"<li>{x}</li>" for x in l)
S1=["Setup da vitrine: Instagram (bio, link, destaques, padrão visual) e Landing Page","Ficha no Google Meu Negócio","Gestão de tráfego pago (Meta Ads → WhatsApp)","Mensuração: pixel/CAPI, CRM de leads e relatório mensal","Reunião mensal de resultados"]
S2=["Social media: 12 posts/mês + stories roteirizados","Calendário editorial mensal alinhado ao funil","Apoio na criação de conteúdo: roteiros e pautas de Reels","Edição de 4 Reels/mês e artes dos carrosséis","Legendas com CTA e hashtags locais"]
S3=["SEO local: Google Meu Negócio otimizado, páginas por tratamento, avaliações","Google Ads (rede de pesquisa) para quem já procura facetas em Goiânia","Remarketing e públicos semelhantes","Automação de WhatsApp: qualificação, follow-up 24h e 7 dias","Diária de captação de vídeo/foto por trimestre","Reunião quinzenal consultiva + painel ao vivo","Prioridade e banco de horas para serviços extras (landing pages, campanhas sazonais)"]
html=f"""<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><link rel="stylesheet" href="../shared/fonts.css"><title>Proposta Expoente | Dra Brenda Simeão</title><link rel="icon" href="data:,">
<style>
:root{{--ac:#A855F7;--hi:#C084FC;--mu:#b4b0bd;--dim:#8d8996}}
*{{box-sizing:border-box;margin:0}}html{{scroll-behavior:smooth;-webkit-text-size-adjust:100%}}
body{{font-family:Inter,sans-serif;font-weight:400;font-size:18px;line-height:1.55;color:#fff;background:#050208;overflow-x:hidden}}
.s{{min-height:100vh;min-height:100svh;padding:48px 22px 96px;position:relative;display:flex;flex-direction:column;justify-content:center;scroll-snap-align:start;
background:radial-gradient(60% 40% at 70% 5%,rgba(123,44,191,.28),transparent 60%),radial-gradient(40% 30% at 10% 30%,rgba(139,92,246,.12),transparent 60%),#050208}}
html{{scroll-snap-type:y proximity}}
.in{{width:100%;max-width:1080px;margin:0 auto}}
.k{{font:600 13.5px Inter;letter-spacing:.2em;text-transform:uppercase;color:var(--hi);margin-bottom:14px}}
h1,h2,h3{{font-family:'Cormorant Garamond',Georgia,serif;line-height:1.1;letter-spacing:-.01em;font-variant-numeric:lining-nums}}
h1{{font-weight:600;font-size:clamp(48px,13vw,92px);line-height:1.03}}
h2{{font-weight:600;font-size:clamp(38px,10vw,60px);margin-bottom:26px}}
h3{{font-weight:700;font-size:27px}}
h1 em,h2 em{{font-style:italic;font-weight:500;color:#DDBDFC}}
.foot{{display:none}}
.g{{display:grid;gap:16px;grid-template-columns:1fr}}
.c{{border:1px solid rgba(255,255,255,.14);border-radius:20px;padding:24px 22px;background:rgba(255,255,255,.06)}}
.c b{{display:block;font:500 54px/1 'Cormorant Garamond',serif;font-variant-numeric:lining-nums;color:var(--hi);margin-bottom:8px}}
.c h3{{margin-bottom:8px}}.c p{{font-size:18px;line-height:1.55;color:var(--mu);font-weight:400}}
ul{{list-style:none;padding:0}}li{{padding:8px 0 8px 26px;position:relative;font-size:18px;line-height:1.45;color:#e6e2ee}}li:before{{content:"→";position:absolute;left:0;color:var(--ac)}}
table{{width:100%;border-collapse:collapse;color:#e6e2ee}}thead{{display:none}}tr{{display:block;border:1px solid rgba(255,255,255,.14);border-radius:18px;padding:14px 18px;margin-bottom:12px;background:rgba(255,255,255,.06)}}
td{{display:flex;justify-content:space-between;gap:14px;padding:8px 0;border-bottom:1px solid rgba(255,255,255,.08);font-size:17px;text-align:right}}td:last-child{{border:0}}td:before{{content:attr(data-label);color:var(--hi);font-weight:500;text-align:left;flex:0 0 44%}}td:first-child{{display:block;text-align:left;font:700 24px/1.2 'Cormorant Garamond',serif;color:#fff}}td:first-child:before{{content:none}}
td b{{color:#fff;font-weight:500}}
.p{{border-radius:24px;padding:28px 24px;border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.06);display:flex;flex-direction:column}}
.p .pr{{font:600 64px/1.05 'Cormorant Garamond',serif;font-variant-numeric:lining-nums;margin:8px 0 2px}}.p .pr small{{font-size:18px;color:var(--dim)}}
.p.hot{{background:linear-gradient(180deg,rgba(139,92,246,.30),rgba(123,44,191,.14));border-color:var(--ac);box-shadow:0 0 50px rgba(123,44,191,.4)}}.p.hot .pr{{color:#DDBDFC}}.p.top{{border-color:rgba(221,189,252,.4)}}
.tag{{align-self:flex-start;font:600 13px Inter;letter-spacing:.14em;background:linear-gradient(180deg,#8B5CF6,#7B2CBF);color:#fff;padding:6px 12px;border-radius:99px;margin-bottom:12px}}
.mini{{font-size:15px;color:var(--dim);margin-top:14px;line-height:1.5}}.p .mini{{margin:0 0 12px}}
.shots{{display:flex;gap:12px}}.shots img{{width:calc(50% - 6px);height:auto;max-height:420px;object-fit:cover;object-position:top;border-radius:14px;border:1px solid rgba(255,255,255,.12)}}
.bar{{min-height:46px;border-radius:10px;background:linear-gradient(90deg,#A855F7,#8B5CF6);color:#fff;font:500 16px Inter;display:flex;align-items:center;padding:8px 14px;margin:8px 0;min-width:68%}}
.arrow{{display:none}}.old{{color:#ff8b96}}.new{{color:#7ef0b0}}
.logo{{font:600 16px Inter;letter-spacing:.3em;margin-bottom:30px}}.logo:before{{content:"";display:inline-block;width:16px;height:16px;border-radius:5px;background:linear-gradient(135deg,#A855F7,#7B2CBF);box-shadow:0 0 14px rgba(123,44,191,.5);margin-right:12px;vertical-align:-2px}}
.cover p.sub{{font-size:20px;font-weight:300;color:var(--mu);margin-top:22px;max-width:640px}}
.nav{{position:fixed;left:0;right:0;bottom:0;z-index:50;display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px 14px calc(10px + env(safe-area-inset-bottom));background:rgba(5,2,8,.88);backdrop-filter:blur(12px);border-top:1px solid rgba(255,255,255,.1)}}
.nav button{{font:500 18px Inter;color:#fff;background:linear-gradient(180deg,#8B5CF6,#7B2CBF);border:0;border-radius:99px;min-width:64px;height:48px;padding:0 20px}}.nav button:disabled{{opacity:.3}}
.nav span{{font-size:16px;color:var(--mu);font-variant-numeric:tabular-nums}}.bar2{{position:fixed;top:0;left:0;height:3px;background:var(--ac);z-index:60;width:0}}
@media(min-width:760px){{body{{font-size:20px}}.s{{padding:64px 56px 100px}}.g2{{grid-template-columns:1fr 1fr}}.g3{{grid-template-columns:repeat(3,1fr)}}.g4{{grid-template-columns:repeat(2,1fr)}}.g5{{grid-template-columns:repeat(2,1fr)}}
thead{{display:table-header-group}}tr{{display:table-row;border:0;padding:0;background:none;margin:0}}td{{display:table-cell;text-align:left;font-size:17px;padding:14px 10px;border-bottom:1px solid rgba(255,255,255,.1)}}td:before{{content:none!important}}td:first-child{{font-size:17px}}
th{{text-align:left;font:500 13px Inter;letter-spacing:.12em;text-transform:uppercase;color:var(--hi);padding:10px;border-bottom:1px solid var(--ac)}}.arrow{{display:table-cell}}.shots img{{max-height:480px}}}}
@media(min-width:1100px){{.g4{{grid-template-columns:repeat(4,1fr)}}.g5{{grid-template-columns:repeat(5,1fr)}}.foot{{display:flex;position:absolute;bottom:70px;left:56px;right:56px;justify-content:space-between;font-size:12px;color:var(--dim);letter-spacing:.14em}}}}
@media print{{@page{{size:1280px 1000px;margin:0}}html{{scroll-snap-type:none}}.nav,.bar2{{display:none!important}}.s{{height:1000px;min-height:0;padding:50px 56px;page-break-after:always;break-inside:avoid;overflow:hidden;-webkit-print-color-adjust:exact;print-color-adjust:exact}}.c,.p,tr,li{{break-inside:avoid}}}}
</style>
{S('cover',f'''<div class="k">Proposta comercial · Outubro 2026</div><div class="logo">EXPOENTE</div><h1>Seu sorriso de vitrine,<br>do Instagram <em>ao WhatsApp.</em></h1><p class="sub">Setup de marketing para a Dra Brenda Simeão: Instagram, Landing Page, tráfego e mensuração.</p><div class="foot"><span>EXPOENTE · ENGENHARIA DE CRESCIMENTO</span><span>Preparada para Dra Brenda Simeão · Goiânia</span></div>''')}
{S('',f'''{head('Quem somos · Método Trion','Marketing que você consegue <em>prever</em>')}<div class="g g3"><div class="c"><b>01</b><h3>Tráfego</h3><p>Anúncios locais com foco em conversa no WhatsApp e em custo por paciente, não em curtida. Ética de saúde (CFO) no centro.</p></div><div class="c"><b>02</b><h3>IA e Funis</h3><p>Do clique à consulta: landing, qualificação e follow-up automatizados, para nenhuma conversa ficar sem resposta.</p></div><div class="c"><b>03</b><h3>Growth</h3><p>Feito com dados, não achismo: CRM e relatório mensal mostram quanto vende, de onde vem e quanto custa cada paciente.</p></div></div><div class="foot"><span>EXPOENTE</span><span>02</span></div>''')}
{S('',f'''{head('Diagnóstico','Seu trabalho é de alto nível. O Instagram ainda não vende por ele.')}<div class="g g4"><div class="c"><b>884</b><h3>seguidores</h3><p>155 posts. Base pequena, com espaço grande de crescimento local.</p></div><div class="c"><b class="old">0</b><h3>links na bio</h3><p>A bio diz "Agende sua avaliação ⬇️", mas não há para onde clicar.</p></div><div class="c"><b class="old">~50%</b><h3>posts sem legenda</h3><p>Só emoji. Nenhum post pede o agendamento.</p></div><div class="c"><b class="old">0</b><h3>destaques e ficha Google</h3><p>Quem pesquisa o seu nome não encontra preço, local, prova ou botão de contato.</p></div></div><p style="margin-top:26px;font-size:16px;color:#b4b0bd">Fonte: auditoria do perfil @drabrendasimeao, 30 últimos posts, coleta de 14/10/2026.</p><div class="foot"><span>EXPOENTE</span><span>03</span></div>''')}
{S('',f'''{head('O que já funciona','Você já tem a base. Falta o funil em volta dela.')}<div class="g g2"><div><ul><li><b>Nicho claro:</b> ~70% do feed é facetas, com fotos macro de ótima qualidade</li><li><b>Constância:</b> ~1 post por semana nos últimos meses</li><li><b>Rosto vende:</b> foto sua teve 94 curtidas e 31 comentários, contra ~18 de média</li><li><b>Parcerias:</b> colabs com outros dentistas ampliam seu alcance</li></ul></div><div class="c" ><h3 style="color:#C084FC">Oportunidade</h3><p style="font-size:17px">Com link na bio, legenda com CTA e anúncio local, o mesmo conteúdo passa a gerar conversas no WhatsApp todos os dias, sem precisar de milhares de seguidores.</p></div></div><div class="foot"><span>EXPOENTE</span><span>04</span></div>''')}
{S('',f'''{head('Problemas → soluções','O que vamos corrigir, ponto a ponto')}<table><tr><th>Hoje</th><th></th><th>Como vai ficar</th></tr>
<tr><td class="old">Bio sem link</td><td class="arrow">→</td><td class="new">Link direto para WhatsApp/LP com mensagem pronta</td></tr>
<tr><td class="old">Legendas só com emoji, sem CTA</td><td class="arrow">→</td><td class="new">Legenda com história do caso + CTA + hashtags locais</td></tr>
<tr><td class="old">Quase sem antes/depois</td><td class="arrow">→</td><td class="new">1 caso por semana: queixa → solução → resultado</td></tr>
<tr><td class="old">Sem destaques</td><td class="arrow">→</td><td class="new">Resultados · Como funciona · Valores · Depoimentos · Local</td></tr>
<tr><td class="old">Reels sem gancho</td><td class="arrow">→</td><td class="new">Bastidor do esculpir com gancho e texto na tela</td></tr>
<tr><td class="old">Sem ficha no Google</td><td class="arrow">→</td><td class="new">Ficha otimizada + avaliações de pacientes</td></tr>
<tr><td class="old">Sem anúncios nem métricas</td><td class="arrow">→</td><td class="new">Meta Ads local + CRM + relatório mensal</td></tr></table><div class="foot"><span>EXPOENTE</span><span>05</span></div>''')}
{S('dark',f'''{head('O funil','Cada etapa pensada para levar a paciente até a cadeira')}<div class="g g5"><div class="c"><b>1</b><h3>Atração</h3><p>Conteúdo 3x/semana + anúncio local para Goiânia</p></div><div class="c"><b>2</b><h3>Conversão</h3><p>Landing Page e link da bio levam ao WhatsApp</p></div><div class="c"><b>3</b><h3>Qualificação</h3><p>3 perguntas antes da conversa: queixa, prazo, histórico</p></div><div class="c"><b>4</b><h3>Fechamento</h3><p>Avaliação com planejamento, parcelamento e follow-up 24h/7 dias</p></div><div class="c"><b>5</b><h3>Prova social</h3><p>Depoimentos e avaliações no Google alimentam o topo</p></div></div><p style="margin-top:30px;font-size:19px;color:#C084FC">CTA único e padrão: "Agende sua avaliação pelo WhatsApp".</p><div class="foot"><span>EXPOENTE</span><span>06</span></div>''')}
{S('',f'''{head('Já deixamos pronto','Nada de promessa: veja o setup funcionando')}<div class="g g2"><div class="shots"><img src="assets/lp-desktop.jpg" alt="Landing Page no desktop"><img src="assets/lp-mobile.jpg" alt="Landing Page no celular"></div><div><h3 style="font-size:24px;margin-bottom:12px">Landing Page completa</h3><p style="color:#a5a1ad;font-size:16px;margin-bottom:22px">Hero com CTA, dores, diferencial, passo a passo, resultados, sobre você, FAQ e formulário que qualifica e abre o WhatsApp.</p><h3 style="font-size:24px;margin-bottom:12px">9 legendas reescritas</h3><p style="color:#a5a1ad;font-size:16px">Mesmas fotos do seu perfil, com antes e depois lado a lado, para você ver a diferença hoje.</p></div></div><div class="foot"><span>EXPOENTE</span><span>07</span></div>''')}
{S('plans',f'''{head('Planos','Escolha o nível de acompanhamento')}<div class="g g3" style="align-items:stretch">
<div class="p"><h3>Vitrine + Tráfego</h3><div class="pr">R$ 1.500<small>/mês</small></div><p class="mini" style="margin:0 0 14px">Para começar a gerar conversas.</p><ul>{chk(S1)}</ul></div>
<div class="p hot"><span class="tag">MAIS ESCOLHIDO</span><h3>Vitrine + Tráfego + Social</h3><div class="pr">R$ 2.000<small>/mês</small></div><p class="mini" style="margin:0 0 14px;color:#a5a1ad">Tudo do plano anterior, mais:</p><ul>{chk(S2)}</ul></div>
<div class="p top"><span class="tag">COMPLETÃO</span><h3>Premium 360°</h3><div class="pr">R$ 3.500<small>/mês</small></div><p class="mini" style="margin:0 0 14px;color:#a5a1ad">Tudo dos planos anteriores, mais:</p><ul>{chk(S3)}</ul></div></div><p class="mini">Valores de gestão e produção. A verba de anúncios é paga direto à plataforma (Meta/Google), à parte. Setup inicial em até 30 dias.</p><div class="foot"><span>EXPOENTE</span><span>08</span></div>''')}
{S('',f'''{head('Compare','O que entra em cada plano')}<table><tr><th>Entrega</th><th>R$ 1.500</th><th>R$ 2.000</th><th>R$ 3.500</th></tr>
{"".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a,b,c,d in [("Setup Instagram + Landing Page","✓","✓","✓"),("Ficha Google Meu Negócio","✓","✓","✓ otimizada + avaliações"),("Tráfego pago Meta Ads","✓","✓","✓ + remarketing"),("CRM + relatório mensal","✓","✓","✓ + painel ao vivo"),("Social media e calendário editorial","—","12 posts/mês","12 posts/mês"),("Roteiros e edição de Reels","—","4 Reels/mês","8 Reels/mês"),("SEO local + Google Ads pesquisa","—","—","✓"),("Automação de follow-up WhatsApp","—","—","✓"),("Captação de vídeo/foto","—","—","1 diária/trimestre"),("Reuniões","Mensal","Mensal","Quinzenal")])}</table><div class="foot"><span>EXPOENTE</span><span>09</span></div>''')}
{S('dark',f'''{head('Investimento em tráfego','Quanto investir e o que esperar (estimativa)')}<table><tr><th>Verba mensal de anúncios</th><th>Custo por conversa</th><th>Conversas no WhatsApp</th><th>Qualificadas (35%)</th><th>Avaliações (40%)</th><th>Pacientes (30%)</th><th>Faturamento*</th></tr>{rows}</table><p style="margin-top:26px;font-size:16px;color:#C084FC">Recomendação para começar: R$ 3.000/mês de verba, com meta de ~6 novos pacientes de facetas por mês.</p><p class="mini" style="color:#9a9486">ESTIMATIVA aproximada, não garantia. Baseada em médias de mercado de anúncios locais de saúde/estética. *Faturamento ilustrativo com ticket médio hipotético de R$ 4.000 por paciente: precisamos validar com você o ticket real, a taxa de comparecimento e a velocidade de resposta no WhatsApp, que impactam muito o resultado. Nos 60 primeiros dias ajustamos as taxas com dados reais.</p><div class="foot"><span>EXPOENTE</span><span>10</span></div>''')}
{S('',f'''{head('Retorno','O investimento total se paga com poucos pacientes')}<div class="g g2"><div><div class="bar" style="width:100%">Verba R$ 3.000 → ~150 conversas</div><div class="bar" style="width:70%">~52 qualificadas</div><div class="bar" style="width:46%">~21 avaliações</div><div class="bar" style="width:30%">~6 pacientes</div></div><div class="c"><h3>Cenário base (plano R$ 2.000)</h3><p style="font-size:17px">Investimento total: R$ 3.000 de anúncios + R$ 2.000 de gestão = <b style="display:inline;font-size:17px">R$ 5.000/mês</b>.</p><p style="font-size:17px;margin-top:10px">Com ~6 pacientes a R$ 4.000 (hipotético), o faturamento estimado é de <b style="display:inline;font-size:17px">~R$ 24 mil</b>. O ponto de equilíbrio chega com ~2 pacientes.</p><p class="mini">Estimativa. Os números reais dependem do ticket, da agenda e da conversão no atendimento.</p></div></div><div class="foot"><span>EXPOENTE</span><span>11</span></div>''')}
{S('',f'''{head('Primeiros 30 dias','Como começamos')}<div class="g g4"><div class="c"><b>Sem. 1</b><h3>Fundação</h3><p>Acessos, briefing, autorização de imagem, número de WhatsApp, link da bio no ar</p></div><div class="c"><b>Sem. 2</b><h3>Vitrine</h3><p>Destaques, ficha Google, publicação da Landing Page, pixel e CRM</p></div><div class="c"><b>Sem. 3</b><h3>Anúncios</h3><p>Criativos com seus melhores casos e primeira campanha no ar</p></div><div class="c"><b>Sem. 4</b><h3>Otimização</h3><p>Primeiro relatório, ajuste de público e da abordagem no WhatsApp</p></div></div><div class="foot"><span>EXPOENTE</span><span>12</span></div>''')}
{S('dark',f'''<div class="k">Próximo passo</div><h1 style="font-size:54px">Vamos colocar seu<br>setup no ar?</h1><p style="margin-top:26px;font-size:20px;color:#a5a1ad;max-width:720px">Escolhendo o plano, iniciamos o briefing no mesmo dia. Nossa promessa: estrutura de vendas no ar em 14 dias.</p><p style="margin-top:34px;font-size:18px;color:#C084FC">guilherme@expoente.marketing</p><div class="foot"><span>EXPOENTE · ENGENHARIA DE CRESCIMENTO</span><span>13</span></div>''')}
<div class="bar2" id="bar"></div><div class="nav"><button id="pv" aria-label="Anterior">←</button><span id="ct"></span><button id="nx" aria-label="Próximo">→</button></div><script>const S=[...document.querySelectorAll('.s')];let i=0;const ct=document.getElementById('ct'),pv=document.getElementById('pv'),nx=document.getElementById('nx'),bar=document.getElementById('bar');
function go(n){{n=Math.max(0,Math.min(S.length-1,n));S[n].scrollIntoView({{behavior:'smooth',block:'start'}})}}
function upd(){{const y=innerHeight*.4;let k=0;S.forEach((e,j)=>{{if(e.getBoundingClientRect().top<=y)k=j}});i=k;ct.textContent=(i+1)+' / '+S.length;pv.disabled=i==0;nx.disabled=i==S.length-1;bar.style.width=((i+1)/S.length*100)+'%'}}
addEventListener('scroll',upd,{{passive:true}});upd();pv.onclick=()=>go(i-1);nx.onclick=()=>go(i+1);
addEventListener('keydown',e=>{{if(['ArrowRight','ArrowDown','PageDown',' '].includes(e.key)){{e.preventDefault();go(i+1)}}if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key)){{e.preventDefault();go(i-1)}}}});</script></html>"""
# labels mobile nas tabelas
import re
def lab(m):
    t=m.group(0);hs=[re.sub('<.*?>','',h) for h in re.findall(r'<th>(.*?)</th>',t)]
    def row(r):
        n=[0]
        def td(x):
            j=n[0];n[0]+=1
            return '<td data-label="'+hs[j]+'"'+x.group(1)+'>' if j<len(hs) and hs[j] else x.group(0)
        return re.sub(r'<td( [^>]*)?>',lambda x:td(type('X',(),{'group':lambda self,k=0:(x.group(1) or '') if k==1 else x.group(0)})()),r.group(0))
    return re.sub(r'<tr>.*?</tr>',row,t,flags=re.S)
html=re.sub(r'<table.*?</table>',lab,html,flags=re.S)
import sys;sys.path.insert(0,'../shared');import icons
html=html.replace('</style>',icons.CSS+'</style>',1).replace('<body>','<body>',1)
head,body=html.split('</style>',1)
body=icons.iconize(body).replace('✓',icons.svg('check'))
body=re.sub(r'(<td[^>]*>)(.*?)(</td>)',r'\1<span>\2</span>\3',body)
html=head+'</style>'+icons.SPRITE+body
html=re.sub(r'(<table>)(<tr>(?:<th>.*?</th>)+</tr>)',r'\1<thead>\2</thead>',html)
open('proposta-v4.html','w').write(html)

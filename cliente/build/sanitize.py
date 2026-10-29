import re, sys, pathlib
S = pathlib.Path('/root/projects/brenda-simeao-setup')
OUT = pathlib.Path('/root/work/brenda-cliente/md'); OUT.mkdir(exist_ok=True)

NAMES = {
 'dossie-estrategico-funil.md':'o dossiê estratégico e de funil','dossie-estrategico-funil':'o dossiê estratégico e de funil',
 'gravacoes.md':'o plano de gravações','roteiros-gravacao.md':'o guia de roteiros e gravação',
 'calendario-instagram.md':'o calendário do Instagram','crm-brenda.md':'o desenho do CRM',
 'triagem-whatsapp-brenda.md':'o documento de triagem no WhatsApp','rastreio-e-relatorio-brenda.md':'o documento de rastreio e relatório',
 'tracking.md':'o documento de Pixel e rastreamento','instagram-perfil.md':'o pacote do Instagram',
 'dominio-e-acessos.md':'o documento de domínio e acessos','auditoria-dra-brenda.md':'a auditoria inicial',
}
# (arquivo, regex de títulos "## " a remover — vai até o próximo título do mesmo nível ou acima)
DROP = {
 'dossie-estrategico-funil': [r'^## 0\.', r'^### 1\.4', r'^### 4\.3', r'^### 4\.5'],
 'calendario-instagram': [r'^## 6\.', r'^## 8\.'],
 'crm-brenda': [r'^## 0\.', r'^## 2\.', r'^## 3\.'],
 'tracking': [r'^## 1\.', r'^## 4\.'],
 'instagram-perfil': [r'^## Contexto rápido', r'^## 1\.'],
 'roteiros-gravacao': [r'^## 0\.', r'^## 5\.'],
 'revisao-cfo-cro-lp': [r'^## schema', r'^## Avaliações \(QR\)'],
 'triagem-whatsapp-brenda': [], 'rastreio-e-relatorio-brenda': [],
}
def drop_sections(lines, pats):
    out=[]; skip=None
    for l in lines:
        m=re.match(r'^(#+) ',l)
        if m:
            lvl=len(m.group(1))
            if skip is not None and lvl<=skip: skip=None
            if skip is None and any(re.search(p,l) for p in pats): skip=lvl
        if skip is None: out.append(l)
    return out

LINE_DROP = re.compile(r'^(Base:|Referência:|Versão \d.*Base:)|R\$|brain_search|segundo cérebro|Evolution API|\bAPP_SECRET|act_\d|Thumdra|Travassos|Vitor Guilherme|Augusto|Pedro\b|Nada foi (criado|publicado|enviado)|[Nn]ada foi ligado|Atas do onboarding|briefing da tarefa|/root/|/opt/|\.(md|py|html)\b.*`|`[^`]*\.(md|py|html|jpg)`', re.I)

def clean(name, text):
    lines = drop_sections(text.split('\n'), DROP.get(name, []))
    out=[]
    for l in lines:
        if l.startswith('Versão') and 'Base:' in l: l = l.split('· Base:')[0].rstrip(' ·')
        if re.search(r'R\$', l) and 'sem "R$"' in l: l = l.replace('sem "R$", ','sem preço, ')
        if LINE_DROP.search(l) and not l.startswith('#') and not l.startswith('|'):
            continue
        out.append(l)
    t='\n'.join(out)
    # tabelas: células com refs de arquivo -> nomes amigáveis
    for k,v in NAMES.items(): t=t.replace('`'+k+'`', v).replace(k, v)
    t=re.sub(r'`(?:instagram/assets/)?(p\d+)\.jpg`',r'foto \1',t)
    t=re.sub(r'`lp/assets/([\w-]+)\.jpg`',r'foto \1 da LP',t)
    t=re.sub(r'`dra-brenda\*\.jpg`','fotos da Dra.',t)
    t=re.sub(r'`(instagram|lp|tools)/[^`]*`','material de apoio',t)
    t=re.sub(r'\s*\(?`\d{12,}`\)?','',t)
    t=re.sub(r'`[\w./-]+\.(?:md|py|html|jpg|svg)`','o material de apoio',t)
    t=re.sub(r'\s*\(EXP-\d+[^)]*\)','',t); t=re.sub(r'EXP-\d+ ?','',t)
    t=t.replace('[OK GUILHERME + Dra.]','[aprovação pendente: Guilherme e Dra.]').replace('[OK GUILHERME]','[aprovação pendente]')
    t=re.sub(r'\*\*\[OK GUILHERME[^\]]*\]\*\*','**[aprovação pendente]**',t)
    t=re.sub(r'\[OK GUILHERME[^\]]*\]','[aprovação pendente]',t)
    t=t.replace('access_token','chave de acesso').replace('token de acesso de sistema','chave de acesso').replace('token de acesso','chave de acesso').replace('token da API','chave da API').replace('token','chave').replace('Token','Chave')
    t=t.replace('o Felipe','a equipe de aplicação').replace('Felipe','equipe de aplicação').replace('**FEL**','**EQP**').replace('**GUI**','**EXP**')
    t=t.replace('Precisa de decisão do Guilherme','Pendente de decisão').replace('Decisão do Guilherme em','Decisão de').replace('(decisão do Guilherme, sem refazer nada)','(sem refazer nada)').replace('o Guilherme tira','a Expoente tira').replace('Guilherme pode reclassificar','a Expoente pode reclassificar').replace('pedida pelo Guilherme','incluída a pedido da Expoente')
    t=t.replace(' (arquivo separado)','')
    t=t.replace('em o material de apoio','na LP').replace('na pasta o material de apoio e em o material de apoio','nas pastas de fotos').replace('em material de apoio','na LP')
    t=t.replace('Instalação na LP (o material de apoio)','Instalação na LP').replace('alterações aplicadas em o material de apoio','alterações aplicadas')
    t=t.replace('O chave','A chave').replace('o chave','a chave').replace('um chave','uma chave').replace('(Node ou n8n)','(Node)').replace('no repositório','no código').replace('neste repositório','neste material')
    t=re.sub(r'`window\.PIXEL_ID="\d+"` preenchido','ID do Pixel preenchido',t)
    t=re.sub(r'`PIXEL_ID` \d+','ID do Pixel',t)
    t=t.replace('`o material de apoio`','material de apoio')
    t=t.replace('na pasta material de apoio e na LP','nas pastas de fotos').replace('Instalação na LP (material de apoio)','Instalação na LP').replace('Fotos do material de apoio (p01 a p21)','Fotos do acervo do Instagram (p01 a p21)')
    t=t.replace('o material de apoio, ','fotos de apoio, ').replace('o material de apoio','foto de apoio').replace('material de apoio','fotos de apoio')
    t=t.replace('(atendimento.jpg)','(foto de atendimento)').replace('(preparo.jpg)','(foto de preparo)')
    return t
for n in DROP:
    t=(S/f'{n}.md').read_text(); (OUT/f'{n}.md').write_text(clean(n,t))
t=pathlib.Path('/root/work/brenda-cliente/src/concorrentes.md').read_text()
(OUT/'benchmark-concorrentes.md').write_text(clean('benchmark',t))

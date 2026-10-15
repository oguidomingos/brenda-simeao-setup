import re
# Ícones line (stroke), cantos arredondados, preenchimento translúcido. Uso: inline sprite + <svg class="ic"><use href="#i-nome"/></svg>
P={
'phone':'<path d="M5 4h4l2 5-2.500 1.500a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
'tooth':'<path d="M7.500 3C5 3 3.500 5 3.500 7.500c0 2 1 3 1.500 5 .5 2.500.8 8.500 3 8.500 1.800 0 1.800-4 3-4s1.200 4 3 4c2.200 0 2.500-6 3-8.500.5-2 1.500-3 1.500-5C19.500 5 18 3 15.500 3c-1.500 0-2.300.8-3.500.8S9 3 7.500 3z"/>',
'angle':'<path d="M4 20V4l16 16z"/><path d="M4 10h3M4 14h4M10 20v-3M14 20v-4" fill="none"/>',
'face':'<circle cx="12" cy="12" r="9"/><path d="M9 10h.01M15 10h.01M9 15.500h6" fill="none"/>',
'smile':'<circle cx="12" cy="12" r="9"/><path d="M9 10h.01M15 10h.01M8.500 14.500a4.500 4.500 0 0 0 7 0" fill="none"/>',
'pin':'<path d="M12 21s7-6.200 7-11.500A7 7 0 0 0 5 9.500C5 14.800 12 21 12 21z"/><circle cx="12" cy="9.500" r="2.500" fill="none"/>',
'clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2" fill="none"/>',
'sparkle':'<path d="M11 3l1.800 5.200L18 10l-5.200 1.800L11 17l-1.800-5.200L4 10l5.200-1.800z"/><path d="M19 15v4M17 17h4" fill="none"/>',
'heart':'<path d="M12 20s-8-4.800-8-11a4.500 4.500 0 0 1 8-2.800A4.500 4.500 0 0 1 20 9c0 6.200-8 11-8 11z"/>',
'chat':'<path d="M4 5h16v11H9l-5 4z"/>',
'eye':'<path d="M2 12s3.500-7 10-7 10 7 10 7-3.500 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3" fill="none"/>',
'hand':'<path d="M8 13V5.500a1.500 1.500 0 0 1 3 0V11M11 5V4a1.500 1.500 0 0 1 3 0v7M14 6.500a1.500 1.500 0 0 1 3 0V14a6 6 0 0 1-6 6h-1a6 6 0 0 1-5-2.700L3.500 14.500a1.500 1.500 0 0 1 2.500-1.600L8 15"/>',
'leaf':'<path d="M5 19C5 10 10 5 20 4c0 10-4 15-12 15z"/><path d="M5 19l7-7" fill="none"/>',
'check':'<circle cx="12" cy="12" r="9"/><path d="M8 12.500l2.800 2.800L16 9.500" fill="none"/>',
'alert':'<path d="M12 3l10 17H2z"/><path d="M12 10v4M12 17.500h.01" fill="none"/>',
'right':'<path d="M4 12h16M14 6l6 6-6 6" fill="none"/>',
'down':'<path d="M12 4v16M6 14l6 6 6-6" fill="none"/>',
}
SPRITE='<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>'+''.join(f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k,v in P.items())+'</defs></svg>'
CSS='.ic{width:1.15em;height:1.15em;vertical-align:-.2em;flex:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round;fill:currentColor;fill-opacity:.14;opacity:.85;display:inline-block}.ic path[fill=none],.ic circle[fill=none]{fill:none}'
M={'📲':'phone','🦷':'tooth','📐':'angle','😶':'face','📍':'pin','🕘':'clock','✨':'sparkle','➡':'right','⬇':'down','💬':'chat','🤍':'heart','😍':'smile','🤩':'smile','😊':'smile','☺':'smile','👀':'eye','🫶':'heart','👋':'hand','🍃':'leaf','✅':'check','⚠':'alert','👏':'sparkle','❤':'heart','⚡':'sparkle'}
STRIP=re.compile('[️‍\U0001F3FB-\U0001F3FF]')
def svg(n,cls=''):return f'<svg class="ic {cls}"><use href="#i-{n}"/></svg>'
def iconize(t):
    t=STRIP.sub('',t)
    return re.sub('|'.join(map(re.escape,M)),lambda m:svg(M[m.group(0)]),t)
def strip(t):
    t=STRIP.sub('',t); t=re.sub('|'.join(map(re.escape,M)),'',t); return re.sub(r'[ \t]+\n','\n',re.sub(r'  +',' ',t))

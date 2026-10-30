import sys,re
P='vite.config.ts'; NL=chr(10)
LIST="['swiper', 'workbox-window']"
canon="  ssr: { noExternal: "+LIST+" },"
s=open(P,encoding='utf-8').read()
if re.search(r"noExternal:\s*\['swiper',\s*'workbox-window'\]", s):
    print('SKIP idempotent: list udah presisi, NOL nyentuh'); sys.exit(0)
s2=re.sub(r"[ \t]*ssr:[ \t]*\{[ \t]*noExternal:[ \t]*(\[[^\]]*\]|true)[ \t]*\},[ \t]*", canon+NL, s)
if s2==s:
    ms=list(re.finditer(r'defineConfig\(\{', s))
    if len(ms)!=1: print('NO ANCHOR bersih (0 atau >1) -> paste cat vite.config.ts'); sys.exit(1)
    i=ms[0].end(); s2=s[:i]+NL+canon+s[i:]
lines=s2.split(NL); out=[l.rstrip() for l in lines]
nws=sum(1 for a,b in zip(lines,out) if a!=b)
open(P,'w',encoding='utf-8',newline=NL).write(NL.join(out))
print('FIX SSR OK: true -> list %s  trailingWS-dibersihin=%d'%(LIST,nws))

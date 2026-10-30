import sys,re
P='vite.config.ts'; NL=chr(10); BS=chr(92)
canon="  ssr: { noExternal: [/^swiper("+BS+"/|$)/] },"
s=open(P,encoding='utf-8').read()
upgraded = ("/^swiper("+BS+"/|$)/" not in s)
s2=re.sub(r"[ \t]*ssr:[ \t]*\{[ \t]*noExternal:[ \t]*\[[^\]]*\][ \t]*\},[ \t]*", canon+NL, s)
lines=s2.split(NL); out=[l.rstrip() for l in lines]
nws=sum(1 for a,b in zip(lines,out) if a!=b)
open(P,'w',encoding='utf-8',newline=NL).write(NL.join(out))
print('FIX SSR OK: regex=%s  trailingWS-dibersihin=%d'%('upgraded' if upgraded else 'already', nws))

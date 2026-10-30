import sys,re
P='vite.config.ts'
s=open(P,encoding='utf-8').read()
if 'noExternal' in s: print('SKIP idempotent: noExternal udah ada, NOL nyentuh'); sys.exit(0)
if re.search(r'\bssr\s*:', s): print('AMBIGU: ada block ssr: existing tanpa noExternal -> paste cat vite.config.ts, gue merge bener (NOL nebak)'); sys.exit(1)
INJ="\n  ssr: { noExternal: ['swiper'] },\n  "
chosen=None
for pat in [r'defineConfig\(\{', r'export\s+default\s+\{']:
    ms=list(re.finditer(pat,s))
    if len(ms)==1: chosen=(pat,ms[0]); break
if not chosen: print('NO ANCHOR bersih (0 atau >1) -> paste cat vite.config.ts'); sys.exit(1)
pat,m=chosen; i=m.end(); out=s[:i]+INJ+s[i:]
if out.count('{')!=out.count('}'): print('SANITY brace ga seimbang -> JANGAN tulis, paste file'); sys.exit(1)
open(P,'w',encoding='utf-8',newline='\n').write(out)
print('PATCH OK: sisipin ssr.noExternal[swiper] setelah anchor',pat)

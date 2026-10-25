import sys
p='LEGODONE.md'
s=open(p,encoding='utf-8').read()
NEW='- ☐ GUNUNG 1.5 KATALOG tp-o.tk — adapter+fixture+debug kelar (cc8e3f5); skema TS + colok halaman nyusul'
ANCH='- ☐ GUNUNG 3 SEO/SSR'
if 'GUNUNG 1.5' in s: print('>> udah ke-track, skip (idempotent)'); sys.exit(0)
if s.count(ANCH)!=1: print('[MELESET] anchor GUNUNG 3 !=1, file TIDAK ditulis'); sys.exit(1)
s=s.replace(ANCH,NEW+'\n'+ANCH,1)
open(p,'w',encoding='utf-8').write(s)
print('OK sisip GUNUNG 1.5 sebelum GUNUNG 3')
# csttan_sync.py (gabungan): anchor longgar 'SELESAI' + repr diagnostik + fallback EOF.
# Emoji ✅ sbg escape \u2705 -> source .py 100% ASCII (kebal clipboard/ligatur); pas nulis, Python render balik jd ✅.
import sys
p='csttan.md'
s=open(p,encoding='utf-8').read()
if 'GUNUNG 1.5' in s: print('>> udah ke-track, skip (idempotent)'); sys.exit(0)
lines=s.split('\n')
idx=-1
for i,l in enumerate(lines):
    if 'SELESAI' in l:
        idx=i
        print('anchor baris %d repr=%r'%(i+1,l))
        break
CK='\u2705'
add=['  %s GUNUNG 1: skema AffiliateOffer TS (19 field, doc ACCESSTRADE telanjang) - 27c093f'%CK,
'  %s GUNUNG 2 part1: fixture promos.json + kartu Agoda + tombol KLAIM noopener - 74bdc11'%CK,
'  %s GUNUNG 1.5 b1+b4: adapter tpoNormalize (norm-envelope-before-dot, unknown->product) + fixture 3 shape + runner - cc8e3f5'%CK]
if idx>=0:
    lines[idx+1:idx+1]=add
    print('sisip setelah baris %d (1-based %d)'%(idx,idx+1))
else:
    lines+=['','----- %s SELESAI (csttan.md) -----'%CK]+add
    print('SELESAI nggak ada -> append blok baru di EOF')
open(p,'w',encoding='utf-8').write('\n'.join(lines))
print('OK ditulis')
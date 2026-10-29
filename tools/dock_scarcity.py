import os,sys
P='src/pages/duality.vue'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
if 'grid-template-rows: 1fr' in t: sys.exit('udah 1-baris, skip')
OLD='grid-template-rows: repeat(2, auto); grid-auto-flow: column;'
NEW='grid-template-rows: 1fr; grid-auto-flow: column;'
c=t.count(OLD)
if c!=1: sys.exit('MELESET count=%d (harus 1): %r'%(c,OLD[:30]))
for ch in NEW:
    if ord(ch)>127: sys.exit('MELESET non-ASCII NEW')
t=t.replace(OLD,NEW)
if 'grid-template-rows: repeat(2, auto)' in t: sys.exit('MELESET 2-baris belum ilang')
if 'grid-template-rows: 1fr' not in t: sys.exit('MELESET 1-baris nggak masuk')
if 'grid-auto-columns: 56px' not in t: sys.exit('MELESET size slot berubah (harus tetep 56)')
if t.count('position: fixed')!=1: sys.exit('MELESET botnav rusak')
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK dock 1-baris (scarcity: 12 slot kepotong=geser)',P)

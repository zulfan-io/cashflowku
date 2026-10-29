import os,sys
P='src/pages/duality.vue'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
if 'display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px' in t: sys.exit('udah vertikal, skip')
FEED_OLD='.feed { display: flex; gap: 12px; margin: 10px calc(-1 * clamp(12px, 3vw, 32px)) 12px; padding-inline: clamp(12px, 3vw, 32px); overflow-x: auto; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; scrollbar-width: none; }\n.feed::-webkit-scrollbar { display: none; }\n.feed > * { flex: 0 0 auto; width: min(30vw, 160px); scroll-snap-align: start; }'
FEED_NEW='.feed { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin: 10px 0 12px; }\n@media (min-width: 640px) { .feed { grid-template-columns: repeat(auto-fill, minmax(170px, 1fr)); gap: 12px; } }'
c=t.count(FEED_OLD)
if c!=1: sys.exit('MELESET count=%d (harus 1): %r'%(c,FEED_OLD[:30]))
for ch in FEED_NEW:
    if ord(ch)>127: sys.exit('MELESET non-ASCII NEW')
t=t.replace(FEED_OLD,FEED_NEW)
if 'grid-auto-flow: column' not in t: sys.exit('MELESET dock 2-baris ilang')
if 'repeat(2, 1fr)' not in t: sys.exit('MELESET feed vertikal nggak masuk')
if 'min(30vw' in t: sys.exit('MELESET feed horizontal masih ada')
if t.count('position: fixed')!=1: sys.exit('MELESET botnav rusak')
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK feed vertikal 2-kolom',P)

import os,sys
P='src/pages/duality.vue'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
if 'grid-auto-flow: column' in t: sys.exit('udah 2-baris, skip')
DOCK_OLD='.dock { display: flex; gap: 8px; margin: 10px 0; overflow-x: auto; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; scrollbar-width: none; }\n.dock::-webkit-scrollbar { display: none; }'
DOCK_NEW='.dock { display: grid; grid-template-rows: repeat(2, auto); grid-auto-flow: column; grid-auto-columns: 84px; gap: 8px; margin: 10px calc(-1 * clamp(12px, 3vw, 32px)); padding-inline: clamp(12px, 3vw, 32px); overflow-x: auto; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; scrollbar-width: none; }\n.dock::-webkit-scrollbar { display: none; }\n.dock > * { scroll-snap-align: start; }'
FEED_OLD='.feed { display: flex; gap: 12px; margin: 10px 0 12px; overflow-x: auto; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; scrollbar-width: none; }\n.feed::-webkit-scrollbar { display: none; }\n.feed > * { flex: 0 0 auto; width: min(46vw, 200px); scroll-snap-align: start; }'
FEED_NEW='.feed { display: flex; gap: 12px; margin: 10px calc(-1 * clamp(12px, 3vw, 32px)) 12px; padding-inline: clamp(12px, 3vw, 32px); overflow-x: auto; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; scrollbar-width: none; }\n.feed::-webkit-scrollbar { display: none; }\n.feed > * { flex: 0 0 auto; width: min(30vw, 160px); scroll-snap-align: start; }'
SLOT_OLD='.slot { position: relative; flex: 0 0 auto; width: 84px; scroll-snap-align: start; background: #fff; border: 1px solid #eee; border-radius: 14px; padding: 14px 4px 10px; text-align: center; transition: background .15s, transform .15s; }'
SLOT_NEW='.slot { position: relative; background: #fff; border: 1px solid #eee; border-radius: 14px; padding: 14px 4px 10px; text-align: center; transition: background .15s, transform .15s; }'
errs=[]
for o,n in [(DOCK_OLD,DOCK_NEW),(FEED_OLD,FEED_NEW),(SLOT_OLD,SLOT_NEW)]:
    c=t.count(o)
    if c!=1: errs.append('count=%d: %r'%(c,o[:30]))
    else:
        for ch in n:
            if ord(ch)>127: errs.append('non-ASCII: %r'%n[:30]); break
        t=t.replace(o,n)
if errs:
    print('[MELESET] TIDAK ditulis:'); [print('  ',e) for e in errs]; sys.exit(1)
if t.count('grid-auto-flow: column')!=1: sys.exit('MELESET 2-baris')
if t.count('calc(-1 * clamp')!=2: sys.exit('MELESET bleed harus 2x (dock+feed)')
if 'min(30vw' not in t: sys.exit('MELESET 3-visible')
if t.count('position: fixed')!=1: sys.exit('MELESET botnav rusak')
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK flow 2-baris+3+bleed',P)

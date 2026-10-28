import os,sys
P='src/pages/duality.vue'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
if 'scroll-snap-type: x mandatory' in t: sys.exit('udah layout, skip')
RW='    <section v-if="pulsaOn" class="reward">\n      Main game -> kumpulin poin -> <b>pulsa gratis</b> dari owner\n    </section>\n'
R=[
(RW+'\n',''),
('    <nav class="botnav">', RW+'\n    <nav class="botnav">'),
('.dock { display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 8px; margin: 10px 0; }',
 '.dock { display: flex; gap: 8px; margin: 10px 0; overflow-x: auto; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; scrollbar-width: none; }\n.dock::-webkit-scrollbar { display: none; }'),
('.feed { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin: 10px 0 12px; }',
 '.feed { display: flex; gap: 12px; margin: 10px 0 12px; overflow-x: auto; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; scrollbar-width: none; }\n.feed::-webkit-scrollbar { display: none; }\n.feed > * { flex: 0 0 auto; width: min(46vw, 200px); scroll-snap-align: start; }'),
('.slot { position: relative; background: #fff; border: 1px solid #eee; border-radius: 14px; padding: 14px 4px 10px; text-align: center; transition: background .15s, transform .15s; }',
 '.slot { position: relative; flex: 0 0 auto; width: 84px; scroll-snap-align: start; background: #fff; border: 1px solid #eee; border-radius: 14px; padding: 14px 4px 10px; text-align: center; transition: background .15s, transform .15s; }'),
]
errs=[]
for o,n in R:
    c=t.count(o)
    if c!=1: errs.append('count=%d: %r'%(c,o[:34]))
    else:
        for ch in n:
            if ord(ch)>127: errs.append('non-ASCII: %r'%n[:34]); break
        t=t.replace(o,n)
if errs:
    print('[MELESET] TIDAK ditulis:'); [print('  ',e) for e in errs]; sys.exit(1)
if t.count('class="reward"')!=1: sys.exit('MELESET reward bukan 1x')
if not (t.index('</main>')<t.index('class="reward"')<t.index('<nav class="botnav">')): sys.exit('MELESET reward bukan di antara feed&botnav')
if t.count('scroll-snap-type: x mandatory')!=2: sys.exit('MELESET snap harus 2x (dock+feed)')
if '.feed > *' not in t or '.dock { display: flex' not in t: sys.exit('MELESET marker flex')
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK layout',P)

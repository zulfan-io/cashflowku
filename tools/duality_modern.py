import os,sys
P='src/pages/duality.vue'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
if 'repeat(auto-fit, minmax(150px' in t: sys.exit('udah modern, skip')
ASIDE='''    <aside class="dock">
      <div v-for="w in slots" :key="w.id" class="slot" :class="{ off: !w.enabled }">
        <span class="ic">{{ w.id.slice(0, 2).toUpperCase() }}</span>
        <span class="lb">{{ w.kind }}</span>
        <span v-if="!w.enabled" class="soon">segera</span>
      </div>
    </aside>'''
R=[
('.dual { max-width: 720px; margin: 0 auto; padding: 12px 12px 64px; font-family: system-ui, sans-serif; color: #1a1a1a; background: #f7f7f7; min-height: 100vh; }',
 '.dual { max-width: 1280px; margin: 0 auto; padding: 12px clamp(12px, 3vw, 32px) 64px; font-family: system-ui, sans-serif; color: #1a1a1a; background: #f7f7f7; min-height: 100vh; }'),
('.feed { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin: 10px 0 12px; }',
 '.feed { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin: 10px 0 12px; }'),
('@media (min-width: 560px) { .feed { grid-template-columns: repeat(3, 1fr); } }',
 '/* auto-fit handle scaling, NOL breakpoint lompat */'),
('.dock { position: fixed; right: 12px; bottom: 64px; width: 176px; background: #fff; border: 1px solid #eee; border-radius: 14px; padding: 8px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; box-shadow: 0 8px 24px rgba(0,0,0,.12); padding-bottom: calc(8px + env(safe-area-inset-bottom)); }',
 '.dock { display: grid; grid-template-columns: repeat(auto-fit, minmax(80px, 1fr)); gap: 8px; margin: 10px 0; }'),
('.slot { position: relative; background: #fafafa; border-radius: 10px; padding: 8px 2px; text-align: center; transition: background .15s; }',
 '.slot { position: relative; background: #fff; border: 1px solid #eee; border-radius: 14px; padding: 14px 4px 10px; text-align: center; transition: background .15s, transform .15s; }'),
('.ic { display: block; font-weight: 800; color: #FF6600; font-size: 13px; }',
 '.ic { display: block; font-weight: 800; color: #FF6600; font-size: 18px; line-height: 1.1; }'),
('.lb { display: block; font-size: 9px; color: #666; margin-top: 2px; }',
 '.lb { display: block; font-size: 10px; color: #666; margin-top: 4px; }'),
('  .dock { background: #1c1c1c; border-color: #2a2a2a; box-shadow: 0 8px 24px rgba(0,0,0,.5); }',
 '  .dock { background: transparent; border-color: transparent; }'),
('  .slot { background: #242424; }',
 '  .slot { background: #1c1c1c; border-color: #2a2a2a; }'),
('''    </main>

    <aside class="dock">
      <div v-for="w in slots" :key="w.id" class="slot" :class="{ off: !w.enabled }">
        <span class="ic">{{ w.id.slice(0, 2).toUpperCase() }}</span>
        <span class="lb">{{ w.kind }}</span>
        <span v-if="!w.enabled" class="soon">segera</span>
      </div>
    </aside>

    <nav class="botnav">''',
 '''    </main>

    <nav class="botnav">'''),
('    <main class="feed">', ASIDE+'\n\n    <main class="feed">'),
]
errs=[]
for o,n in R:
    c=t.count(o)
    if c!=1: errs.append('count=%d: %r'%(c,o[:34]))
    else:
        for ch in n:
            if ord(ch)>127: errs.append('non-ASCII new: %r'%n[:34]); break
        t=t.replace(o,n)
if errs:
    print('[MELESET] TIDAK ditulis:'); [print('  ',e) for e in errs]; sys.exit(1)
if t.count('position: fixed')!=1: sys.exit('MELESET botnav rusak (fixed harus 1x)')
if t.count('<aside class="dock">')!=1 or t.count('</aside>')!=1: sys.exit('MELESET aside bukan 1x')
for m in ['repeat(auto-fit, minmax(150px','max-width: 1280px','repeat(auto-fit, minmax(80px']:
    if m not in t: sys.exit('MELESET marker '+m)
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK modern',P)

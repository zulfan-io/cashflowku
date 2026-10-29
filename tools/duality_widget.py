import os,sys
P='src/pages/duality.vue'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
if 'grid-auto-columns: 52px' in t: sys.exit('udah widget kecil, skip')
R=[
('.dock { display: grid; grid-template-rows: repeat(2, auto); grid-auto-flow: column; grid-auto-columns: 84px; gap: 8px; margin: 10px calc(-1 * clamp(12px, 3vw, 32px)); padding-inline: clamp(12px, 3vw, 32px); overflow-x: auto; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; scrollbar-width: none; }',
 '.dock { display: grid; grid-template-rows: repeat(2, auto); grid-auto-flow: column; grid-auto-columns: 52px; gap: 6px; margin: 8px calc(-1 * clamp(12px, 3vw, 32px)); padding-inline: clamp(12px, 3vw, 32px); overflow-x: auto; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; scrollbar-width: none; }'),
('.slot { position: relative; background: #fff; border: 1px solid #eee; border-radius: 14px; padding: 14px 4px 10px; text-align: center; transition: background .15s, transform .15s; }',
 '.slot { position: relative; background: transparent; border: 0; border-radius: 12px; padding: 6px 2px; text-align: center; transition: background .15s, transform .15s; }'),
('.ic { display: block; font-weight: 800; color: #FF7A45; font-size: 18px; line-height: 1.1; }',
 '.ic { display: block; font-weight: 800; color: #FF7A45; font-size: 13px; line-height: 1.1; }'),
('.lb { display: block; font-size: 10px; color: #666; margin-top: 4px; }',
 '.lb { display: block; font-size: 9px; color: #666; margin-top: 2px; }'),
]
errs=[]
for o,n in R:
    c=t.count(o)
    if c!=1: errs.append('count=%d: %r'%(c,o[:30]))
    else:
        for ch in n:
            if ord(ch)>127: errs.append('non-ASCII: %r'%n[:30]); break
        t=t.replace(o,n)
if errs:
    print('[MELESET WIDGET] TIDAK ditulis:'); [print('  ',e) for e in errs]; sys.exit(1)
if 'grid-auto-columns: 52px' not in t: sys.exit('MELESET marker widget')
if t.count('position: fixed')!=1: sys.exit('MELESET botnav rusak')
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK widget kecil',P)

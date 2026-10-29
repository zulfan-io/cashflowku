import os,sys,json
DV='src/pages/duality.vue'; PJ='src/data/ports.json'
for f in (DV,PJ):
    if not os.path.isfile(f): sys.exit('NGGAK ADA '+f)
dv=open(DV,encoding='utf-8').read(); pj=open(PJ,encoding='utf-8').read()
errs=[]
if 'background: transparent; border: 0;' in dv and 'grid-auto-columns: 56px' in dv and '"floating_max_slots": 12' in pj:
    sys.exit('udah widget2, skip')
R=[
('.slot { position: relative; background: transparent; border: 0; border-radius: 12px; padding: 6px 2px; text-align: center; transition: background .15s, transform .15s; }',
 '.slot { position: relative; background: #fff; border: 1px solid #eee; border-radius: 12px; padding: 8px 2px; text-align: center; transition: background .15s, transform .15s; }'),
('grid-auto-columns: 52px; gap: 6px;','grid-auto-columns: 56px; gap: 6px;'),
('.ic { display: block; font-weight: 800; color: #FF7A45; font-size: 13px; line-height: 1.1; }',
 '.ic { display: block; font-weight: 800; color: #FF7A45; font-size: 15px; line-height: 1.1; }'),
]
for o,n in R:
    c=dv.count(o)
    if c!=1: errs.append('duality count=%d: %r'%(c,o[:28]))
    else:
        for ch in n:
            if ord(ch)>127: errs.append('non-ASCII dv: %r'%n[:28]); break
        dv=dv.replace(o,n)
c=pj.count('"floating_max_slots": 8')
if c!=1: errs.append('ports count=%d max_slots'%c)
else: pj=pj.replace('"floating_max_slots": 8','"floating_max_slots": 12')
if errs:
    print('[MELESET] TIDAK ditulis (file utuh):'); [print('  ',e) for e in errs]; sys.exit(1)
try: json.loads(pj)
except Exception as e: sys.exit('MELESET json ports: %s'%e)
if 'background: #fff; border: 1px solid #eee' not in dv: sys.exit('MELESET kotak slot')
if 'grid-auto-columns: 56px' not in dv: sys.exit('MELESET size dock')
if '"floating_max_slots": 12' not in pj: sys.exit('MELESET slots 12')
if dv.count('position: fixed')!=1: sys.exit('MELESET botnav rusak')
for ch in dv+pj:
    if ord(ch)>127: sys.exit('MELESET non-ASCII final')
open(DV,'w',encoding='utf-8',newline='\n').write(dv)
open(PJ,'w',encoding='utf-8',newline='\n').write(pj)
print('OK widget2: kotak balik + 56px + 12 slot (geser)',DV,PJ)

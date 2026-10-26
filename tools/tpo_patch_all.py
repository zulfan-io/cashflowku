import subprocess,sys
A='src/utils/tpoNormalize.js'; G='tools/tpo_batu4.py'
a=open(A,encoding='utf-8').read(); g=open(G,encoding='utf-8').read()
res=[]
def one(s,anchor,repl,marker,name):
    if marker in s: res.append((name,'skip')); return s
    if s.count(anchor)==1: res.append((name,'apply')); return s.replace(anchor,repl,1)
    res.append((name,'MELESET')); return s
one_a=lambda *x: globals().__setitem__('a',one(a,*x)) or a
# adapter: value-object trim + array-element trim + prod images[]/shop_id
a=one(a,':norm(v[k]);}return o;}',":(typeof v[k]==='string'?v[k].trim():norm(v[k]));}return o;}",'v[k].trim()','norm-value-trim')
a=one(a,'return v.map(norm);',"return v.map(function(x){return typeof x==='string'?x.trim():norm(x)});","typeof x==='string'",'norm-array-trim')
a=one(a,'return{id:p.id,name:p.name,image:(p.images&&p.images[0])||null,sold:p.sold||0,','return{id:p.id,name:p.name,images:Array.isArray(p.images)?p.images:[],shop_id:p.shop_id||null,sold:p.sold||0,','shop_id:p.shop_id','prod-images-shopid')
# generator: shop_id field
g=one(g,'"id ":2,"name "','\"id \":2,\"shop_id\":3,\"name "','\"shop_id\":3','gen-shopid')
if any(st=='MELESET' for _,st in res):
    print('[MELESET] TIDAK ditulis:'); [print('  -',n,st) for n,st in res if st=='MELESET']; sys.exit(1)
if all(st=='skip' for _,st in res):
    print('>> semua udah ke-patch, skip (idempotent)'); sys.exit(0)
open(A,'w',encoding='utf-8').write(a); open(G,'w',encoding='utf-8').write(g)
print('status:',[(n,st) for n,st in res])
print('regen fixture + re-check:')
subprocess.run([sys.executable,G])
r=subprocess.run(['python3','tools/card_field_check.py'],capture_output=True,text=True)
print(r.stdout,end='')
if r.stderr: print('[stderr]',r.stderr.strip()[:120])
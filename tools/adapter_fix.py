import sys
p='src/utils/tpoNormalize.js'
s=open(p,encoding='utf-8').read()
if 'shop_id:p.shop_id' in s: print('>> udah ke-patch, skip'); sys.exit(0)
e=[]
A1=":norm(v[k]);}return o;}"
B1=":(typeof v[k]==='string'?v[k].trim():norm(v[k]));}return o;}"
A2="return{id:p.id,name:p.name,image:(p.images&&p.images[0])||null,sold:p.sold||0,"
B2="return{id:p.id,name:p.name,images:Array.isArray(p.images)?p.images:[],shop_id:p.shop_id||null,sold:p.sold||0,"
if s.count(A1)!=1: e.append('anchor norm-value !=1')
if s.count(A2)!=1: e.append('anchor prod-shape !=1')
if e:
    print('[MELESET] TIDAK ditulis:'); [print('  -',x) for x in e]; sys.exit(1)
s=s.replace(A1,B1,1).replace(A2,B2,1)
open(p,'w',encoding='utf-8').write(s)
print('OK patch: norm trim value + prod images[]/shop_id')
print('verify images:Array=%d shop_id=%d trimVal=%d (hrs 1 1 1)'%(s.count('images:Array.isArray'),s.count('shop_id:p.shop_id'),s.count("v[k].trim()")))
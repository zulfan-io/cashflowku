import os,sys
P='src/components/CProductCardThin.vue'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
if 'picsum.photos' in t: sys.exit('udah foto, skip')
OLD='''      <span v-else class="ph-t">foto</span>'''
NEW='''      <img v-else :src="'https://picsum.photos/seed/shoper-' + props.product.id + '/400/400'" alt="" loading="lazy" />'''
c=t.count(OLD)
if c!=1: sys.exit('MELESET count=%d (harus 1): %r'%(c,OLD[:30]))
for ch in NEW:
    if ord(ch)>127: sys.exit('MELESET non-ASCII NEW')
t=t.replace(OLD,NEW)
if 'picsum.photos' not in t: sys.exit('MELESET picsum nggak masuk')
if 'ph-t">foto' in t: sys.exit('MELESET abu foto belum ilang')
if '#FF7A45' not in t: sys.exit('MELESET coral card rusak')
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK foto picsum seeded',P)

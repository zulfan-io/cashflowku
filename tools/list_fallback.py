import os,sys
P='src/pages/list.vue'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
if 'dummyBatch' in t: sys.exit('udah fallback, skip')
OLD1='async function loadBatch() {'
NEW1='''const NAMES = ['Kemeja Flanel Oversize','Celana Kargo Dewasa','Hoodie Fleece Premium','Sepatu Sneakers Retro','Tas Ransel Anti Air','Jam Tangan Digital Sport','Jaket Denim Klasik','Sandal Kulit Pria']
const PRICES = [89000,120000,135000,199000,159000,75000,210000,99000]
function dummyBatch(from) {
  const out = []
  for (let i = 0; i < PAGE; i++) {
    const n = from + i
    out.push(mapOffer({ id: n + 1, title: NAMES[n % NAMES.length], image_url: 'https://picsum.photos/seed/shoper-list-' + n + '/400/400', price: PRICES[n % PRICES.length] }))
  }
  return out
}

async function loadBatch() {'''
OLD2='  if (error || !data || !data.length) { done.value = true; return }'
NEW2='''  if (error || !data || !data.length) {
    if (items.value.length < CAP) {
      items.value = items.value.concat(dummyBatch(from))
      if (items.value.length >= CAP) done.value = true
      return
    }
    done.value = true; return
  }'''
errs=[]
for o,n in [(OLD1,NEW1),(OLD2,NEW2)]:
    c=t.count(o)
    if c!=1: errs.append('count=%d: %r'%(c,o[:30]))
    else:
        for ch in n:
            if ord(ch)>127: errs.append('non-ASCII: %r'%n[:30]); break
        t=t.replace(o,n)
if errs:
    print('[MELESET FALLBACK] TIDAK ditulis:'); [print('  ',e) for e in errs]; sys.exit(1)
for m in ['dummyBatch','NAMES','items.value.length < CAP']:
    if m not in t: sys.exit('MELESET marker '+m)
if 'function mapOffer' not in t: sys.exit('MELESET mapOffer hilang')
if t.count('done.value = true')<2: sys.exit('MELESET logika done')
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK list fallback dummy',P)

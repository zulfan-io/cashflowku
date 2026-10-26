import sys
p='src/pages/shop/[shop].vue'
s=open(p,encoding='utf-8').read()
if 'tpoParse' in s: print('>> udah ke-colok, skip'); sys.exit(0)
A1="import ShopRequest from '~/services/shop-request'"
A2="useShop.publicProducts = productData.data"
if s.count(A1)!=1: print('[MELESET] anchor import !=1'); sys.exit(1)
if s.count(A2)!=1: print('[MELESET] anchor assignment !=1'); sys.exit(1)
s=s.replace(A1, A1+"\nimport { tpoParse } from '~/utils/tpoNormalize'", 1)
s=s.replace(A2,
"const _p = tpoParse(productData)\n  useShop.publicProducts = _p.kind === 'list' ? _p.list : (Array.isArray(productData) ? productData : [])", 1)
open(p,'w',encoding='utf-8').write(s)
print('OK colok shop: import + assignment kebal 2 shape')
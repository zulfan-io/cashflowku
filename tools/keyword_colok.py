import sys
p='src/pages/search/[keyword].vue'
s=open(p,encoding='utf-8').read()
if 'tpoParse' in s: print('>> udah ke-colok, skip'); sys.exit(0)
A1="import ProductRequest from '~/services/product-request'"
A2="useKeyword.resultProduct = searchData.data"
if s.count(A1)!=1: print('[MELESET] anchor import !=1'); sys.exit(1)
if s.count(A2)!=1: print('[MELESET] anchor assignment !=1'); sys.exit(1)
s=s.replace(A1, A1+"\nimport { tpoParse } from '~/utils/tpoNormalize'", 1)
s=s.replace(A2,
"const _k = tpoParse(searchData)\n  useKeyword.resultProduct = _k.kind === 'list' ? _k.list : []", 1)
open(p,'w',encoding='utf-8').write(s)
print('OK colok keyword: import + assignment (list-only, fallback [])')
import sys
p='package.json'
s=open(p,encoding='utf-8').read()
if '"onlyBuiltDependencies"' not in s: print('>> udah ilang, skip'); sys.exit(0)
A=',\n    "onlyBuiltDependencies": [\n      "@parcel/watcher",\n      "cypress",\n      "esbuild",\n      "swiper",\n      "vue-demi",\n      "vue-echarts"\n    ]'
if s.count(A)!=1:
    print('[MELESET] anchor count=%d (hrs 1), TIDAK ditulis'%s.count(A)); sys.exit(1)
open(p,'w',encoding='utf-8').write(s.replace(A,'',1))
print('OK hapus onlyBuiltDependencies (dead config pnpm9 di lockfile pnpm7)')
print('verify obd=%d peer=%d (hrs 0 1)'%(s.count('"onlyBuiltDependencies"'),s.count('"peerDependencyRules"')))
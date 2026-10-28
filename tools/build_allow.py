import os,sys
P='pnpm-workspace.yaml'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
if 'onlyBuiltDependencies' in t:
    print('>> udah ada onlyBuiltDependencies, skip'); sys.exit(0)
add='\nonlyBuiltDependencies:\n  - esbuild\n  - swiper\n  - vue-demi\n  - vue-echarts\n'
t=t.rstrip('\n')+'\n'+add
for ch in t:
    if ord(ch)>127: sys.exit('MELESET non-ASCII')
for m in ['allowBuilds','onlyBuiltDependencies','- esbuild','- vue-echarts']:
    if m not in t: sys.exit('MELESET marker '+m)
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK hedge',P)

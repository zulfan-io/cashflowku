import os,sys
P='pnpm-workspace.yaml'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
if t.lstrip().startswith('packages:'):
    print('>> udah ada packages:, skip'); sys.exit(0)
t='packages: []\n'+t
for ch in t:
    if ord(ch)>127: sys.exit('MELESET non-ASCII')
for m in ['packages: []','allowBuilds','onlyBuiltDependencies']:
    if m not in t: sys.exit('MELESET marker '+m)
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK prefix packages: []',P)

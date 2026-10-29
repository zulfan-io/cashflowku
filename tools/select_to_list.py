import os,sys
P='src/pages/duality.vue'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
if "router.push('/list')" in t: sys.exit('udah redirect, skip')
R=[
("import { supabase } from '~/utils/supabase'\n",
 "import { supabase } from '~/utils/supabase'\nimport { useRouter } from 'vue-router'\n"),
('const loveCounts = ref({})',
 'const router = useRouter()\nconst loveCounts = ref({})'),
("console.log('select', p.id, p.name)",
 "router.push('/list')"),
]
errs=[]
for o,n in R:
    c=t.count(o)
    if c!=1: errs.append('count=%d: %r'%(c,o[:30]))
    else:
        for ch in n:
            if ord(ch)>127: errs.append('non-ASCII: %r'%n[:30]); break
        t=t.replace(o,n)
if errs:
    print('[MELESET SELECT] TIDAK ditulis:'); [print('  ',e) for e in errs]; sys.exit(1)
if "router.push('/list')" not in t: sys.exit('MELESET marker push')
if t.count('useRouter')<2: sys.exit('MELESET useRouter kurang (import+const)')
if t.count('position: fixed')!=1: sys.exit('MELESET botnav rusak')
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK duality onSelect -> /list',P)

import os,sys
P='src/pages/index.vue'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
if "router.replace('/duality')" in t: sys.exit('udah redirect, skip')
OLD="<script setup>\nuseHead({\n"
NEW="<script setup>\nimport { useRouter } from 'vue-router'\nconst router = useRouter()\nrouter.replace('/duality')\nuseHead({\n"
c=t.count(OLD)
if c!=1: sys.exit('MELESET count=%d (harus 1): %r'%(c,OLD[:30]))
for ch in NEW:
    if ord(ch)>127: sys.exit('MELESET non-ASCII di NEW')
t=t.replace(OLD,NEW)
for m in ["import { useRouter } from 'vue-router'","router.replace('/duality')"]:
    if m not in t: sys.exit('MELESET marker '+m)
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK redirect root -> /duality',P)

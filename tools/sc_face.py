import os,sys
P='src/pages/sc-preview.vue'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
if 'scface-' in t: sys.exit('udah wajah, skip')
OLD='      <StoryCircle v-for="(f, i) in faces" :key="f" :label="f" :read="i < 2" :size="60" @open="() => {}" />'
NEW='      <StoryCircle v-for="(f, i) in faces" :key="f" :label="f" :src="\'https://picsum.photos/seed/scface-\' + f + \'/120/120\'" :read="i < 2" :size="60" @open="() => {}" />'
c=t.count(OLD)
if c!=1: sys.exit('MELESET count=%d (harus 1): %r'%(c,OLD[:30]))
for ch in NEW:
    if ord(ch)>127: sys.exit('MELESET non-ASCII NEW')
t=t.replace(OLD,NEW)
if 'scface-' not in t: sys.exit('MELESET src nggak masuk')
if ':label="f"' not in t: sys.exit('MELESET label fallback hilang (harus tetep ada kalau gambar gagal)')
if '<StoryCircle' not in t: sys.exit('MELESET tag hilang')
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK sc-preview wajah picsum',P)

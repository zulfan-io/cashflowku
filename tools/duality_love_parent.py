import os,sys
P='src/pages/duality.vue'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
if 'function onLove' in t: sys.exit('udah ada handler, skip')
R=[
('          @select="onSelect"\n        />',
 '          @select="onSelect"\n          @love="onLove"\n          @share="onShare"\n          :love-count="loveCounts[p.id] || 0"\n          :share-count="shareCounts[p.id] || 0"\n        />'),
('function onSelect(p) {',
 '''const loveCounts = ref({})
const shareCounts = ref({})
async function onLove(p) {
  const { data: { user } } = await supabase.auth.getUser()
  if (!user) { console.log('login dulu buat love'); return }
  const { data: mem } = await supabase.from('shoper_members').select('id').eq('user_id', user.id).single()
  if (!mem) { console.log('belum jadi member'); return }
  const { error } = await supabase.from('shoper_loves').insert({ member_id: mem.id, target_type: 'offer', target_id: String(p.id) })
  if (!error) loveCounts.value[p.id] = (loveCounts.value[p.id] || 0) + 1
}
async function onShare(p) {
  const { error } = await supabase.from('shoper_shares').insert({ target_type: 'offer', target_id: String(p.id), channel: 'app' })
  if (!error) shareCounts.value[p.id] = (shareCounts.value[p.id] || 0) + 1
}
function onSelect(p) {'''),
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
    print('[MELESET PARENT] TIDAK ditulis:'); [print('  ',e) for e in errs]; sys.exit(1)
if t.count('position: fixed')!=1: sys.exit('MELESET botnav rusak')
if '.dual {' not in t: sys.exit('MELESET .dual ilang')
for m in ['function onLove','@love="onLove"','loveCounts']:
    if m not in t: sys.exit('MELESET marker parent '+m)
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK parent handler',P)

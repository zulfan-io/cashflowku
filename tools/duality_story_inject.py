import os,sys
SC='src/components/StoryCircle.vue'; DV='src/pages/duality.vue'
for f in (SC,DV):
    if not os.path.isfile(f): sys.exit('NGGAK ADA '+f)
sc=open(SC,encoding='utf-8').read(); dv=open(DV,encoding='utf-8').read()
if 'storyFaces' in dv: sys.exit('udah sisip, skip')
errs=[]
# 1) StoryCircle props (anchor 1x, kebukti)
o1="defineProps<{ src?: string | null; label?: string; read?: boolean; size?: number }>()"
n1="defineProps<{ src?: string | null; label?: string; read?: boolean; size?: number; ring?: string }>()"
if sc.count(o1)!=1: errs.append('SC props count=%d'%sc.count(o1))
else: sc=sc.replace(o1,n1)
# 2) StoryCircle style: anchor PAKAI konteks sc-ring biar unik (fix dosa count=2)
o2='<span class="sc-ring" :style="{ width: s + \'px\', height: s + \'px\' }">'
n2='<span class="sc-ring" :style="{ width: s + \'px\', height: s + \'px\', borderColor: ring || undefined }">'
if sc.count(o2)!=1: errs.append('SC style count=%d (harus 1)'%sc.count(o2))
else: sc=sc.replace(o2,n2)
# 3) duality script: storyFaces sebelum chips (anchor kebukti line 53)
co='const chips = Object.values(brands).slice(0, 12)'
cn='const storyFaces = [\'A\',\'B\',\'C\',\'D\',\'E\',\'F\',\'G\']\n'+co
if dv.count(co)!=1: errs.append('DV chips count=%d'%dv.count(co))
else: dv=dv.replace(co,cn)
# 4) duality template: rail SEBELUM section chips, indent 4/6 selaras (rapi Coi)
to='    <section class="chips">'
tn='''    <div class="storyrail">
      <StoryCircle v-for="(f, i) in storyFaces" :key="f" :label="f" :src="'https://picsum.photos/seed/dstory-' + f + '/120/120'" :read="i < 1" :size="54" ring="#0095F6" />
    </div>
    <section class="chips">'''
if dv.count(to)!=1: errs.append('DV chips-tag count=%d'%dv.count(to))
else: dv=dv.replace(to,tn)
# 5) duality style: .storyrail sebelum </style>
so='</style>'
sn='''.storyrail { display: flex; gap: 10px; overflow-x: auto; padding: 10px clamp(12px,3vw,32px); scrollbar-width: none; -webkit-overflow-scrolling: touch; }
.storyrail::-webkit-scrollbar { display: none; }
</style>'''
if dv.count(so)!=1: errs.append('DV /style count=%d'%dv.count(so))
else: dv=dv.replace(so,sn)
if errs:
    print('[MELESET] TIDAK ditulis (file utuh):'); [print('  ',e) for e in errs]; sys.exit(1)
for ch in sc+dv:
    if ord(ch)>127: sys.exit('MELESET non-ASCII')
if 'ring="#0095F6"' not in dv: sys.exit('MELESET biru nggak masuk')
if 'storyFaces' not in dv or '.storyrail' not in dv: sys.exit('MELESET marker duality')
if 'ring?' not in sc or 'borderColor: ring' not in sc: sys.exit('MELESET marker SC')
open(SC,'w',encoding='utf-8',newline='\n').write(sc)
open(DV,'w',encoding='utf-8',newline='\n').write(dv)
print('OK inject: ring biru + rail story di duality (sc1/sc2 selamat)')

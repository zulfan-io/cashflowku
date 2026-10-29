import os,sys
FILES=['src/components/StoryCircle.vue','src/components/Dots.vue','src/components/NotifDot.vue','src/pages/sc-preview.vue']
OLD='<script setup>'
NEW='<script setup lang="ts">'
errs=[]; pend={}
for P in FILES:
    if not os.path.isfile(P): errs.append('NGGAK ADA '+P); continue
    t=open(P,encoding='utf-8').read()
    if NEW in t: continue
    c=t.count(OLD)
    if c!=1: errs.append('%s count=%d (harus 1)'%(P,c)); continue
    tn=t.replace(OLD,NEW)
    if NEW not in tn: errs.append('%s marker hilang'%P); continue
    for ch in tn:
        if ord(ch)>127: errs.append('%s non-ASCII'%P); break
    pend[P]=tn
if errs:
    print('[MELESET] TIDAK ditulis (file utuh):'); [print('  ',e) for e in errs]; sys.exit(1)
for P,tn in pend.items():
    open(P,'w',encoding='utf-8',newline='\n').write(tn)
print('OK lang=ts ->', len(pend), 'file')

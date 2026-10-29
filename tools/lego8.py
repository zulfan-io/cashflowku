import os,sys
P='LEGODONE.md'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
B=chr(9744); C=chr(9745)
FL=[('- '+B+' StoryCircle.vue','- '+C+' StoryCircle.vue'),
('- '+B+' Dots.vue','- '+C+' Dots.vue'),
('- '+B+' NotifDot.vue','- '+C+' NotifDot.vue'),
('- '+B+' hero = rail story bulat','- '+C+' hero = rail story bulat'),
('- '+B+' navbar ikon-saja','- '+C+' navbar ikon-saja'),
('- '+B+' dot posisi carousel','- '+C+' dot posisi carousel'),
('- '+B+' hero = katalog produk','- '+C+' hero = katalog produk'),
('- '+B+' seller story-circle di card','- '+C+' seller story-circle di card'),
('- '+B+' navbar ikon+label','- '+C+' navbar ikon+label'),
('- '+B+' 2 demo NOL nyentuh','- '+C+' 2 demo NOL nyentuh'),
('- '+B+' yin-yang = KOMPOSISI','- '+C+' yin-yang = KOMPOSISI'),
('- '+B+' gate Coi: acc split','- '+C+' gate Coi: acc split')]
errs=[]
for o,n in FL:
    c=t.count(o)
    if c!=1: errs.append('count=%d: %r'%(c,o[2:30]))
    else: t=t.replace(o,n)
if errs:
    print('[MELESET LEGO] TIDAK ditulis:'); [print('  ',e) for e in errs]; sys.exit(1)
GEL='\n- '+B+' story viewer penuh (swipe/progress/posting dari shoper_status) = GELOMBANG C, NOL nebak scope'
if 'GELOMBANG C' not in t:
    anchor='- '+C+' backend story = shoper_status'
    if t.count(anchor)!=1: sys.exit('MELESET anchor backend')
    t=t.replace(anchor, anchor+GEL)
for ch in t:
    if ord(ch)>127 and ch not in (B,C): pass
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK legodone GUNUNG 8 di-centang + gelombang C dicatat')

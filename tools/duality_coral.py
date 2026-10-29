import os,sys
P='src/pages/duality.vue'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
if '#FF7A45' in t and 'prefers-color-scheme' not in t: sys.exit('udah coral+terang, skip')
n=t.count('#FF6600')
if n==0: sys.exit('MELESET #FF6600 nggak ada (file beda versi?)')
t=t.replace('#FF6600','#FF7A45')
if '#FF6600' in t: sys.exit('MELESET masih ada #FF6600')
if t.count('#FF7A45')!=n: sys.exit('MELESET count coral mismatch')
SM='/* auto-fit handle scaling'; DM='@media (prefers-color-scheme: dark)'; EM='</style>'
i=t.find(SM)
if i==-1: i=t.find(DM)
j=t.find(EM)
if i==-1 or j==-1 or i>=j: sys.exit('MELESET marker blok dark')
t=t[:i]+t[j:]
if 'prefers-color-scheme' in t: sys.exit('MELESET dark belum ilang')
if t.count(EM)!=1: sys.exit('MELESET </style> rusak')
if '.dual {' not in t: sys.exit('MELESET .dual ilang')
if t.count('position: fixed')!=1: sys.exit('MELESET botnav rusak')
for ch in t:
    if ord(ch)>127: sys.exit('MELESET non-ASCII')
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK coral+terang',P,'(%d aksen di-flip)'%n)

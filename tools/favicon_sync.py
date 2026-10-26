import os,shutil,sys
CAND=['/sdcard/Download/ImageKilat/41.jpg','/sdcard/Download/41.jpg',os.path.expanduser('~/storage/shared/Download/ImageKilat/41.jpg'),os.path.expanduser('~/storage/shared/Download/41.jpg'),'./41.jpg','./ImageKilat/41.jpg']
src=next((c for c in CAND if os.path.isfile(c)),None)
if not src:
    print('[NOL FILE] 41.jpg nggak ketemu di kandidat:'); [print('  -',c) for c in CAND]
    print('>> share/download 41.jpg ke salah satu path itu, atau kasih tau path-nya, run ulang.'); sys.exit(1)
dst='public/favicon.jpg'
os.makedirs('public',exist_ok=True)
shutil.copyfile(src,dst)
print('OK copy',src,'->',dst,os.path.getsize(dst),'byte')
p='index.html'; s=open(p,encoding='utf-8').read()
A='<link rel="icon" href="/favicon.svg" type="image/svg+xml">'
B='<link rel="icon" href="/favicon.jpg" type="image/jpeg">'
if A not in s:
    if 'favicon.jpg' in s: print('>> index.html udah ke-patch, skip'); sys.exit(0)
    print('[MELESET] anchor favicon.svg nggak ada, TIDAK ditulis'); sys.exit(1)
open(p,'w',encoding='utf-8').write(s.replace(A,B,1))
print('OK patch index.html line 7 -> favicon.jpg')
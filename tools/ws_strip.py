import re,sys
p='index.html'
s=open(p,encoding='utf-8').read()
ls=s.split('\n')
print('SEBELUM baris 37 repr =',repr(ls[36]) if len(ls)>36 else 'N/A')
n=re.sub(r'[ \t]+\n','\n',s)
buang=len(s)-len(n)
if buang==0: print('>> nggak ada trailing-ws, skip (idempotent)'); sys.exit(0)
open(p,'w',encoding='utf-8').write(n)
ls2=n.split('\n')
print('SESUDAH baris 37 repr =',repr(ls2[36]) if len(ls2)>36 else 'N/A')
print('OK buang %d char trailing-ws'%buang)
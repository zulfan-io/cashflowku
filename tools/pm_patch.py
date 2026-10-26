import sys
p='package.json'
s=open(p,encoding='utf-8').read()
if '"packageManager"' in s: print('>> udah ada packageManager, skip'); sys.exit(0)
A='"scripts": {'
B='"packageManager": "pnpm@7.33.7",\n  "scripts": {'
if s.count(A)!=1:
    print('[MELESET] anchor scripts count=%d (hrs 1), TIDAK ditulis'%s.count(A))
    print('>> jalanin: grep -n "\\"scripts\\"" package.json , lapor output-nya'); sys.exit(1)
s=s.replace(A,B,1)
open(p,'w',encoding='utf-8').write(s)
print('OK sisip packageManager pnpm@7.33.7 sebelum scripts')
print('verify pm=%d scripts=%d (hrs 1 1)'%(s.count('"packageManager"'),s.count('"scripts": {')))
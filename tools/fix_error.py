import re,sys,subprocess
P='src/helpers/error.ts'
print('===== ISI %s (lo liat konteksnya) ====='%P)
print(open(P,encoding='utf-8').read())
print('===== PATCH =====')
s=open(P,encoding='utf-8').read()
if re.search(r'export[^\n]*\buseToast\b', s):
    print('GUARD: useToast di-EXPORT dari error.ts -> file lain import dia, gue NOL patch buta. Paste list importernya.'); sys.exit(1)
s2=re.sub(r'(?m)^[ \t]*const useToast[ \t]*=[ \t]*toast\(\)[ \t]*;?[ \t]*\n','',s)
n=len(re.findall(r'\buseToast\b', s2))
s2=s2.replace('useToast.','toast().')
if re.search(r'\buseToast\b', s2):
    print('GUARD: masih ada useToast (bukan pola .x) -> paste, gue liat'); sys.exit(1)
if s2==s: print('SKIP idempotent'); sys.exit(0)
open(P,'w',encoding='utf-8',newline='\n').write(s2)
print('PATCH OK: hapus col-0 decl + ganti %d pemakaian useToast. -> toast().'%n)
print('--- git diff (LO LIAT, GUE BELUM COMMIT) ---')
print(subprocess.run(['git','diff','--',P],capture_output=True,text=True).stdout)

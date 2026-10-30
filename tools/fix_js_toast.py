import re,sys,subprocess,glob
files=glob.glob('src/**/*.js',recursive=True)
patched=[]
for P in files:
    s=open(P,encoding='utf-8').read()
    if not re.search(r'(?m)^[ \t]*const useToast[ \t]*=[ \t]*toast\(\)',s):
        continue
    if re.search(r'export[^\n]*\buseToast\b',s):
        print('GUARD: useToast di-EXPORT di %s -> paste cat %s'%(P,P)); sys.exit(1)
    s2=re.sub(r'(?m)^[ \t]*const useToast[ \t]*=[ \t]*toast\(\)[ \t]*;?[ \t]*\n','',s)
    s2=s2.replace('useToast.','toast().')
    if re.search(r'\buseToast\b',s2):
        print('GUARD: sisa useToast (bukan .x) di %s -> paste cat %s'%(P,P)); sys.exit(1)
    open(P,'w',encoding='utf-8',newline='\n').write(s2)
    patched.append(P)
    print('PATCH OK: %s'%P)
    print('--- git diff %s ---'%P)
    print(subprocess.run(['git','diff','--',P],capture_output=True,text=True).stdout)
print('TOTAL di-patch: %d -> %r'%(len(patched),patched) if patched else 'SKIP: NOL .js punya pola col-0')

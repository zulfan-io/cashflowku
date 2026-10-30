import re,sys,subprocess
P='src/pages/admin/dashboard.vue'
s=open(P,encoding='utf-8').read(); orig=s
if 'typeof document' not in s:
    s=s.replace("const modalCongrate = document.getElementById('modalPopup')","const modalCongrate = typeof document !== 'undefined' ? document.getElementById('modalPopup') : null")
    s=s.replace("modalCongrate.style.transform","modalCongrate && modalCongrate.style.transform")
    s=s.replace("modalCongrate.style.opacity","modalCongrate && modalCongrate.style.opacity")
    s=s.replace("modalCongrate.style.display","modalCongrate && modalCongrate.style.display")
if s==orig: print('SKIP idempotent')
else:
    open(P,'w',encoding='utf-8',newline='\n').write(s)
    print('PATCH OK dashboard.vue'); print(subprocess.run(['git','diff','--',P],capture_output=True,text=True).stdout)

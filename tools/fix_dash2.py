import re,sys,subprocess
P='src/pages/admin/dashboard.vue'
s=open(P,encoding='utf-8').read(); orig=s
if 'if (modalCongrate)' in s: print('SKIP idempotent'); sys.exit(0)
s=s.replace("const modalCongrate = document.getElementById('modalPopup')","const modalCongrate = typeof document !== 'undefined' ? document.getElementById('modalPopup') : null")
s=re.sub(r"(?m)^([ \t]*)modalCongrate\.style\.(\w+) = (.+)$", r"\1if (modalCongrate) modalCongrate.style.\2 = \3", s)
if s==orig: print('SKIP: pola NOL ketemu'); sys.exit(0)
open(P,'w',encoding='utf-8',newline='\n').write(s)
print('PATCH OK dashboard.vue'); print(subprocess.run(['git','diff','--',P],capture_output=True,text=True).stdout)

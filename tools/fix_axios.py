import re,sys,subprocess
P='src/services/axios-instance.js'
s=open(P,encoding='utf-8').read(); orig=s
if 'typeof localStorage' not in s:
    s=s.replace("const token = localStorage.getItem('token')","const token = typeof localStorage !== 'undefined' ? localStorage.getItem('token') : null")
if '(error?.response?.data?.message)' not in s:
    s=s.replace("error.response.data.message","(error?.response?.data?.message) ?? 'network'")
if '(error?.response?.statusText)' not in s:
    s=s.replace("error.response.statusText","(error?.response?.statusText) ?? 'request failed'")
if s==orig: print('SKIP idempotent')
else:
    open(P,'w',encoding='utf-8',newline='\n').write(s)
    print('PATCH OK axios-instance.js'); print(subprocess.run(['git','diff','--',P],capture_output=True,text=True).stdout)
print('===== dashboard.vue 70-95 (READ-ONLY) =====')
r=subprocess.run(['sed','-n','70,95p','src/pages/admin/dashboard.vue'],capture_output=True,text=True)
print(r.stdout or r.stderr)

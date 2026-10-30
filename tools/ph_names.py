import json,subprocess,sys
r=subprocess.run(['curl','-s','--max-time','25','https://api.iconify.design/ph.json'],capture_output=True,text=True)
if r.returncode!=0 or not r.stdout.strip(): sys.exit('CURL GAGAL = network lo mati, bukan nama')
d=json.loads(r.stdout)
names=list(d.get('icons',{}).keys())
print('TOTAL',len(names))
for kw in ['house','home','cart','basket','shop','grid','square','bell','notif','user','person','account','profile']:
    hits=[n for n in names if kw in n]
    print(kw,'->',hits[:10])

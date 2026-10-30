import json,subprocess,sys
def get(url):
    r=subprocess.run(['curl','-s','--max-time','25',url],capture_output=True,text=True)
    return r.returncode, r.stdout
rc,out=get('https://api.iconify.design/ph.json')
print('META rc=',rc,'len=',len(out))
if len(out)<10: sys.exit('META pendek = server nggak ngasih, bukan nama')
try: d=json.loads(out)
except Exception as e: sys.exit('META bukan JSON (%s) RAW[:120]=%r'%(e,out[:120]))
if not isinstance(d,dict): sys.exit('META type=%s RAW[:120]=%r'%(type(d).__name__,out[:120]))
ic=d.get('icons',{})
print('META top-keys=',list(d.keys())[:10],'| icons=',len(ic) if isinstance(ic,dict) else 'BUKAN dict')
if not isinstance(ic,dict) or not ic: sys.exit('META nggak punya dict icons -> RAW[:200]=%r'%out[:200])
names=list(ic.keys()); KW=['house','home','cart','basket','shop','grid','square','bell','notif','user','person','account','profile']; found={}
for kw in KW:
    hits=[n for n in names if kw in n]; found[kw]=hits; print(' ',kw,'->',hits[:8])
pick=None
for kw in ['house','home','cart','basket']:
    if found[kw]: pick=found[kw][0]; break
if not pick: sys.exit('NOL nama house/home/cart di metadata -> liat daftar di atas, Phosphor beda penamaan')
print('PROBE pakai nama VALID dari META:',pick)
rc2,o2=get('https://api.iconify.design/ph/%s.json'%pick)
print('  rc=',rc2,'len=',len(o2))
try:
    dd=json.loads(o2)
    if isinstance(dd,dict) and 'body' in dd: print('  BODY OK | currentColor?',('currentColor' in dd['body']),'| viewBox=',dd.get('viewBox'))
    else: print('  NOL-body keys=',list(dd.keys())[:5] if isinstance(dd,dict) else type(dd).__name__)
except Exception as e: print('  NON-JSON (%s) RAW[:120]=%r'%(e,o2[:120]))

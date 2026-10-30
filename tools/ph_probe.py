import json,subprocess,sys
def get(url):
    r=subprocess.run(['curl','-s','--compressed','--max-time','25',url],capture_output=True,text=True)
    return r.returncode, r.stdout
print('=== A: metadata /ph.json (liat struktur aslinya) ===')
rc,out=get('https://api.iconify.design/ph.json')
print('rc=',rc,'| len=',len(out))
print('RAW[:300]=',repr(out[:300]))
try:
    d=json.loads(out)
    print('TYPE parsed =',type(d).__name__)
    if isinstance(d,dict):
        print('KEYS =',list(d.keys())[:12])
        ic=d.get('icons',{})
        print('icons count =',len(ic) if isinstance(ic,dict) else 'BUKAN dict')
        if isinstance(ic,dict):
            for kw in ['house','home','cart','basket','grid','square','bell','user','person']:
                hits=[n for n in ic if kw in n]
                print(' ',kw,'->',hits[:8])
except Exception as e:
    print('json.loads GAGAL:',e,'-> body bukan JSON dict, liat RAW di atas')
print()
print('=== B: probe ikon langsung /ph/<nama>.json (yang kita butuhin = body) ===')
for n in ['house','house-fill','home','home-fill','shopping-cart','shopping-cart-fill','cart','cart-simple-fill','squares-four','squares-four-fill','grid','bell','bell-fill','user','user-fill','person','person-fill']:
    rc,o=get('https://api.iconify.design/ph/%s.json'%n)
    has='?'
    try:
        dd=json.loads(o)
        if isinstance(dd,dict) and 'body' in dd:
            has='OK' if 'currentColor' in dd['body'] else 'OK-tapi-BUKAN-currentColor'
        else:
            has='NOL-body keys=%s'%(list(dd.keys())[:4] if isinstance(dd,dict) else type(dd).__name__)
    except Exception:
        has='NON-JSON len=%d'%len(o)
    print('  %-22s %s'%(n,has))

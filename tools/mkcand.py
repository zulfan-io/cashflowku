import os,sys,re,json
IC='src/components/icons'; CD='src/data/cand.json'
files=sorted([f for f in os.listdir(IC) if f.endswith('.vue')])
if not files: sys.exit('FOLDER IKON KOSONG')
def body_of(fn):
    t=open(IC+'/'+fn,encoding='utf-8').read()
    m=re.search(r'<svg[\s\S]*?</svg>',t)
    if not m: return None
    s=m.group(0).replace('"',"'").replace('#','%23')
    return 'url("data:image/svg+xml,%s")'%re.sub(r'\s+',' ',s).strip()
cand=[]; skipped=[]
for fn in files:
    r=body_of(fn)
    if r is None:
        t=open(IC+'/'+fn,encoding='utf-8').read()
        skipped.append((fn,'<svg' in t,'</svg>' in t))
        continue
    cand.append({'num':len(cand)+1,'name':fn[:-4],'m':r})
if not cand: sys.exit('SEMUA rusak -> paste: head -3 src/components/icons/IShopee.vue')
cj=json.dumps(cand,ensure_ascii=True)
for ch in cj:
    if ord(ch)>127: sys.exit('MELESET non-ASCII cand.json')
json.loads(cj)
os.makedirs('src/data',exist_ok=True)
open(CD,'w',encoding='utf-8',newline='\n').write(cj+'\n')
print('OK cand.json: %d ikon (nomor 1..%d)'%(len(cand),len(cand)))
if skipped:
    print('SKIP %d rusak (TIDAK muncul di galeri, beresin nanti):'%len(skipped))
    for fn,o,c in skipped:
        print('  %s  <svg=%s  </svg=%s'%(fn,o,c))

import os,sys,re,json
SRC='src'; DOC='docs/trace_report.txt'
SKIP={'node_modules','.git','dist','.nuxt','.output'}
EXT=['.ts','.js','.vue','.tsx','.jsx','.mjs','.cjs','.json']
# alias: default ~/@ -> src. kalau vite.config lo beda, run ulang: --alias ~=src --alias @=src
ALIAS={'~':SRC,'@':SRC}
for a in sys.argv[1:]:
    if a.startswith('--alias') and '=' in a:
        k,v=a.split('=',1); ALIAS[k.lstrip('-').replace('alias','').strip('~@') or k]=v.strip()
def walk(root):
    out=[]
    for dp,dn,fn in os.walk(root):
        dn[:]=[d for d in dn if d not in SKIP]
        for f in fn:
            if f.endswith(('.ts','.js','.vue','.tsx','.jsx','.mjs','.cjs')): out.append(os.path.join(dp,f))
    return out
files=walk(SRC)+(['index.html'] if os.path.isfile('index.html') else [])+walk('tools') if os.path.isdir('tools') else walk(SRC)
files=[f for f in files if not f.endswith('.py')]
RE=re.compile(r'(?:import\s+(?:[\w*\s{},$]*\s+from\s+)?|export\s+(?:[\w*\s{},$]*\s+from\s+)|require\(\s*|import\(\s*)["\']([^"\']+)["\']')
def resolve(spec,frm):
    if spec.startswith('.'): base=os.path.normpath(os.path.join(os.path.dirname(frm),spec))
    else:
        pre=next((p for p in ALIAS if spec==p or spec.startswith(p+'/')),None)
        if not pre: return None,True
        base=os.path.normpath(os.path.join(ALIAS[pre],spec[len(pre):].lstrip('/')))
    for cand in [base]+[base+e for e in EXT]+[os.path.join(base,'index'+e) for e in EXT]:
        if os.path.isfile(cand): return cand,False
    return None,False
edges=[];nodes=set(files)
for f in files:
    try:s=open(f,encoding='utf-8',errors='replace').read()
    except:continue
    for m in RE.finditer(s):
        spec=m.group(1); to,ext=resolve(spec,f)
        kind='dynamic' if 'import(' in s[max(0,m.start()-8):m.start()+8] else ('require' if 'require(' in s[max(0,m.start()-8):m.start()+8] else 'import')
        edges.append({'frm':f,'spec':spec,'to':to,'ext':ext,'kind':kind})
incoming={n:0 for n in nodes}
broken=[];unres=[]
for e in edges:
    if e['ext']: continue
    if e['to'] is None: broken.append(e)
    else: incoming[e['to']]=incoming.get(e['to'],0)+1
ENTRY={f for f in nodes if f=='index.html' or re.search(r'src[/\\]main\.',f) or f.startswith('tools')}
yatim=[f for f in nodes if incoming.get(f,0)==0 and f not in ENTRY]
adj={}
for e in edges:
    if e['to']: adj.setdefault(e['frm'],[]).append(e['to'])
cycles=[];seen={}
def dfs(n,st):
    seen[n]=1;st.append(n)
    for m in adj.get(n,[]):
        if m in st: cycles.append(st[st.index(m):]+[m])
        elif seen.get(m)!=1: dfs(m,st)
    st.pop();seen[n]=2
for n in list(adj): 
    if seen.get(n)!=1: dfs(n,[])
L=[]
L.append('=== TRACE GRAPH (sambungan antar-file) ===')
L.append('nodes=%d edges_internal=%d broken=%d yatim=%d cycles=%d'%(len(nodes),sum(1 for e in edges if not e['ext'] and e['to']),len(broken),len(yatim),len(cycles)))
L.append('alias aktif: '+', '.join('%s->%s'%(k,v) for k,v in ALIAS.items())+'  (cek vite.config lo, beda? run --alias)')
L.append('--- [XX] PUTUS (import ke file yang TIDAK ADA) ---')
for e in broken[:30]: L.append('  %s -> %s  (%s)'%(e['frm'],e['spec'],e['kind']))
if len(broken)>30: L.append('  ... +%d lagi'%(len(broken)-30))
if not broken: L.append('  [OK] nihil')
L.append('--- [!!] YATIM (nggak di-import siapa-siapa, di luar entry) ---')
for f in yatim[:30]: L.append('  '+f)
if len(yatim)>30: L.append('  ... +%d lagi'%(len(yatim)-30))
if not yatim: L.append('  [OK] nihil')
L.append('--- [!!] SIKLUS (A->B->A, ranjau bundler) ---')
for c in cycles[:10]: L.append('  '+' -> '.join(c))
if not cycles: L.append('  [OK] nihil')
L.append('--- [??] EXTERNAL/UNRESOLVED (bare specifier, mungkin alias belum di-set) ---')
exts=sorted({e['spec'] for e in edges if e['ext']})[:40]
L.append('  '+', '.join(exts) if exts else '  [OK] nihil')
L.append('=== BATAS: trace ini STATIS. Dynamic-import-by-var, event-bus, provide/inject, pinia-cross-ref, python-tools TIDAK keliatan. ===')
rep='\n'.join(L)+'\n'
os.makedirs('docs',exist_ok=True); open(DOC,'w',encoding='utf-8').write(rep)
print(rep)
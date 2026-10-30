import os,sys,re,json
DU='src/pages/duality.vue'; CFG='src/data/icons.json'
if not os.path.isfile(DU): sys.exit('NGGAK ADA '+DU)
src=open(DU,encoding='utf-8').read()
try: CFGD=json.load(open(CFG,encoding='utf-8'))
except Exception as e: sys.exit('NGGAK BACA icons.json: %s'%e)
nb=CFGD.get('themes',{}).get('navbar-permen')
if not nb or 'icons' not in nb or len(nb['icons'])!=5: sys.exit('MELESET config navbar-permen NOL 5 slot')
idle=nb.get('idle','#9a9a9a')
# assert anchors SEBELUM nulis apa pun
A_SCRIPT='<script setup lang="ts">'
A_LABEL='>{{ t.label }}</button>'
A_STYLE='</style>'
for nm,a,c in (('script setup',A_SCRIPT,1),('label button',A_LABEL,1),('style close',A_STYLE,1)):
    n=src.count(a)
    if n!=c: sys.exit('MELESET anchor %s: ketemu %d, harus %d -> paste sed -n "1,90p" %s'%(nm,n,c,DU))
ids=re.findall(r"id:\s*['\"]([^'\"]+)['\"]",src)
WANT=['home','kat','game','notif','saya']
ids=[x for x in ids if x in WANT]
if ids!=WANT: sys.exit('MELESET id tabs (setelah filter): ketemu %s, harus %s -> paste line 70-80'%(ids,WANT))
MAPID={'home':'IHome','kat':'IShop','game':'IApplication','notif':'INotify','saya':'IAccount'}
slots=nb['icons']
CFGBI='{'
for i,mid in enumerate(WANT):
    s=slots[i]
    CFGBI+="'%s':{lite:'%s',base:'%s',m:%s},"%(mid,s['lite'],s['base'],json.dumps(s['m']))
CFGBI+='}'
IMPORTS='\n'.join("import %s from '~/components/icons/%s.vue'"%(MAPID[m],MAPID[m]) for m in WANT)
REG='const BI_REG = { '+', '.join(MAPID[m] for m in WANT)+' }'
INJECT='''
'''+IMPORTS+'''
'''+REG+'''
const BI_MAP: Record<string,string> = '''+json.dumps(MAPID)+'''
const BI_CFG: Record<string,{lite:string;base:string;m:string}> = '''+CFGBI+'''
const BI_IDLE = '''+json.dumps(idle)+'''
function biStyle(t: any) {
  const nm = BI_MAP[t.id]; const s = BI_CFG[t.id]
  if (!nm || !s) return {}
  const on = !!t.on
  return { '--m': s.m, '--lite': on ? s.lite : BI_IDLE, '--base': on ? s.base : BI_IDLE, color: on ? s.base : BI_IDLE }
}
'''
CSS='''
.bi { display: inline-flex; width: 24px; height: 24px; -webkit-mask: var(--m) center / contain no-repeat; mask: var(--m) center / contain no-repeat; background: linear-gradient(180deg, var(--lite), var(--base)); transition: transform .26s cubic-bezier(.34,1.56,.64,1), filter .22s, opacity .2s; }
.btab:not(.act) .bi { opacity: .55; }
.btab.act .bi { transform: translateY(-2px) scale(1.12); filter: drop-shadow(0 4px 8px currentColor); }
'''
out=src.replace(A_SCRIPT, A_SCRIPT+INJECT, 1)
out=out.replace(A_LABEL, '><span class="bi" :style="biStyle(t)"></span></button>', 1)
out=out.replace(A_STYLE, CSS+A_STYLE, 1)
# guard pasca-inject
for nm,a in (('biStyle call','biStyle(t)'),('.bi css','.bi {'),('mask css','-webkit-mask: var(--m)')):
    if a not in out: sys.exit('MELESET post-inject %s'%nm)
if out.count(A_SCRIPT)!=1 or out.count(A_STYLE)!=1: sys.exit('MELESET tag ganda pasca-inject')
for ch in out:
    if ord(ch)>127:
        i=out.index(ch); sys.exit('MELESET non-ASCII pos=%d char=%r konteks=%r'%(i,ch,out[max(0,i-20):i+20]))
if out.count('</template>')!=src.count('</template>'): sys.exit('MELESET template count berubah')
open(DU,'w',encoding='utf-8',newline='\n').write(out)
print('OK colok duality: navbar huruf->ikon 2-warna, id:', ids[:5], '| rumah zamrud ikut:', slots[0]['base'])

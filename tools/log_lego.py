import re,sys,subprocess,glob
# nemuin file legodone (anchor literal dari byte lo, kebukti)
cand=set()
for P in glob.glob('**/*.md',recursive=True)+glob.glob('**/legodone*',recursive=True):
    try: s=open(P,encoding='utf-8').read()
    except: continue
    if 'GUNUNG 3 SEO/SSR' in s and 'RINGKAS' in s: cand.add(P)
cand={p for p in cand if not p.startswith('node_modules')}
if len(cand)==0: print('GUARD: file legodone NOL ketemu -> paste: ls ~ ; echo $legodone'); sys.exit(1)
if len(cand)>1: print('GUARD: multi %r -> paste list'%sorted(cand)); sys.exit(1)
P=cand.pop(); s=open(P,encoding='utf-8').read()
# centang GUNUNG 3 (anchor literal, idempotent)
old='- ☐ GUNUNG 3 SEO/SSR'
new='- ☑ GUNUNG 3 SEO/SSR — HIJAU CF b6b2ad1 Node22 (716 file, .html ke-prerender, WebSocket kelar); 3 luka tersisa: VITE_BASE_DOMAIN kosong(undefined/api+errno-111), $/jQuery SSR dashboard'
if old in s: s=s.replace(old,new,1); print('CENTANG GUNUNG3: ☐->☑')
elif new.split('—')[0].strip() in s: print('CENTANG: SKIP udah ☑')
else: print('GUARD: anchor GUNUNG3 beda -> paste grep -n GUNUNG3 %s'%P); sys.exit(1)
# APPEND trace ngelog di bawah (aturan lo: pencapaian = peta = catet)
TRACE='''
## NGELÓG — trace pencapaian (dibawah legodone, rule Coi korporat)
- 2026-10-30 17:11 :: GUNUNG 3 SEO/SSR mendarat. CF build #0a0d9bc7 commit b6b2ad1 Node22.23.4 = Success (716 file, .html ke-prerender = SEO kebukti). Timeline tembok yang diruntuhin 90 ronde: swiper(CJS) -> workbox-window(CJS) -> noExternal true(collateral @vue/server-renderer node:stream) -> list manual[swiper,workbox] -> pinia _s(useToast col-0 axios-instance.js, 85 ronde buta .js) -> axios localStorage+error.response(reading data) -> dashboard document($ is not defined, jQuery) -> supabase WebSocket(Node20->22). 3 luka tersisa: env VITE_BASE_DOMAIN kosong, $/jQuery SSR, API builder-block(errno-111 akibat env). vite-ssg 0.17 NOL fail-fast = hijau tapi setengah halaman kosong.
'''
if 'NGELÓG — trace' not in s: s=s.rstrip()+TRACE; print('APPEND trace ngelog: +')
else: print('APPEND: SKIP trace udah ada')
open(P,'w',encoding='utf-8',newline='\n').write(s)
print('FILE: %s'%P)
print('--- git diff -- %s ---'%P)
print(subprocess.run(['git','diff','--',P],capture_output=True,text=True).stdout)

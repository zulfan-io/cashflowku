import os,sys,subprocess
P='LEGODONE.md'
if not os.path.exists(P): print('GUARD: %s NOL ada -> cwd lo di repo?'%P); sys.exit(1)
s=open(P,encoding='utf-8').read()
if 'NGELÓG — trace' in s: print('SKIP idempotent: trace udah ada'); sys.exit(0)
TRACE="""

## NGELÓG — trace pencapaian (dibawah legodone, rule Coi korporat)
- 2026-10-30 17:11 :: GUNUNG 3 SEO/SSR mendarat. CF build #0a0d9bc7 commit b6b2ad1 Node22.23.4 = Success (716 file, .html ke-prerender = SEO kebukti). Timeline tembok yang diruntuhin 90 ronde: swiper(CJS) -> workbox-window(CJS) -> noExternal true(collateral @vue/server-renderer node:stream) -> list manual[swiper,workbox] -> pinia _s(useToast col-0 axios-instance.js, 85 ronde buta .js) -> axios localStorage+error.response(reading data) -> dashboard document($ is not defined, jQuery) -> supabase WebSocket(Node20->22). 3 luka tersisa: env VITE_BASE_DOMAIN kosong, $/jQuery SSR, API builder-block(errno-111 akibat env). vite-ssg 0.17 NOL fail-fast = hijau tapi setengah halaman kosong."""
open(P,'w',encoding='utf-8',newline='\n').write(s.rstrip()+TRACE+'\n')
print('APPEND OK: trace masuk %s'%P)
print('--- git diff -- %s ---'%P)
print(subprocess.run(['git','diff','--',P],capture_output=True,text=True).stdout)

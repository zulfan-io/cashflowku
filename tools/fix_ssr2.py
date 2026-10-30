import re,sys
NL=chr(10)
def rw(P,s): open(P,'w',encoding='utf-8',newline=NL).write(s)
# --- modules/pinia.ts: aktifin pinia global ---
P='src/modules/pinia.ts'; s=open(P,encoding='utf-8').read()
if 'setActivePinia' not in s:
    s=s.replace("import { createPinia } from 'pinia'","import { createPinia, setActivePinia } from 'pinia'")
    s=s.replace("  const pinia = createPinia()","  const pinia = createPinia()"+NL+"  setActivePinia(pinia)")
    rw(P,s); print('pinia.ts: setActivePinia +')
else: print('pinia.ts: SKIP udah ada')
# --- App.vue: window listener masuk onMounted ---
P='src/App.vue'; s=open(P,encoding='utf-8').read()
if "window.addEventListener('scroll', scrollFunction)" in s and 'onMounted(() => {' in s:
    s=s.replace("window.addEventListener('scroll', scrollFunction)"+NL,"")  # buang top-level
    # sisipin ke dalem onMounted pertama
    s=s.replace("onMounted(() => {","onMounted(() => {"+NL+"  window.addEventListener('scroll', scrollFunction)",1)
    rw(P,s); print('App.vue: window listener dipindah ke onMounted +')
else: print('App.vue: SKIP (udah dibenerin / anchor beda)')

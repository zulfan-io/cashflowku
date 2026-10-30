import os,sys
CN='src/components/CNav.vue'; PV='src/pages/candy-preview.vue'
for f in (CN,PV):
    if os.path.isfile(f):
        ex=open(f,encoding='utf-8').read()
        if 'cnav' in ex or 'cnav3' in ex: sys.exit('udah cnav, skip')
        sys.exit('ABORT '+f+' ada bukan buatan gue')
NC='''<!-- cnav -->
<script setup lang="ts">
import { ref } from 'vue'
import IHome from '~/components/icons/IHome.vue'
import ICart from '~/components/icons/ICart.vue'
import IApplication from '~/components/icons/IApplication.vue'
import INotify from '~/components/icons/INotify.vue'
import IAccount from '~/components/icons/IAccount.vue'
const tabs = [
  { id: 'home', c: '#FF6A2B', I: IHome },
  { id: 'kat', c: '#2F6BFF', I: ICart },
  { id: 'game', c: '#7C4DFF', I: IApplication },
  { id: 'notif', c: '#FFB300', I: INotify },
  { id: 'saya', c: '#00B894', I: IAccount },
]
const on = ref('home')
</script>

<template>
  <nav class="cnav">
    <button v-for="t in tabs" :key="t.id" class="ctab" :class="{ on: on === t.id }" :style="{ color: t.c }" @click="on = t.id">
      <component :is="t.I" class="ic" />
    </button>
  </nav>
</template>

<style scoped>
.cnav { position: fixed; left: 0; right: 0; bottom: 0; max-width: 480px; margin: 0 auto; display: flex; justify-content: space-around; background: #fff; border-top: 1px solid #eee; padding: 8px 4px calc(8px + env(safe-area-inset-bottom)); z-index: 5; }
.ctab { flex: 1; border: 0; background: transparent; cursor: pointer; display: flex; align-items: center; justify-content: center; padding: 6px 0; perspective: 500px; }
.ic { font-size: 24px; display: block; transform: rotateX(14deg); opacity: .62; filter: drop-shadow(0 2px 2px rgba(0,0,0,.12)); transition: transform .28s cubic-bezier(.34,1.56,.64,1), opacity .2s, filter .2s; }
.ctab.on .ic { transform: rotateX(0) translateY(-3px) scale(1.12); opacity: 1; filter: drop-shadow(0 4px 6px rgba(0,0,0,.22)); animation: pop .34s cubic-bezier(.34,1.56,.64,1); }
@keyframes pop { 0% { transform: rotateX(0) translateY(-3px) scale(1); } 55% { transform: rotateX(0) translateY(-6px) scale(1.2); } 100% { transform: rotateX(0) translateY(-3px) scale(1.12); } }
</style>
'''
PC='''<!-- cnav3 -->
<script setup lang="ts">
import CNav from '~/components/CNav.vue'
import IHome from '~/components/icons/IHome.vue'
import ICart from '~/components/icons/ICart.vue'
import IApplication from '~/components/icons/IApplication.vue'
import INotify from '~/components/icons/INotify.vue'
import IAccount from '~/components/icons/IAccount.vue'
const big = [IHome, ICart, IApplication, INotify, IAccount]
const cols = ['#FF6A2B', '#2F6BFF', '#7C4DFF', '#FFB300', '#00B894']
</script>

<template>
  <div class="cv">
    <div class="cv-note">CNav v3 - ikon desainer dari repo lo, bukan gambar buta. Ikon saja NOL label. 2.5D: idle miring, tap = tegak + bounce sekali. GAME = IApplication sementara.</div>
    <div class="cv-row">
      <span v-for="(b, i) in big" :key="i" class="big" :style="{ color: cols[i] }"><component :is="b" /></span>
    </div>
    <CNav />
  </div>
</template>

<style scoped>
.cv { max-width: 480px; margin: 0 auto; padding: 24px 16px 120px; font-family: system-ui, sans-serif; color: #1a1a1a; background: #f7f7f7; min-height: 100vh; }
.cv-note { font-size: 12px; color: #888; line-height: 1.5; margin-bottom: 16px; }
.cv-row { display: flex; gap: 18px; justify-content: center; padding: 18px; background: #fff; border: 1px solid #eee; border-radius: 14px; }
.big { font-size: 34px; display: inline-flex; }
</style>
'''
errs=[]
for f,C,mk in ((CN,NC,['cnav','IHome from','<component :is','rotateX','@keyframes pop','perspective']),(PV,PC,['cnav3','CNav from','component :is','cv-row'])):
    for ch in C:
        if ord(ch)>127: errs.append('non-ASCII '+f); break
    if '<script setup lang="ts">' not in C: errs.append('lang=ts hilang '+f)
    for m in mk:
        if m not in C: errs.append('marker '+m+' hilang '+f)
    if C.count('</template>')!=1 or C.count('</style>')!=1: errs.append('tag tutup '+f)
if errs:
    print('[MELESET] TIDAK ditulis (file utuh):'); [print('  ',e) for e in errs]; sys.exit(1)
open(CN,'w',encoding='utf-8',newline='\n').write(NC)
open(PV,'w',encoding='utf-8',newline='\n').write(PC)
print('OK CNav pakai ikon repo + preview v3', CN, PV)

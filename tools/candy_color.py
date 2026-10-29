import os,sys
CI='src/components/CIcon.vue'; PV='src/pages/candy-preview.vue'
for f in (CI,PV):
    if not os.path.isfile(f): sys.exit('NGGAK ADA '+f)
IC='''<!-- candy2 -->
<script setup lang="ts">
import { computed } from 'vue'
const props = defineProps<{ name: string; active?: boolean; size?: number }>()
const s = computed(() => props.size || 26)
const gid = computed(() => 'cg2-' + props.name)
const PAL: Record<string, [string, string]> = {
  home: ['#FFA06E', '#FF6A2B'],
  cart: ['#6FA0FF', '#2F6BFF'],
  game: ['#A98BFF', '#7C4DFF'],
  bell: ['#FFD27A', '#FFB300'],
  user: ['#5FE0C0', '#00B894'],
}
const P: Record<string, string> = {
  home: 'M12 3 L3 11 v9 a1 1 0 0 0 1 1 h5 v-6 h4 v6 h5 a1 1 0 0 0 1-1 v-9 Z',
  cart: 'M5 6 h2 l2.2 9.2 a2 2 0 0 0 2 1.6 h7.2 a2 2 0 0 0 2-1.6 L22 8 H8 M10 20 a1 1 0 1 0 0-2 a1 1 0 0 0 0 2 M18 20 a1 1 0 1 0 0-2 a1 1 0 0 0 0 2',
  game: 'M7 9 h10 a4 4 0 0 1 4 4 v2 a3 3 0 0 1-3 3 l-2-2 h-8 l-2 2 a3 3 0 0 1-3-3 v-2 a4 4 0 0 1 4-4 Z M8 12 v3 M6.5 13.5 h3 M15 12.5 h1.5 M17 14 h1.5',
  bell: 'M12 4 a5 5 0 0 1 5 5 v3 l1.5 2.5 H5.5 L7 12 V9 a5 5 0 0 1 5-5 Z M10.5 17 a1.5 1.5 0 0 0 3 0',
  user: 'M12 4 a3.5 3.5 0 1 1 0 7 a3.5 3.5 0 0 1 0-7 Z M5.5 20 a6.5 6.5 0 0 1 13 0 Z',
}
const base = computed(() => (PAL[props.name] || PAL.home)[1])
const lite = computed(() => (PAL[props.name] || PAL.home)[0])
</script>

<template>
  <svg class="ci" :class="{ act: active }" :width="s" :height="s" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient :id="gid" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" :stop-color="lite"/>
        <stop offset="1" :stop-color="base"/>
      </linearGradient>
    </defs>
    <path :d="P[name] || P.home" :fill="'url(#' + gid + ')'" :stroke="base" stroke-width="1.3" stroke-linejoin="round" stroke-linecap="round"/>
    <ellipse cx="9.5" cy="8" rx="2.4" ry="1.4" fill="#ffffff" opacity="0.55"/>
  </svg>
</template>

<style scoped>
.ci { display: block; filter: drop-shadow(0 2px 3px rgba(0,0,0,.18)); transition: filter .15s, transform .15s; }
.ci.act { filter: drop-shadow(0 3px 6px rgba(0,0,0,.28)); transform: translateY(-1px) scale(1.06); }
</style>
'''
PC='''<!-- candy2 -->
<script setup lang="ts">
import CIcon from '~/components/CIcon.vue'
const tabs = [['home','HOME'],['cart','KAT'],['game','GAME'],['bell','NOTIF'],['user','SAYA']]
</script>

<template>
  <div class="cv">
    <div class="cv-note">Candy v2 - tiap permen beda warna (level Shopee/Trip). Bukan 3D Tiket; untuk 3D pakai JPG lo (Jalur B). Navbar tiruan, belum dicolok ke duality.</div>
    <nav class="cnav">
      <button v-for="(t, i) in tabs" :key="t[0]" class="ctab" :class="{ on: i === 0 }">
        <CIcon :name="t[0]" :active="i === 0" :size="26" />
      </button>
    </nav>
    <div class="cv-row">
      <CIcon v-for="t in tabs" :key="t[0]" :name="t[0]" :size="34" />
    </div>
  </div>
</template>

<style scoped>
.cv { max-width: 480px; margin: 0 auto; padding: 24px 16px 120px; font-family: system-ui, sans-serif; color: #1a1a1a; background: #f7f7f7; min-height: 100vh; }
.cv-note { font-size: 12px; color: #888; line-height: 1.5; margin-bottom: 16px; }
.cnav { position: fixed; left: 0; right: 0; bottom: 0; max-width: 480px; margin: 0 auto; display: flex; justify-content: space-around; background: #fff; border-top: 1px solid #eee; padding: 8px 4px calc(8px + env(safe-area-inset-bottom)); z-index: 5; }
.ctab { flex: 1; border: 0; background: transparent; cursor: pointer; padding: 4px 0; display: flex; justify-content: center; }
.ctab :deep(.ci) { filter: grayscale(1) opacity(.4); }
.ctab.on :deep(.ci) { filter: drop-shadow(0 3px 6px rgba(0,0,0,.28)); }
.cv-row { display: flex; gap: 18px; justify-content: center; margin-top: 24px; padding: 16px; background: #fff; border: 1px solid #eee; border-radius: 14px; }
</style>
'''
errs=[]
for f,C,mk in ((CI,IC,['candy2','PAL','linearGradient','drop-shadow','url(#','P.home']),(PV,PC,['candy2','CIcon from','cnav','cv-row'])):
    for ch in C:
        if ord(ch)>127: errs.append('non-ASCII '+f); break
    if '<script setup lang="ts">' not in C: errs.append('lang=ts hilang '+f)
    for m in mk:
        if m not in C: errs.append('marker '+m+' hilang '+f)
    if C.count('</template>')!=1 or C.count('</style>')!=1: errs.append('tag tutup '+f)
if errs:
    print('[MELESET] TIDAK ditulis (file utuh):'); [print('  ',e) for e in errs]; sys.exit(1)
open(CI,'w',encoding='utf-8',newline='\n').write(IC)
open(PV,'w',encoding='utf-8',newline='\n').write(PC)
print('OK candy2 multi-warna (Jalur A)', CI, PV)

import os,sys
CI='src/components/CIcon.vue'; PV='src/pages/candy-preview.vue'
for f in (CI,PV):
    if os.path.isfile(f):
        ex=open(f,encoding='utf-8').read()
        if 'candy' in ex: sys.exit('udah candy, skip')
        sys.exit('ABORT '+f+' udah ada bukan buatan gue')
IC='''<!-- candy -->
<script setup lang="ts">
import { computed } from 'vue'
const props = defineProps<{ name: string; active?: boolean; size?: number }>()
const s = computed(() => props.size || 26)
const gid = computed(() => 'cg-' + props.name)
const P: Record<string, string> = {
  home: 'M12 3 L3 11 v9 a1 1 0 0 0 1 1 h5 v-6 h4 v6 h5 a1 1 0 0 0 1-1 v-9 Z',
  cart: 'M6 7 h13 l-1.6 8.2 a2 2 0 0 1-2 1.8 H9.6 a2 2 0 0 1-2-1.8 L6 7 Z M9 7 V5.5 a3 3 0 0 1 6 0 V7',
  game: 'M7 9 h10 a4 4 0 0 1 4 4 v2 a3 3 0 0 1-3 3 l-2-2 h-8 l-2 2 a3 3 0 0 1-3-3 v-2 a4 4 0 0 1 4-4 Z',
  bell: 'M12 4 a5 5 0 0 1 5 5 v3 l1.5 2.5 H5.5 L7 12 V9 a5 5 0 0 1 5-5 Z M10.5 17 a1.5 1.5 0 0 0 3 0',
  user: 'M12 4 a3.5 3.5 0 1 1 0 7 a3.5 3.5 0 0 1 0-7 Z M5.5 20 a6.5 6.5 0 0 1 13 0 Z',
}
</script>

<template>
  <svg class="ci" :class="{ act: active }" :width="s" :height="s" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient :id="gid" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stop-color="#FFA06E"/>
        <stop offset="1" stop-color="#FF7A45"/>
      </linearGradient>
    </defs>
    <path :d="P[name] || P.home" :fill="'url(#' + gid + ')'" stroke="#FF7A45" stroke-width="1.4" stroke-linejoin="round" stroke-linecap="round"/>
    <ellipse cx="9.5" cy="8" rx="2.4" ry="1.4" fill="#ffffff" opacity="0.5"/>
  </svg>
</template>

<style scoped>
.ci { display: block; filter: drop-shadow(0 2px 3px rgba(255,122,69,.28)); transition: filter .15s, transform .15s; }
.ci.act { filter: drop-shadow(0 3px 6px rgba(255,122,69,.5)); transform: translateY(-1px) scale(1.06); }
</style>
'''
PC='''<!-- candy -->
<script setup lang="ts">
import CIcon from '~/components/CIcon.vue'
const tabs = [['home','HOME'],['cart','KAT'],['game','GAME'],['bell','NOTIF'],['user','SAYA']]
</script>

<template>
  <div class="cv">
    <div class="cv-note">Candy preview - navbar tiruan, belum dicolok ke duality. Yang aktif = coral mengkilap + ngambang. Yang inactive = abu.</div>
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
.ctab :deep(.ci) { filter: grayscale(1) opacity(.45); }
.ctab.on :deep(.ci) { filter: drop-shadow(0 3px 6px rgba(255,122,69,.5)); }
.cv-row { display: flex; gap: 18px; justify-content: center; margin-top: 24px; padding: 16px; background: #fff; border: 1px solid #eee; border-radius: 14px; }
</style>
'''
errs=[]
for f,C,mk in ((CI,IC,['candy','linearGradient','drop-shadow','url(#','P.home']),(PV,PC,['candy','CIcon from','cnav','cv-row'])):
    for ch in C:
        if ord(ch)>127: errs.append('non-ASCII '+f); break
    if '<script setup lang="ts">' not in C: errs.append('lang=ts hilang '+f)
    for m in mk:
        if m not in C: errs.append('marker '+m+' hilang '+f)
    if C.count('</template>')!=1 or C.count('</style>')!=1: errs.append('tag tutup '+f)
if errs:
    print('[MELESET] TIDAK ditulis:'); [print('  ',e) for e in errs]; sys.exit(1)
open(CI,'w',encoding='utf-8',newline='\n').write(IC)
open(PV,'w',encoding='utf-8',newline='\n').write(PC)
print('OK candy: CIcon filled+gradient+shadow + preview', CI, PV)

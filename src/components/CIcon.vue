<!-- candy2 -->
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

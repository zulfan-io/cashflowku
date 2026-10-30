<!-- tw-grad -->
<script setup lang="ts">
import { ref } from 'vue'
import cfg from '~/data/icons.json'

const REG = { 'IHome': IHome, 'IShop': IShop, 'IApplication': IApplication, 'INotify': INotify, 'IAccount': IAccount, 'IStar': IStar, 'IHeart': IHeart, 'IBasket': IBasket, 'ITime': ITime }
function comp(name: string) { return REG[name] || null }
const themes = (cfg as any).themes as Record<string, any>
const act = ref<Record<string, number>>(Object.fromEntries(Object.keys(themes).map((k) => [k, 2])))
</script>

<template>
  <div class="tw">
    <div class="tw-note">2-WARNA via mask (gradient di BADAN ikon, BUKAN 3D). TEKEN = aktif (2-tone + glow + naik), lain = DIAM (abu flat). Warna = lite/base di icons.json, ganti 1 baris hex = ganti rasa.</div>
    <div v-for="(t, tn) in themes" :key="tn" class="tw-card">
      <div class="tw-head"><span class="tw-name">{{ tn }}</span><span class="tw-desc">{{ t.desc }} - teken ganti aktif</span></div>
      <div class="tw-row">
        <button v-for="(ic, ii) in t.icons" :key="ii" class="tw-ic" :class="{ on: act[tn] === ii }"
          :style="{ '--m': ic.m, '--lite': act[tn] === ii ? ic.lite : t.idle, '--base': act[tn] === ii ? ic.base : t.idle, color: act[tn] === ii ? ic.base : t.idle }"
          @click="act[tn] = ii"></button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.tw { max-width: 480px; margin: 0 auto; padding: 24px 16px 80px; font-family: system-ui, sans-serif; color: #1a1a1a; background: #f7f7f7; min-height: 100vh; }
.tw-note { font-size: 12px; color: #888; line-height: 1.5; margin-bottom: 16px; }
.tw-card { background: #fff; border: 1px solid #eee; border-radius: 14px; padding: 14px 16px 18px; margin-bottom: 14px; }
.tw-head { display: flex; flex-direction: column; margin-bottom: 12px; }
.tw-name { font-size: 13px; font-weight: 700; color: #333; }
.tw-desc { font-size: 11px; color: #aaa; }
.tw-row { display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; }
.tw-ic { border: 0; background: transparent; cursor: pointer; width: 30px; height: 30px; padding: 0; display: inline-flex; -webkit-mask: var(--m) center / contain no-repeat; mask: var(--m) center / contain no-repeat; background: linear-gradient(180deg, var(--lite), var(--base)); transition: transform .26s cubic-bezier(.34,1.56,.64,1), filter .22s, opacity .2s; }
.tw-ic:not(.on) { opacity: .55; }
.tw-ic.on { transform: translateY(-3px) scale(1.16); filter: drop-shadow(0 5px 10px currentColor); }
</style>

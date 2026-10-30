<!-- tuas -->
<script setup lang="ts">
import cfg from '~/data/icons.json'
import IHome from '~/components/icons/IHome.vue'
import IShop from '~/components/icons/IShop.vue'
import IApplication from '~/components/icons/IApplication.vue'
import INotify from '~/components/icons/INotify.vue'
import IAccount from '~/components/icons/IAccount.vue'
import IStar from '~/components/icons/IStar.vue'
import IHeart from '~/components/icons/IHeart.vue'
import IBasket from '~/components/icons/IBasket.vue'
import ITime from '~/components/icons/ITime.vue'
const REG = { 'IHome': IHome, 'IShop': IShop, 'IApplication': IApplication, 'INotify': INotify, 'IAccount': IAccount, 'IStar': IStar, 'IHeart': IHeart, 'IBasket': IBasket, 'ITime': ITime }
function resolve(name: string) { return REG[name] || null }
const themes = (cfg as any).themes as Record<string, any>
</script>

<template>
  <div class="tw">
    <div class="tw-note">TUAS (import eksplisit, NOL glob/auto-import). Tiap blok = 1 tema dari icons.json. Tengah = DIPILIH (naik+nyala), lain = DIAM (abu). Merah = nama di config NOL ada file (cek menu waiter).</div>
    <div v-for="(t, tn) in themes" :key="tn" class="tw-card">
      <div class="tw-head"><span class="tw-name">{{ tn }}</span><span class="tw-desc">{{ t.desc }}</span></div>
      <div class="tw-row">
        <span v-for="(ic, ii) in t.icons" :key="ii" class="tw-ic" :class="{ on: ii === 2 }" :style="ii === 2 ? { color: t.palette[ii] } : { color: t.idle }">
          <component :is="resolve(ic)" v-if="resolve(ic)" />
          <em v-else class="tw-miss">{{ ic }}</em>
        </span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.tw { max-width: 480px; margin: 0 auto; padding: 24px 16px 80px; font-family: system-ui, sans-serif; color: #1a1a1a; background: #f7f7f7; min-height: 100vh; }
.tw-note { font-size: 12px; color: #888; line-height: 1.5; margin-bottom: 16px; }
.tw-card { background: #fff; border: 1px solid #eee; border-radius: 14px; padding: 14px 16px 18px; margin-bottom: 14px; }
.tw-head { display: flex; flex-direction: column; margin-bottom: 10px; }
.tw-name { font-size: 13px; font-weight: 700; color: #333; }
.tw-desc { font-size: 11px; color: #aaa; }
.tw-row { display: flex; gap: 22px; justify-content: center; }
.tw-ic { font-size: 30px; display: inline-flex; transition: transform .25s cubic-bezier(.34,1.56,.64,1), filter .2s, opacity .2s; }
.tw-ic.on { transform: translateY(-3px) scale(1.14); filter: drop-shadow(0 4px 7px rgba(0,0,0,.22)); }
.tw-miss { font-size: 10px; color: #e11d48; font-style: normal; }
</style>

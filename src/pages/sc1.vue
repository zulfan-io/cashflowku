<!-- sc-page -->
<script setup lang="ts">
import StoryCircle from '~/components/StoryCircle.vue'
import Dots from '~/components/Dots.vue'
import NotifDot from '~/components/NotifDot.vue'
import { ref } from 'vue'
const faces = ['A','B','C','D','E','F','G']
const posts = [
 { who:'Rani', ago:'2j', body:'nemu hoodies lokal murah, check', img:'https://picsum.photos/seed/sc1p1/600/600', love:12, share:3, imgs:3 },
 { who:'Dito', ago:'5j', body:'celana kargo ini gila sih', img:'https://picsum.photos/seed/sc1p2/600/600', love:40, share:9, imgs:1 },
]
const nav = ['H','S','+','L','M']
const open = ref(null)
</script>
<template>
  <div class="sc1">
    <header class="bar"><span class="brand">shoper</span><span class="bic">S<span class="brel"><NotifDot :on="true" /></span></span></header>
    <div class="rail">
      <StoryCircle v-for="(f,i) in faces" :key="f" :label="f" :src="'https://picsum.photos/seed/sc1f-'+f+'/120/120'" :read="i<2" :size="58" @open="open=f" />
    </div>
    <article v-for="(p,pi) in posts" :key="pi" class="post">
      <div class="ph"><StoryCircle :label="p.who[0]" :src="'https://picsum.photos/seed/sc1a-'+p.who+'/80/80'" :size="34" @open="open=p.who" /><div class="who"><b>{{ p.who }}</b><i>{{ p.ago }}</i></div></div>
      <p class="txt">{{ p.body }}</p>
      <div class="shot"><img :src="p.img" alt="" /><Dots v-if="p.imgs>1" :count="p.imgs" :active="0" /></div>
      <div class="act"><button>&#9825; {{ p.love }}</button><button>&#8618; {{ p.share }}</button></div>
    </article>
    <nav class="bnav"><button v-for="(n,ni) in nav" :key="ni" class="bn" :class="{on:ni===0}">{{ n }}<NotifDot v-if="ni===3" :on="true" /></button></nav>
    <div v-if="open" class="ov" @click="open=null"><img class="ovi" :src="'https://picsum.photos/seed/sc1s-'+open+'/600/900'" alt="" /><div class="ovt">{{ open }} &#183; story 24 jam (viewer penuh = gelombang C)</div></div>
  </div>
</template>
<style scoped>
.sc1 { max-width: 480px; margin: 0 auto; padding: 0 0 64px; font-family: system-ui, sans-serif; color: #1a1a1a; background: #f7f7f7; min-height: 100vh; }
.bar { display: flex; align-items: center; justify-content: space-between; padding: 12px 16px; border-bottom: 1px solid #eee; }
.brand { font-weight: 800; color: #FF7A45; font-size: 18px; }
.bic { position: relative; font-weight: 800; color: #888; }
.brel { position: absolute; top: -4px; right: -8px; }
.rail { display: flex; gap: 10px; overflow-x: auto; padding: 12px 16px; scrollbar-width: none; }
.rail::-webkit-scrollbar { display: none; }
.post { background: #fff; border-top: 1px solid #eee; border-bottom: 1px solid #eee; padding: 10px 16px 12px; }
.ph { display: flex; align-items: center; gap: 8px; }
.who b { font-size: 13px; display: block; }
.who i { font-size: 11px; color: #999; font-style: normal; }
.txt { font-size: 13px; margin: 8px 0; line-height: 1.4; }
.shot { position: relative; border-radius: 10px; overflow: hidden; }
.shot img { width: 100%; display: block; aspect-ratio: 1/1; object-fit: cover; }
.shot .dt-row, .shot > *:last-child { position: absolute; bottom: 8px; left: 0; right: 0; }
.act { display: flex; gap: 14px; margin-top: 8px; }
.act button { border: 0; background: transparent; font-size: 13px; color: #555; cursor: pointer; padding: 2px 0; }
.bnav { position: fixed; left: 0; right: 0; bottom: 0; display: flex; justify-content: space-around; background: #fff; border-top: 1px solid #eee; padding: 8px 4px calc(8px + env(safe-area-inset-bottom)); z-index: 5; }
.bn { position: relative; border: 0; background: transparent; font-size: 18px; font-weight: 800; color: #bbb; cursor: pointer; padding: 2px 10px; }
.bn.on { color: #FF7A45; }
.ov { position: fixed; inset: 0; background: rgba(0,0,0,.92); z-index: 20; display: flex; flex-direction: column; align-items: center; justify-content: center; }
.ovi { width: 100%; max-width: 480px; height: 100%; object-fit: cover; }
.ovt { position: absolute; bottom: 24px; color: #fff; font-size: 12px; }
</style>

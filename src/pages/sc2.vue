<!-- sc-page -->
<script setup lang="ts">
import StoryCircle from '~/components/StoryCircle.vue'
import Dots from '~/components/Dots.vue'
import NotifDot from '~/components/NotifDot.vue'
import { ref, onMounted } from 'vue'
import { supabase } from '~/utils/supabase'
function mapOffer(o) {
  const price = o.price != null ? Number(o.price) : null
  return { id: o.id, name: o.title || 'Produk', seller: 'Toko ' + (o.brand || 'Shoper'), price, love: 0, share: 0, imgs: 1 }
}
const prods = ref([])
const nav = [['H','HOME'],['S','KAT'],['+','GAME'],['L','NOTIF'],['M','SAYA']]
const open = ref(null)
onMounted(async () => {
  try {
    const { data, error } = await supabase.from('shoper_offers').select('*').eq('active', true).limit(8)
    if (!error && data && data.length) prods.value = data.map(mapOffer)
    else prods.value = dummy()
  } catch (e) { prods.value = dummy() }
})
function dummy() {
  const d = [[1,'Kemeja Flanel Oversize',89000,2],[2,'Celana Kargo Dewasa',120000,1],[3,'Hoodie Fleece Premium',135000,3],[4,'Sepatu Sneakers Retro',199000,1]]
  return d.map(x => ({ id:x[0], name:x[1], seller:'Toko Rani', price:x[2], love:50+x[0], share:x[0], imgs:x[3] }))
}
</script>
<template>
  <div class="sc2">
    <header class="bar"><span class="brand">shoper</span><span class="bic">S<span class="brel"><NotifDot :on="true" /></span></span></header>
    <main class="grid">
      <article v-for="p in prods" :key="p.id" class="pc">
        <div class="pimg"><img :src="'https://picsum.photos/seed/sc2p-'+p.id+'/400/400'" alt="" /><span v-if="p.imgs>1" class="pg">1/{{ p.imgs }}</span></div>
        <div class="pbd">
          <div class="sel"><StoryCircle :label="p.seller[0]" :src="'https://picsum.photos/seed/sc2s-'+p.seller+'/80/80'" :size="24" @open="open=p.seller" /><span>{{ p.seller }}</span></div>
          <h3>{{ p.name }}</h3>
          <p class="pr">Rp{{ (p.price||0).toLocaleString('id-ID') }}</p>
          <div class="act"><button>&#9825; {{ p.love }}</button><button>&#8618; {{ p.share }}</button></div>
        </div>
      </article>
    </main>
    <nav class="bnav"><button v-for="(n,ni) in nav" :key="ni" class="bn" :class="{on:ni===0}"><span class="bi">{{ n[0] }}<NotifDot v-if="ni===3" :on="true" /></span><span class="bl">{{ n[1] }}</span></button></nav>
    <div v-if="open" class="ov" @click="open=null"><img class="ovi" :src="'https://picsum.photos/seed/sc2s-'+open+'/600/900'" alt="" /><div class="ovt">{{ open }} &#183; story 24 jam (viewer penuh = gelombang C)</div></div>
  </div>
</template>
<style scoped>
.sc2 { max-width: 1280px; margin: 0 auto; padding: 0 0 72px; font-family: system-ui, sans-serif; color: #1a1a1a; background: #f7f7f7; min-height: 100vh; }
.bar { display: flex; align-items: center; justify-content: space-between; padding: 12px 16px; border-bottom: 1px solid #eee; }
.brand { font-weight: 800; color: #FF7A45; font-size: 18px; }
.bic { position: relative; font-weight: 800; color: #888; }
.brel { position: absolute; top: -4px; right: -8px; }
.grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; padding: 12px 10px; }
@media (min-width: 640px) { .grid { grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); } }
.pc { background: #fff; border: 1px solid #eee; border-radius: 12px; overflow: hidden; }
.pimg { position: relative; aspect-ratio: 1/1; }
.pimg img { width: 100%; height: 100%; object-fit: cover; display: block; }
.pg { position: absolute; top: 6px; right: 6px; background: rgba(0,0,0,.6); color: #fff; font-size: 10px; padding: 1px 6px; border-radius: 6px; }
.pbd { padding: 8px; }
.sel { display: flex; align-items: center; gap: 6px; margin-bottom: 4px; }
.sel span { font-size: 10px; color: #888; }
.pc h3 { font-size: 13px; font-weight: 600; margin: 0 0 4px; line-height: 1.3; }
.pr { font-size: 14px; color: #FF7A45; font-weight: 800; margin: 0; }
.act { display: flex; gap: 12px; margin-top: 6px; }
.act button { border: 0; background: transparent; font-size: 12px; color: #666; cursor: pointer; padding: 2px 0; }
.bnav { position: fixed; left: 0; right: 0; bottom: 0; display: flex; justify-content: space-around; background: #fff; border-top: 1px solid #eee; padding: 6px 4px calc(6px + env(safe-area-inset-bottom)); z-index: 5; }
.bn { position: relative; border: 0; background: transparent; display: flex; flex-direction: column; align-items: center; gap: 2px; cursor: pointer; color: #999; padding: 2px 8px; }
.bi { position: relative; font-size: 16px; font-weight: 800; }
.bl { font-size: 9px; font-weight: 700; letter-spacing: .3px; }
.bn.on { color: #FF7A45; }
.ov { position: fixed; inset: 0; background: rgba(0,0,0,.92); z-index: 20; display: flex; align-items: center; justify-content: center; }
.ovi { width: 100%; max-width: 480px; height: 100%; object-fit: cover; }
.ovt { position: absolute; bottom: 24px; color: #fff; font-size: 12px; }
</style>

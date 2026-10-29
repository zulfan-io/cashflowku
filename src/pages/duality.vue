<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { supabase } from '~/utils/supabase'
import { useRouter } from 'vue-router'
import type { Product } from '~/schema/catalog'
import CProductCardThin from '~/components/CProductCardThin.vue'
import manifest from '~/data/ports.json'
import brands from '~/shared/brands'

const mk = (id, name, price, stock, sold, rating) => ({
  id, name, image: null, sold, rating, price, stock, variants: [],
  models: price != null ? [{ id, sku: 'SKU' + id, price, stock, variation_index: [], is_default: true, product_id: id }] : [],
  wholesale: []
})
function placeholderFeed() {
  const f = [
    mk(1, 'Kemeja Flanel Oversize', 89000, 32, 1240, 4.8),
    mk(2, 'Celana Kargo Dewasa', null, 0, 870, 4.6),
    mk(3, 'Hoodie Fleece Premium', 135000, 14, 2100, 4.9),
    mk(4, 'Sepatu Sneakers Retro', 199000, 7, 540, 4.3),
    mk(5, 'Tas Ransel Anti Air', 159000, 21, 3300, 4.7),
    mk(6, 'Jam Tangan Digital Sport', 75000, 3, 410, 4.5)
  ]
  f[1].models = [
    { id: 2, sku: 'SKU2A', price: 120000, stock: 5, variation_index: [], is_default: false, product_id: 2 },
    { id: 3, sku: 'SKU2B', price: 150000, stock: 9, variation_index: [], is_default: true, product_id: 2 }
  ]
  return f
}
function mapOffer(o) {
  const price = o.price != null ? Number(o.price) : null
  return {
    id: o.id, name: o.title || 'Produk', image: o.image_url || null,
    sold: 0, rating: 0, price, stock: 0, variants: [], wholesale: [],
    models: price != null ? [{ id: o.id, sku: 'AFF' + o.id, price, stock: 0, variation_index: [], is_default: true, product_id: o.id }] : []
  }
}
const feed = ref(placeholderFeed())
const src = ref('demo')
const rowLabels = ['Rekomendasi Untukmu', 'Produk Terlaris', 'Flash Sale', 'Baru Datang']
const feedAll = computed(() => { const f = feed.value; return f.length >= 15 ? f : [...f, ...f, ...f] })
const feedRows = computed(() => { const out = []; for (let i = 0; i < feedAll.value.length; i += 5) out.push(feedAll.value.slice(i, i + 5)); return out })
onMounted(async () => {
  try {
    const { data, error } = await supabase
      .from('shoper_offers')
      .select('*')
      .eq('active', true)
      .limit(24)
    if (!error && data && data.length) {
      feed.value = data.map(mapOffer)
      src.value = 'live'
    }
  } catch (e) {}
})

const storyFaces = ['A','B','C','D','E','F','G']
const chips = Object.values(brands).slice(0, 12)
const capture = manifest.reward.capture.join(' + ')
const pulsaOn = manifest.reward.pulsa_on_points

const slots = computed(() => {
  const fl = manifest.ports.filter(p => p.mount === 'floating')
  const max = manifest.ui.floating_max_slots
  const out = []
  for (let i = 0; i < max; i++) out.push(fl[i] || { id: 'slot-' + (i + 1), kind: 'segera', enabled: false, mount: 'floating' })
  return out
})

// bottom-nav ala Shopee: ikon = TEKS ASCII placeholder, ganti 1 baris pas colok ~icons/carbon lo
const tabs = [
  { id: 'home', label: 'HOME', on: true },
  { id: 'kat', label: 'KAT', on: false },
  { id: 'game', label: 'GAME', on: false },
  { id: 'notif', label: 'NOTIF', on: false },
  { id: 'saya', label: 'SAYA', on: false }
]

const router = useRouter()
const loveCounts = ref({})
const shareCounts = ref({})
async function onLove(p) {
  const { data: { user } } = await supabase.auth.getUser()
  if (!user) { console.log('login dulu buat love'); return }
  const { data: mem } = await supabase.from('shoper_members').select('id').eq('user_id', user.id).single()
  if (!mem) { console.log('belum jadi member'); return }
  const { error } = await supabase.from('shoper_loves').insert({ member_id: mem.id, target_type: 'offer', target_id: String(p.id) })
  if (!error) loveCounts.value[p.id] = (loveCounts.value[p.id] || 0) + 1
}
async function onShare(p) {
  const { error } = await supabase.from('shoper_shares').insert({ target_type: 'offer', target_id: String(p.id), channel: 'app' })
  if (!error) shareCounts.value[p.id] = (shareCounts.value[p.id] || 0) + 1
}
function onSelect(p) {
  router.push('/list')
}
function onTab(t) {
  console.log('tab', t.id)
}
</script>

<template>
  <div class="dual">
    <header class="top">
      <span class="logo">shoper</span>
      <span class="tag">katalog affiliate + widget pintasan</span>
      <span class="badge" :class="src">{{ src }}</span>
    </header>

    <div class="storyrail">
      <StoryCircle v-for="(f, i) in storyFaces" :key="f" :label="f" :src="'https://picsum.photos/seed/dstory-' + f + '/120/120'" :read="i < 1" :size="54" ring="#0095F6" />
    </div>
    <section class="chips">
      <button v-for="b in chips" :key="b" class="chip">{{ b }}</button>
    </section>

    <aside class="dock">
      <div v-for="w in slots" :key="w.id" class="slot" :class="{ off: !w.enabled }">
        <span class="ic">{{ w.id.slice(0, 2).toUpperCase() }}</span>
        <span class="lb">{{ w.kind }}</span>
        <span v-if="!w.enabled" class="soon">segera</span>
      </div>
    </aside>

    <section v-for="(row, ri) in feedRows" :key="ri" class="feedrow">
      <div class="lbl">{{ rowLabels[ri] || 'Rekomendasi' }}</div>
      <main class="feed">
        <CProductCardThin
          v-for="p in row"
          :key="p.id + '-' + ri"
          :product="p"
          @select="onSelect"
          @love="onLove"
          @share="onShare"
          :love-count="loveCounts[p.id] || 0"
          :share-count="shareCounts[p.id] || 0"
        />
      </main>
    </section>

    <section v-if="pulsaOn" class="reward">
      Main game -> kumpulin poin -> <b>pulsa gratis</b> dari owner
    </section>

    <nav class="botnav">
      <button
        v-for="t in tabs"
        :key="t.id"
        class="btab"
        :class="{ act: t.on }"
        @click="onTab(t)"
      >{{ t.label }}</button>
    </nav>

    <footer class="gate">
      Daftar member: <b>{{ capture }}</b> -> database berharga
    </footer>
  </div>
</template>

<style scoped>
.dual { max-width: 1280px; margin: 0 auto; padding: 12px clamp(12px, 3vw, 32px) 64px; font-family: system-ui, sans-serif; color: #1a1a1a; background: #f7f7f7; min-height: 100vh; }
.top { display: flex; align-items: baseline; gap: 8px; padding: 8px 0; border-bottom: 1px solid #e6e6e6; }
.logo { font-weight: 800; color: #FF7A45; font-size: 20px; }
.tag { font-size: 12px; color: #888; }
.badge { margin-left: auto; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 999px; letter-spacing: .5px; }
.badge.demo { background: #FFE0C2; color: #B34700; }
.badge.live { background: #D8F5DC; color: #1B7A2E; }
.reward { margin: 10px 0; padding: 10px 12px; background: #FFF3E9; border-radius: 10px; font-size: 13px; }
.chips { display: flex; gap: 6px; overflow-x: auto; padding: 6px 0; -webkit-overflow-scrolling: touch; }
.chip { flex: 0 0 auto; border: 1px solid #ddd; background: #fff; border-radius: 999px; padding: 5px 10px; font-size: 12px; cursor: pointer; transition: background .15s, border-color .15s, color .15s; }
.chip:active { background: #FF7A45; border-color: #FF7A45; color: #fff; }
.feedrow { margin: 8px 0; }
.feedrow .lbl { font-size: 13px; font-weight: 700; color: #1a1a1a; padding: 0 2px 4px; }
.feed { display: flex; gap: 10px; overflow-x: auto; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; scrollbar-width: none; margin: 4px 0; }
.feed::-webkit-scrollbar { display: none; }
.feed > * { flex: 0 0 auto; width: 30vw; max-width: 150px; scroll-snap-align: start; }
.rise-item { transition: opacity .35s ease, transform .35s ease; }
.rise-enter-from { opacity: 0; transform: translateY(14px); }
.rise-enter-to { opacity: 1; transform: none; }
.dock { display: grid; grid-template-rows: repeat(2, auto); grid-auto-flow: column; grid-auto-columns: 56px; gap: 6px; margin: 8px calc(-1 * clamp(12px, 3vw, 32px)); padding-inline: clamp(12px, 3vw, 32px); overflow-x: auto; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; scrollbar-width: none; }
.dock::-webkit-scrollbar { display: none; }
.dock > * { scroll-snap-align: start; }
.slot { position: relative; background: #fff; border: 1px solid #eee; border-radius: 12px; padding: 8px 2px; text-align: center; transition: background .15s, transform .15s; }
.slot:active { background: #FFF3E9; }
.slot.off { opacity: .5; }
.ic { display: block; font-weight: 800; color: #FF7A45; font-size: 15px; line-height: 1.1; }
.lb { display: block; font-size: 9px; color: #666; margin-top: 2px; }
.soon { position: absolute; top: 2px; right: 2px; font-size: 7px; background: #FF7A45; color: #fff; border-radius: 6px; padding: 1px 3px; }
.botnav { position: fixed; left: 0; right: 0; bottom: 0; display: flex; justify-content: space-around; background: #fff; border-top: 1px solid #e6e6e6; padding: 6px 4px calc(6px + env(safe-area-inset-bottom)); z-index: 5; }
.btab { flex: 1; border: 0; background: transparent; font-size: 10px; font-weight: 700; letter-spacing: .5px; color: #888; padding: 4px 0; cursor: pointer; transition: color .15s; }
.btab.act { color: #FF7A45; }
.gate { text-align: center; font-size: 12px; color: #666; padding: 10px; border-top: 1px solid #e6e6e6; }
.storyrail { display: flex; gap: 10px; overflow-x: auto; padding: 10px clamp(12px,3vw,32px); scrollbar-width: none; -webkit-overflow-scrolling: touch; }
.storyrail::-webkit-scrollbar { display: none; }
</style>


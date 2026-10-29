<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from '~/utils/supabase'

const router = useRouter()
const PAGE = 20
const CAP = 100
const items = ref([])
const loading = ref(false)
const done = ref(false)

function mapOffer(o) {
  const price = o.price != null ? Number(o.price) : null
  return { id: o.id, name: o.title || 'Produk', image: o.image_url || null, sold: 0, rating: 0, price, stock: 0, variants: [], wholesale: [], models: price != null ? [{ id: o.id, sku: 'AFF' + o.id, price, stock: 0, variation_index: [], is_default: true, product_id: o.id }] : [] }
}

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
function onSelect(p) { console.log('detail soon', p.id) }

const NAMES = ['Kemeja Flanel Oversize','Celana Kargo Dewasa','Hoodie Fleece Premium','Sepatu Sneakers Retro','Tas Ransel Anti Air','Jam Tangan Digital Sport','Jaket Denim Klasik','Sandal Kulit Pria']
const PRICES = [89000,120000,135000,199000,159000,75000,210000,99000]
function dummyBatch(from) {
  const out = []
  for (let i = 0; i < PAGE; i++) {
    const n = from + i
    out.push(mapOffer({ id: n + 1, title: NAMES[n % NAMES.length], image_url: 'https://picsum.photos/seed/shoper-list-' + n + '/400/400', price: PRICES[n % PRICES.length] }))
  }
  return out
}

async function loadBatch() {
  if (loading.value || done.value) return
  loading.value = true
  const from = items.value.length
  const { data, error } = await supabase.from('shoper_offers').select('*').eq('active', true).range(from, from + PAGE - 1)
  loading.value = false
  if (error || !data || !data.length) {
    if (items.value.length < CAP) {
      items.value = items.value.concat(dummyBatch(from))
      if (items.value.length >= CAP) done.value = true
      return
    }
    done.value = true; return
  }
  items.value = items.value.concat(data.map(mapOffer))
  if (items.value.length >= CAP || data.length < PAGE) done.value = true
}

let io = null
const sentinel = ref(null)
onMounted(() => {
  loadBatch()
  io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) loadBatch() }, { rootMargin: '400px' })
  if (sentinel.value) io.observe(sentinel.value)
})
onBeforeUnmount(() => { if (io) io.disconnect() })
</script>

<template>
  <div class="lst">
    <header class="lhead">
      <button class="back" @click="router.back()">Kembali</button>
      <span class="lttl">Katalog</span>
    </header>
    <main class="lgrid">
      <CProductCardThin v-for="p in items" :key="p.id" :product="p" @select="onSelect" @love="onLove" @share="onShare" :love-count="loveCounts[p.id] || 0" :share-count="shareCounts[p.id] || 0" />
    </main>
    <div ref="sentinel" class="lsent">{{ done ? ('Sudah semua (' + items.length + ' produk)') : (loading ? 'Memuat...' : 'Gulir untuk muat lagi') }}</div>
  </div>
</template>

<style scoped>
.lst { max-width: 1280px; margin: 0 auto; padding: 12px clamp(12px,3vw,32px) 64px; font-family: system-ui, sans-serif; color: #1a1a1a; background: #f7f7f7; min-height: 100vh; }
.lhead { display: flex; align-items: center; gap: 12px; padding: 8px 0; border-bottom: 1px solid #e6e6e6; }
.back { border: 1px solid #eee; background: #fff; border-radius: 999px; padding: 6px 14px; font-size: 13px; font-weight: 700; color: #FF7A45; cursor: pointer; }
.lttl { font-weight: 800; font-size: 16px; }
.lgrid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin: 12px 0; }
@media (min-width: 640px) { .lgrid { grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 12px; } }
.lsent { text-align: center; font-size: 12px; color: #888; padding: 16px 0 8px; }
</style>

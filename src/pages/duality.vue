<script setup lang="ts">
import { ref, computed } from 'vue'
import type { Product } from '~/schema/catalog'
import CProductCardThin from '~/components/CProductCardThin.vue'
import manifest from '~/data/ports.json'
import brands from '~/shared/brands'

const mk = (id, name, price, stock, sold, rating) => ({
  id, name, image: null, sold, rating, price, stock, variants: [],
  models: price != null ? [{ id, sku: 'SKU' + id, price, stock, variation_index: [], is_default: true, product_id: id }] : [],
  wholesale: []
})
const feed = ref([
  mk(1, 'Kemeja Flanel Oversize', 89000, 32, 1240, 4.8),
  mk(2, 'Celana Kargo Dewasa', null, 0, 870, 4.6),
  mk(3, 'Hoodie Fleece Premium', 135000, 14, 2100, 4.9),
  mk(4, 'Sepatu Sneakers Retro', 199000, 7, 540, 4.3),
  mk(5, 'Tas Ransel Anti Air', 159000, 21, 3300, 4.7),
  mk(6, 'Jam Tangan Digital Sport', 75000, 3, 410, 4.5)
])
feed.value[1].models = [
  { id: 2, sku: 'SKU2A', price: 120000, stock: 5, variation_index: [], is_default: false, product_id: 2 },
  { id: 3, sku: 'SKU2B', price: 150000, stock: 9, variation_index: [], is_default: true, product_id: 2 }
]

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

function onSelect(p) {
  console.log('select', p.id, p.name)
}
</script>

<template>
  <div class="dual">
    <header class="top">
      <span class="logo">shoper</span>
      <span class="tag">katalog affiliate + widget pintasan</span>
    </header>

    <section v-if="pulsaOn" class="reward">
      Main game -> kumpulin poin -> <b>pulsa gratis</b> dari owner
    </section>

    <section class="chips">
      <button v-for="b in chips" :key="b" class="chip">{{ b }}</button>
    </section>

    <main class="feed">
      <CProductCardThin v-for="p in feed" :key="p.id" :product="p" @select="onSelect" />
    </main>

    <aside class="dock">
      <div v-for="w in slots" :key="w.id" class="slot" :class="{ off: !w.enabled }">
        <span class="ic">{{ w.id.slice(0, 2).toUpperCase() }}</span>
        <span class="lb">{{ w.kind }}</span>
        <span v-if="!w.enabled" class="soon">segera</span>
      </div>
    </aside>

    <footer class="gate">
      Daftar member: <b>{{ capture }}</b> -> database berharga
    </footer>
  </div>
</template>

<style scoped>
.dual { max-width: 720px; margin: 0 auto; padding: 12px; font-family: system-ui, sans-serif; color: #1a1a1a; }
.top { display: flex; align-items: baseline; gap: 8px; padding: 8px 0; border-bottom: 1px solid #eee; }
.logo { font-weight: 800; color: #FF6600; font-size: 20px; }
.tag { font-size: 12px; color: #888; }
.reward { margin: 10px 0; padding: 10px 12px; background: #FFF3E9; border-radius: 10px; font-size: 13px; }
.chips { display: flex; gap: 6px; overflow-x: auto; padding: 6px 0; }
.chip { flex: 0 0 auto; border: 1px solid #ddd; background: #fff; border-radius: 999px; padding: 5px 10px; font-size: 12px; cursor: pointer; transition: background .15s, border-color .15s; }
.chip:hover { background: #FF6600; border-color: #FF6600; color: #fff; }
.feed { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin: 10px 0 96px; }
.dock { position: fixed; right: 12px; bottom: 12px; width: 176px; background: #fff; border: 1px solid #eee; border-radius: 14px; padding: 8px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; box-shadow: 0 8px 24px rgba(0,0,0,.12); }
.slot { position: relative; background: #fafafa; border-radius: 10px; padding: 8px 2px; text-align: center; transition: background .15s; }
.slot:hover { background: #FFF3E9; }
.slot.off { opacity: .5; }
.ic { display: block; font-weight: 800; color: #FF6600; font-size: 13px; }
.lb { display: block; font-size: 9px; color: #666; margin-top: 2px; }
.soon { position: absolute; top: 2px; right: 2px; font-size: 7px; background: #FF6600; color: #fff; border-radius: 6px; padding: 1px 3px; }
.gate { text-align: center; font-size: 12px; color: #666; padding: 10px; border-top: 1px solid #eee; }
@media (min-width: 560px) { .feed { grid-template-columns: repeat(3, 1fr); } }
</style>


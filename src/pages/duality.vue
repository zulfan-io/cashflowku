<script setup lang="ts">
import { ref } from 'vue'
import type { Product } from '~/schema/catalog'
import manifest from '~/data/ports.json'
import brands from '~/shared/brands'

// TODO(colok adapter): ganti array di bawah dengan hasil tpoParse/getResources lo.
// Shape = persis schema Product (image/price nullable -> null-safe di template).
const feed = ref<Product[]>([
  { id: 1, name: 'Kemeja Flanel Oversize', image: null, sold: 1240, rating: 4.8, price: 89000, stock: 32, variants: [], models: [], wholesale: [] },
  { id: 2, name: 'Celana Kargo Dewasa', image: null, sold: 870, rating: 4.6, price: null, stock: 0, variants: [], models: [], wholesale: [] },
  { id: 3, name: 'Hoodie Fleece Premium', image: null, sold: 2100, rating: 4.9, price: 135000, stock: 14, variants: [], models: [], wholesale: [] },
  { id: 4, name: 'Sepatu Sneakers Retro', image: null, sold: 540, rating: 4.3, price: 199000, stock: 7, variants: [], models: [], wholesale: [] },
  { id: 5, name: 'Tas Ransel Anti Air', image: null, sold: 3300, rating: 4.7, price: 159000, stock: 21, variants: [], models: [], wholesale: [] },
  { id: 6, name: 'Jam Tangan Digital Sport', image: null, sold: 410, rating: 4.5, price: 75000, stock: 3, variants: [], models: [], wholesale: [] }
])

const chips = Object.values(brands).slice(0, 12) as string[]
const widgets = manifest.ports.filter((p: any) => p.mount === 'floating').slice(0, manifest.ui.floating_max_slots)
const capture = manifest.reward.capture as string[]
const pulsaOn = manifest.reward.pulsa_on_points as boolean

function fmt(n: number | null): string {
  return n == null ? '-' : 'Rp' + n.toLocaleString('id-ID')
}
function rate(n: number | null): string {
  return n == null ? '-' : n.toFixed(1)
}
</script>

<template>
  <div class="dual">
    <header class="top">
      <span class="logo">shoper</span>
      <span class="tag">dualitas: feed affiliate + widget</span>
    </header>

    <section v-if="pulsaOn" class="reward">
      Main game -> kumpulin poin -> <b>pulsa gratis</b> dari owner
    </section>

    <section class="chips">
      <button v-for="b in chips" :key="b" class="chip">{{ b }}</button>
    </section>

    <main class="feed">
      <article v-for="p in feed" :key="p.id" class="card">
        <div class="ph">
          <img v-if="p.image" :src="p.image" :alt="p.name" />
          <span v-else class="ph-t">foto</span>
        </div>
        <h3 class="nm">{{ p.name }}</h3>
        <p class="pr">{{ fmt(p.price) }}</p>
        <p class="mt"><span>{{ rate(p.rating) }}</span> &middot; {{ p.sold }} terjual</p>
      </article>
    </main>

    <aside class="dock">
      <div v-for="w in widgets" :key="w.id" class="slot" :class="{ off: !w.enabled }">
        <span class="ic">{{ w.id.slice(0, 2) }}</span>
        <span class="lb">{{ w.kind }}</span>
        <span v-if="!w.enabled" class="soon">segera</span>
      </div>
    </aside>

    <footer class="gate">
      Daftar member: <b>{{ capture.join(' + ') }}</b> -> database berharga
    </footer>
  </div>
</template>

<style scoped>
.dual { max-width: 720px; margin: 0 auto; padding: 12px; font-family: system-ui, sans-serif; color: #1a1a1a; }
.top { display: flex; align-items: baseline; gap: 8px; padding: 8px 0; border-bottom: 1px solid #eee; }
.logo { font-weight: 800; color: #FF7A1A; font-size: 20px; }
.tag { font-size: 12px; color: #888; }
.reward { margin: 10px 0; padding: 10px 12px; background: #FFF3E9; border-radius: 10px; font-size: 13px; }
.chips { display: flex; gap: 6px; overflow-x: auto; padding: 6px 0; }
.chip { flex: 0 0 auto; border: 1px solid #ddd; background: #fff; border-radius: 999px; padding: 5px 10px; font-size: 12px; cursor: pointer; transition: background .15s, border-color .15s; }
.chip:hover { background: #FF7A1A; border-color: #FF7A1A; color: #fff; }
.feed { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin: 10px 0 80px; }
.card { background: #fff; border: 1px solid #eee; border-radius: 12px; overflow: hidden; transition: transform .15s, box-shadow .15s; }
.card:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(0,0,0,.08); }
.ph { aspect-ratio: 1 / 1; background: linear-gradient(135deg, #f3f3f3, #e9e9e9); display: flex; align-items: center; justify-content: center; }
.ph img { width: 100%; height: 100%; object-fit: cover; }
.ph-t { font-size: 12px; color: #aaa; }
.nm { font-size: 13px; margin: 8px 8px 2px; font-weight: 600; line-height: 1.3; }
.pr { font-size: 15px; color: #FF7A1A; font-weight: 800; margin: 0 8px; }
.mt { font-size: 11px; color: #888; margin: 4px 8px 8px; }
.dock { position: fixed; right: 12px; bottom: 12px; width: 168px; background: #fff; border: 1px solid #eee; border-radius: 14px; padding: 8px; display: grid; grid-template-columns: repeat(2, 1fr); gap: 6px; box-shadow: 0 8px 24px rgba(0,0,0,.12); }
.slot { position: relative; background: #fafafa; border-radius: 10px; padding: 8px 4px; text-align: center; transition: background .15s; }
.slot:hover { background: #FFF3E9; }
.slot.off { opacity: .55; }
.ic { display: block; font-weight: 800; color: #FF7A1A; font-size: 14px; }
.lb { display: block; font-size: 10px; color: #666; }
.soon { position: absolute; top: 2px; right: 3px; font-size: 8px; background: #FF7A1A; color: #fff; border-radius: 6px; padding: 1px 4px; }
.gate { text-align: center; font-size: 12px; color: #666; padding: 10px; border-top: 1px solid #eee; }
@media (min-width: 560px) { .feed { grid-template-columns: repeat(3, 1fr); } }
</style>
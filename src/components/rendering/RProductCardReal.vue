<template>
  <div class="rp-card">
    <img class="rp-img" :src="imgSrc(product.image)" :alt="product.name || ''" loading="lazy" />
    <div class="rp-body">
      <div class="rp-name">{{ product.name }}</div>
      <div class="rp-price">{{ fmtPrice(product.price) }}</div>
      <div class="rp-meta">
        <span v-if="product.sold > 0" class="rp-sold">{{ product.sold }} TERJUAL</span>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({ product: { type: Object, default: () => ({}) } })
// image dari API tp-o.tk = id aset ("demo-xxx "), BUKAN url. NOL nebak prefix ->
// fallback ke aset lo yang pasti ada; pas backend kasih http(s) url, otomatis kepake.
const imgSrc = (im) => (!im ? '/img/gen/gift-box-open.webp' : (/^https?:/.test(im) ? im : '/img/gen/gift-box-open.webp'))
const fmtPrice = (p) => (p == null ? '-' : '$' + Number(p).toFixed(2))
</script>

<style scoped>
.rp-card { width: 15rem; background: #fff; border-radius: 1rem; overflow: hidden; box-shadow: 0 6px 18px rgba(0,0,0,.12); display: flex; flex-direction: column; }
.rp-img { width: 100%; height: 20rem; object-fit: cover; background: #f3f4f6; }
.rp-body { padding: .75rem 1rem 1rem; display: flex; flex-direction: column; gap: .4rem; }
.rp-name { font-weight: 600; color: #111827; line-height: 1.3; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; min-height: 2.6em; }
.rp-price { color: #FF7A1A; font-weight: 800; font-size: 1.25rem; }
.rp-meta { display: flex; gap: .5rem; align-items: center; font-size: .8rem; color: #6b7280; }
.rp-sold { background: #FF7A1A; color: #FFF7EC; font-weight: 700; font-size: .7rem; padding: .1rem .4rem; border-radius: .3rem; }
</style>
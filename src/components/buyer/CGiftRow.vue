<template>
  <section class="gift-row p-5" aria-labelledby="gr-title">
    <div class="gr-head text-center mb-4">
      <h2 id="gr-title" class="text-2xl font-semibold text-[#FF7A1A]">Deretan Kejutan</h2>
      <p class="opacity-70">Produk & promo pilihan — scroll terus, tiap baris ada kado.</p>
    </div>
    <div class="gr-grid">
      <div v-for="it in items" :key="it.src" class="gr-card">
        <img :src="it.src" :alt="it.label" class="gr-img" loading="lazy" @error="$event.target.style.display='none'" />
        <span class="gr-label">{{ it.label }}</span>
      </div>
    </div>
  </section>
</template>
<script setup>
import { ref } from 'vue'
const items = ref([
  {src:'/img/gen/preview-1.jpg',label:'Kejutan Pagi'},
  {src:'/img/gen/badge-flash.webp',label:'Flash Harian'},
  {src:'/img/gen/preview-2.jpg',label:'Kejutan Siang'},
  {src:'/img/gen/sticker-discount.webp',label:'Diskon Kado'},
  {src:'/img/gen/preview-3.jpg',label:'Kejutan Sore'},
  {src:'/img/gen/badge-xpress.webp',label:'Kilat Express'},
  {src:'/img/gen/preview-4.jpg',label:'Kejutan Malam'},
  {src:'/img/gen/preview-5.jpg',label:'Kejutan Spesial'},
])
</script>
<style scoped>
.gr-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.8rem;max-width:1100px;margin:0 auto}
.gr-card{background:#111827;border:1px solid #FF7A1A33;border-radius:.9rem;overflow:hidden;display:flex;flex-direction:column;transition:transform .25s}
.gr-card:hover{transform:translateY(-4px)}
.gr-img{width:100%;aspect-ratio:1/1;object-fit:cover;background:#FF7A1A22}
.gr-label{padding:.5rem;text-align:center;font-weight:600;color:#FFF7EC;font-size:.9rem}
</style>

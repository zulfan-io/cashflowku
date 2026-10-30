<!-- cart-soft -->
<script setup lang="ts">
import ICartSoft from '~/components/icons/ICartSoft.vue'
const cols = ['#888888', '#FF6A2B', '#2F6BFF', '#7C4DFF']
</script>

<template>
  <div class="cs">
    <div class="cs-note">Bukti konsep: 1 file ICartSoft.vue, di-panggil 4x, warna beda-beda karena currentColor ngikutin CSS. Tinggal import, NOL duplikat file. Lo milih keluarga ikon: andrtsx / ion-outline / ion-filled.</div>
    <div class="cs-row">
      <span v-for="(c, i) in cols" :key="i" class="cs-ic" :style="{ color: c }"><ICartSoft /></span>
    </div>
    <div class="cs-row cs-big">
      <span v-for="(c, i) in cols" :key="i" class="cs-ic" :style="{ color: c }"><ICartSoft /></span>
    </div>
  </div>
</template>

<style scoped>
.cs { max-width: 480px; margin: 0 auto; padding: 24px 16px 80px; font-family: system-ui, sans-serif; color: #1a1a1a; background: #f7f7f7; min-height: 100vh; }
.cs-note { font-size: 12px; color: #888; line-height: 1.5; margin-bottom: 16px; }
.cs-row { display: flex; gap: 22px; justify-content: center; padding: 18px; background: #fff; border: 1px solid #eee; border-radius: 14px; margin-bottom: 12px; }
.cs-big .cs-ic { font-size: 40px; }
.cs-ic { font-size: 26px; display: inline-flex; }
</style>

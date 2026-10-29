<!-- candy2 -->
<script setup lang="ts">
import CIcon from '~/components/CIcon.vue'
const tabs = [['home','HOME'],['cart','KAT'],['game','GAME'],['bell','NOTIF'],['user','SAYA']]
</script>

<template>
  <div class="cv">
    <div class="cv-note">Candy v2 - tiap permen beda warna (level Shopee/Trip). Bukan 3D Tiket; untuk 3D pakai JPG lo (Jalur B). Navbar tiruan, belum dicolok ke duality.</div>
    <nav class="cnav">
      <button v-for="(t, i) in tabs" :key="t[0]" class="ctab" :class="{ on: i === 0 }">
        <CIcon :name="t[0]" :active="i === 0" :size="26" />
      </button>
    </nav>
    <div class="cv-row">
      <CIcon v-for="t in tabs" :key="t[0]" :name="t[0]" :size="34" />
    </div>
  </div>
</template>

<style scoped>
.cv { max-width: 480px; margin: 0 auto; padding: 24px 16px 120px; font-family: system-ui, sans-serif; color: #1a1a1a; background: #f7f7f7; min-height: 100vh; }
.cv-note { font-size: 12px; color: #888; line-height: 1.5; margin-bottom: 16px; }
.cnav { position: fixed; left: 0; right: 0; bottom: 0; max-width: 480px; margin: 0 auto; display: flex; justify-content: space-around; background: #fff; border-top: 1px solid #eee; padding: 8px 4px calc(8px + env(safe-area-inset-bottom)); z-index: 5; }
.ctab { flex: 1; border: 0; background: transparent; cursor: pointer; padding: 4px 0; display: flex; justify-content: center; }
.ctab :deep(.ci) { filter: grayscale(1) opacity(.4); }
.ctab.on :deep(.ci) { filter: drop-shadow(0 3px 6px rgba(0,0,0,.28)); }
.cv-row { display: flex; gap: 18px; justify-content: center; margin-top: 24px; padding: 16px; background: #fff; border: 1px solid #eee; border-radius: 14px; }
</style>

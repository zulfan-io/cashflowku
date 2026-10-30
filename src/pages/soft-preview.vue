<!-- soft-pack -->
<script setup lang="ts">
import ICartSoft from '~/components/icons/ICartSoft.vue'
import IGridSoft from '~/components/icons/IGridSoft.vue'
const icons = [ICartSoft, IGridSoft]
const cols = ['#888888', '#FF6A2B', '#2F6BFF', '#7C4DFF']
</script>

<template>
  <div class="sp">
    <div class="sp-note">Keluarga soft (andrtsx duotone): cart + grid serumah, stroke 1.5 + fill .2. 1 file per ikon, warna ngikutin CSS. Borong sisanya (home/gamepad/bell/person) dari set yang sama.</div>
    <div class="sp-row">
      <span v-for="(c,ci) in cols" :key="ci" class="sp-ic" :style="{ color: c }"><component :is="icons[0]" /></span>
    </div>
    <div class="sp-row sp-big">
      <span v-for="(c,ci) in cols" :key="ci" class="sp-ic" :style="{ color: c }"><component :is="icons[1]" /></span>
    </div>
  </div>
</template>

<style scoped>
.sp { max-width: 480px; margin: 0 auto; padding: 24px 16px 80px; font-family: system-ui, sans-serif; color: #1a1a1a; background: #f7f7f7; min-height: 100vh; }
.sp-note { font-size: 12px; color: #888; line-height: 1.5; margin-bottom: 16px; }
.sp-row { display: flex; gap: 22px; justify-content: center; padding: 18px; background: #fff; border: 1px solid #eee; border-radius: 14px; margin-bottom: 12px; }
.sp-big .sp-ic { font-size: 40px; }
.sp-ic { font-size: 26px; display: inline-flex; }
</style>

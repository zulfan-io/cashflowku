<!-- soft-pack -->
<script setup lang="ts">
import ICartSoft from '~/components/icons/ICartSoft.vue'
import IGridSoft from '~/components/icons/IGridSoft.vue'
import IGamepadSoft from '~/components/icons/IGamepadSoft.vue'
const icons = [ICartSoft, IGridSoft, IGamepadSoft]
const cols = ['#888888', '#FF6A2B', '#2F6BFF', '#7C4DFF']
</script>

<template>
  <div class="sp">
    <div class="sp-note">Keluarga soft: cart+grid (andrtsx duotone) + gamepad (hugeicons pure stroke). Campur set disengaja, lo nilai: janggal = ganti.</div>
    <div class="sp-row" v-for="(ic,ii) in icons" :key="ii">
      <span v-for="(c,ci) in cols" :key="ci" class="sp-ic" :style="{ color: c }"><component :is="ic" /></span>
    </div>
  </div>
</template>

<style scoped>
.sp { max-width: 480px; margin: 0 auto; padding: 24px 16px 80px; font-family: system-ui, sans-serif; color: #1a1a1a; background: #f7f7f7; min-height: 100vh; }
.sp-note { font-size: 12px; color: #888; line-height: 1.5; margin-bottom: 16px; }
.sp-row { display: flex; gap: 22px; justify-content: center; padding: 18px; background: #fff; border: 1px solid #eee; border-radius: 14px; margin-bottom: 12px; }
.sp-ic { font-size: 30px; display: inline-flex; }
</style>

<script setup lang="ts">
import { computed } from 'vue'
const props = defineProps<{ src?: string | null; label?: string; read?: boolean; size?: number; ring?: string }>()
const emit = defineEmits<{ (e: 'open'): void }>()
const s = computed(() => props.size || 56)
const ini = computed(() => (props.label || '?').slice(0, 1).toUpperCase())
</script>

<template>
  <button class="sc-wrap" :style="{ width: s + 'px', height: s + 'px' }" :class="{ read }" @click="emit('open')">
    <span class="sc-ring" :style="{ width: s + 'px', height: s + 'px', borderColor: ring || undefined }">
      <img v-if="src" class="sc-img" :src="src" alt="" />
      <span v-else class="sc-ini">{{ ini }}</span>
    </span>
  </button>
</template>

<style scoped>
.sc-wrap { border: 0; background: transparent; padding: 0; cursor: pointer; display: inline-flex; flex: 0 0 auto; }
.sc-ring { display: flex; align-items: center; justify-content: center; border-radius: 50%; border: 2px solid #FF7A45; padding: 2px; box-sizing: border-box; transition: border-color .2s; }
.sc-wrap.read .sc-ring { border-color: #ddd; }
.sc-img { width: 100%; height: 100%; border-radius: 50%; object-fit: cover; }
.sc-ini { width: 100%; height: 100%; border-radius: 50%; display: flex; align-items: center; justify-content: center; background: #f0f0f0; color: #888; font-weight: 700; font-size: 16px; }
</style>

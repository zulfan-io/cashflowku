<script setup lang="ts">
defineProps<{ on?: boolean }>()
</script>

<template>
  <span v-if="on" class="nd-dot"></span>
</template>

<style scoped>
.nd-dot { position: absolute; top: -2px; right: -2px; width: 9px; height: 9px; border-radius: 50%; background: #FF3B30; border: 2px solid #fff; box-sizing: content-box; }
</style>

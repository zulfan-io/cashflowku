<script setup>
import StoryCircle from '~/components/StoryCircle.vue'
import Dots from '~/components/Dots.vue'
import NotifDot from '~/components/NotifDot.vue'
const faces = ['A','B','C','D','E','F']
</script>

<template>
  <div class="pv">
    <h2 class="pv-h">Rail Story (24 jam, bulat = wajah)</h2>
    <div class="pv-rail">
      <StoryCircle v-for="(f, i) in faces" :key="f" :label="f" :read="i < 2" :size="60" @open="() => {}" />
    </div>
    <p class="pv-note">2 pertama = sudah dilihat (ring abu). Sisanya unread (ring coral).</p>

    <h2 class="pv-h">Dots posisi (tanpa teks, tanpa tombol)</h2>
    <Dots :count="5" :active="2" />

    <h2 class="pv-h">Notif titik (merah = ada baru, bukan angka)</h2>
    <div class="pv-bell">B<span class="pv-rel"><NotifDot :on="true" /></span></div>
  </div>
</template>

<style scoped>
.pv { max-width: 720px; margin: 0 auto; padding: 24px 16px 64px; font-family: system-ui, sans-serif; color: #1a1a1a; background: #f7f7f7; min-height: 100vh; }
.pv-h { font-size: 14px; font-weight: 700; margin: 24px 0 10px; color: #555; }
.pv-rail { display: flex; gap: 12px; overflow-x: auto; padding: 4px 2px; scrollbar-width: none; }
.pv-rail::-webkit-scrollbar { display: none; }
.pv-note { font-size: 11px; color: #999; margin: 8px 0 0; }
.pv-bell { position: relative; display: inline-flex; align-items: center; justify-content: center; width: 36px; height: 36px; border-radius: 50%; background: #fff; border: 1px solid #eee; font-weight: 800; color: #888; }
.pv-rel { position: absolute; top: 0; right: 0; }
</style>

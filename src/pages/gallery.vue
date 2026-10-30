<!-- gl-candy -->
<script setup lang="ts">
import { ref, computed } from 'vue'
import cand from '~/data/cand.json'
import cfg from '~/data/icons.json'
const C = cand as any[]
const CFG = cfg as any
const SLOTS = ['home', 'kat', 'game', 'notif', 'saya']
const PER = 12
const page = ref(0)
const active = ref('home')
const copied = ref(false)
const name2num: Record<string, number> = {}
C.forEach((c: any) => { name2num[c.name] = c.num })
const sel = ref<Record<string, number>>({})
;(CFG.themes['navbar-permen'].icons || []).forEach((sl: any, i: number) => {
  sel.value[SLOTS[i]] = name2num[sl.n] || 0
})
const pal = computed(() => (CFG.themes['navbar-permen'].icons || []).map((sl: any) => ({ lite: sl.lite, base: sl.base })))
const activeIdx = computed(() => SLOTS.indexOf(active.value))
const activePal = computed(() => pal.value[activeIdx.value] || { lite: '#9a9a9a', base: '#5a5a5a' })
const totalPages = computed(() => Math.max(1, Math.ceil(C.length / PER)))
const pageItems = computed(() => C.slice(page.value * PER, page.value * PER + PER))
const candByNum = (n: number) => C.find((c: any) => c.num === n)
const pvItems = computed(() => SLOTS.map((s, i) => ({ s, num: sel.value[s], c: candByNum(sel.value[s]), p: pal.value[i] })).filter((x: any) => x.c))
const summary = computed(() => SLOTS.map((s) => s + '=' + sel.value[s]).join(','))
function isSelected(n: number) { return sel.value[active.value] === n }
function assign(n: number) {
  sel.value[active.value] = n
  const idx = SLOTS.indexOf(active.value)
  active.value = SLOTS[(idx + 1) % SLOTS.length]
}
function prev() { if (page.value > 0) page.value-- }
function next() { if (page.value < totalPages.value - 1) page.value++ }
async function copy() {
  try { await navigator.clipboard.writeText(summary.value); copied.value = true; setTimeout(() => (copied.value = false), 1500) } catch (e) { copied.value = false }
}
</script>

<template>
  <div class="gl">
    <div class="gl-note">GALERI CANDY. Grid ikut WARNA slot aktif - teken chip di atas, semua piring ganti rasa. TEKEN ikon = masuk slot + naik + ring + centang, otomatis maju. Garis hijau di bawah: SALIN atau baca, kirim ke aku, aku encode ke icons.json.</div>
    <div class="gl-slots">
      <button v-for="(s, i) in SLOTS" :key="s" class="gl-chip" :class="{ on: active === s }" :style="{ '--cl': pal[i] ? pal[i].base : '#1a1a1a' }" @click="active = s">
        <span class="gl-chip-n">{{ s }}</span>
        <span class="gl-chip-v">#{{ sel[s] }} {{ (candByNum(sel[s]) || {}).name || '?' }}</span>
      </button>
    </div>
    <div class="gl-pageinfo">Halaman {{ page + 1 }} / {{ totalPages }} - {{ C.length }} ikon</div>
    <div class="gl-grid">
      <button v-for="c in pageItems" :key="c.num" class="gl-cell" :class="{ sel: isSelected(c.num) }" :style="{ '--m': c.m, '--lite': activePal.lite, '--base': activePal.base }" @click="assign(c.num)">
        <span class="gl-glyph"></span>
        <span class="gl-check">&#10003;</span>
        <span class="gl-num">{{ c.num }}</span>
        <span class="gl-name">{{ c.name }}</span>
      </button>
    </div>
    <div class="gl-nav">
      <button class="gl-btn" @click="prev">&#9664; Prev</button>
      <button class="gl-btn" @click="next">Next &#9654;</button>
    </div>
    <div class="gl-prev-lab">PREVIEW navbar-permen (bentuk dari pilihanmu, warna per-slot)</div>
    <div class="gl-preview">
      <div v-for="it in pvItems" :key="it.s" class="pvcell">
        <span class="pv" :style="{ '--m': it.c.m, '--lite': it.p.lite, '--base': it.p.base }"></span>
        <small>{{ it.s }}</small>
      </div>
    </div>
    <div class="gl-out">
      <code class="gl-order">{{ summary }}</code>
      <button class="gl-btn" @click="copy">SALIN</button>
      <span v-if="copied" class="gl-ok">tersalin</span>
    </div>
  </div>
</template>

<style scoped>
.gl { max-width: 480px; margin: 0 auto; padding: 20px 14px 80px; font-family: system-ui, sans-serif; color: #1a1a1a; background: #f4f4f6; min-height: 100vh; }
.gl-note { font-size: 12px; color: #777; line-height: 1.55; margin-bottom: 14px; }
.gl-slots { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 14px; }
.gl-chip { border: 1px solid #e2e2e6; background: #fff; border-radius: 999px; padding: 7px 13px; cursor: pointer; display: flex; flex-direction: column; align-items: flex-start; min-width: 60px; transition: background .2s, color .2s, box-shadow .2s, transform .15s; }
.gl-chip:active { transform: scale(.95); }
.gl-chip.on { background: var(--cl); border-color: transparent; box-shadow: 0 6px 16px -6px var(--cl); }
.gl-chip.on .gl-chip-n, .gl-chip.on .gl-chip-v { color: #fff; }
.gl-chip-n { font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: .5px; color: #333; }
.gl-chip-v { font-size: 10px; color: #999; }
.gl-pageinfo { font-size: 11px; color: #999; margin-bottom: 10px; }
.gl-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; background: #fff; border: 1px solid #ececf0; border-radius: 18px; padding: 14px; box-shadow: 0 8px 24px -16px rgba(0,0,0,.18); }
.gl-cell { position: relative; border: 0; background: transparent; cursor: pointer; display: flex; flex-direction: column; align-items: center; gap: 5px; padding: 12px 6px 9px; border-radius: 16px; transition: transform .22s cubic-bezier(.34,1.56,.64,1), box-shadow .22s, background .2s; }
.gl-cell:active { transform: scale(.93); }
.gl-cell.sel { transform: translateY(-3px) scale(1.05); background: #fff; box-shadow: 0 8px 18px -6px var(--base), inset 0 0 0 2px var(--base); }
.gl-glyph { width: 40px; height: 40px; display: inline-block; -webkit-mask: var(--m) center / contain no-repeat; mask: var(--m) center / contain no-repeat; background: linear-gradient(180deg, var(--lite), var(--base)); }
.gl-check { position: absolute; top: 5px; right: 8px; font-size: 14px; font-weight: 800; color: var(--base); opacity: 0; transition: opacity .2s; }
.gl-cell.sel .gl-check { opacity: 1; }
.gl-num { font-size: 13px; font-weight: 800; color: #1a1a1a; }
.gl-name { font-size: 9px; color: #9a9a9a; max-width: 80px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.gl-nav { display: flex; gap: 12px; justify-content: center; margin: 14px 0; }
.gl-btn { border: 1px solid #e2e2e6; background: #fff; border-radius: 999px; padding: 9px 18px; cursor: pointer; font-size: 12px; font-weight: 600; color: #333; transition: background .18s, transform .15s; }
.gl-btn:active { transform: scale(.95); background: #f0f0f3; }
.gl-prev-lab { font-size: 11px; color: #999; margin: 8px 0; }
.gl-preview { display: flex; gap: 16px; justify-content: center; background: #fff; border: 1px solid #ececf0; border-radius: 18px; padding: 16px; box-shadow: 0 8px 24px -16px rgba(0,0,0,.18); }
.pvcell { display: flex; flex-direction: column; align-items: center; gap: 5px; }
.pv { width: 28px; height: 28px; display: inline-block; -webkit-mask: var(--m) center / contain no-repeat; mask: var(--m) center / contain no-repeat; background: linear-gradient(180deg, var(--lite), var(--base)); }
.pvcell small { font-size: 9px; color: #aaa; text-transform: uppercase; letter-spacing: .4px; }
.gl-out { display: flex; gap: 8px; align-items: center; margin-top: 16px; flex-wrap: wrap; }
.gl-order { background: #111; color: #7CFC9A; padding: 7px 10px; border-radius: 10px; font-size: 11px; word-break: break-all; flex: 1; min-width: 150px; }
.gl-ok { font-size: 11px; color: #10B981; font-weight: 700; }
</style>

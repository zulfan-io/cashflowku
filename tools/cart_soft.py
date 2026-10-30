import os,sys
IC='src/components/icons/ICartSoft.vue'; PV='src/pages/cart-soft-preview.vue'
if os.path.isfile('src/components/icons/ICart.vue') and IC=='src/components/icons/ICart.vue': sys.exit('ABORT: mau timpa ICart.vue harta lo')
for f in (IC,PV):
    if os.path.isfile(f):
        ex=open(f,encoding='utf-8').read()
        if 'cart-soft' in ex: sys.exit('udah ada, skip')
        sys.exit('ABORT '+f+' ada bukan buatan gue')
SVG='''<svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">
	<g fill="none">
		<path fill="currentColor" d="M21.03 13.6c1.27-3.32 1.9-4.98 1.22-6.2a3 3 0 0 0-.28-.42c-.89-1.1-2.66-1.12-6.21-1.18l-5.08-.08c-3.08-.04-4.62-.07-5.52.85l-.25.3c-.78 1.03-.52 2.55-.01 5.59c.37 2.2.55 3.31 1.29 4l.24.2c.8.62 1.92.62 4.16.62h5.08c1.82 0 2.73 0 3.45-.44l.26-.18c.67-.52 1-1.37 1.65-3.07" opacity=".2" />
		<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="m4.96 12.09l-.84-6.14h11.26c3.52 0 5.28 0 6.17 1.05a3 3 0 0 1 .37.54c.65 1.21.01 2.85-1.26 6.13c-.64 1.64-.96 2.46-1.6 2.97q-.16.12-.33.22c-.71.42-1.59.42-3.35.42H10.9c-2.5 0-3.74 0-4.59-.74s-1.02-1.98-1.35-4.45" />
		<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4.6 9.25L3.94 4.9a2.45 2.45 0 0 0-2.42-2.1" />
		<circle cx="8.25" cy="19.11" r="1.83" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" transform="rotate(90 8.25 19.11)" />
		<circle cx="17.27" cy="19.11" r="1.83" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" transform="rotate(90 17.27 19.11)" />
		<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="m15.62 12.34l-.5.49c-1 1-1.5 1.5-2.11 1.5c-.62 0-1.12-.5-2.13-1.5l-.49-.5M13 9.05v4.88" />
	</g>
</svg>'''
NC='''<!-- cart-soft -->
<template>
  ''' + SVG + '''
</template>
'''
PC='''<!-- cart-soft -->
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
'''
errs=[]
for f,C,mk in ((IC,NC,['cart-soft','currentColor','viewBox="0 0 24 24"','</svg>']),(PV,PC,['cart-soft','ICartSoft from','cs-row','currentColor'])):
    for ch in C:
        if ord(ch)>127: errs.append('non-ASCII '+f); break
    for m in mk:
        if m not in C: errs.append('marker '+m+' hilang '+f)
    if C.count('</template>')!=1: errs.append('tag tutup '+f)
if errs:
    print('[MELESET] TIDAK ditulis (file utuh):'); [print('  ',e) for e in errs]; sys.exit(1)
open(IC,'w',encoding='utf-8',newline='\n').write(NC)
open(PV,'w',encoding='utf-8',newline='\n').write(PC)
print('OK ICartSoft 1 file + preview 4 warna', IC, PV)

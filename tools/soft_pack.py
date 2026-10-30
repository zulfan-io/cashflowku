import os,sys
def wrap(svg):
    s=svg.replace('\t','  ')
    if '\t' in s: sys.exit('MELESET tab sisa')
    body='\n'.join(('  '+l if l.strip() else l) for l in s.split('\n'))
    return '<!-- soft-icon -->\n<template>\n'+body+'\n</template>\n'
CART='<svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">\n\t<g fill="none">\n\t\t<path fill="currentColor" d="M21.03 13.6c1.27-3.32 1.9-4.98 1.22-6.2a3 3 0 0 0-.28-.42c-.89-1.1-2.66-1.12-6.21-1.18l-5.08-.08c-3.08-.04-4.62-.07-5.52.85l-.25.3c-.78 1.03-.52 2.55-.01 5.59c.37 2.2.55 3.31 1.29 4l.24.2c.8.62 1.92.62 4.16.62h5.08c1.82 0 2.73 0 3.45-.44l.26-.18c.67-.52 1-1.37 1.65-3.07" opacity=".2" />\n\t\t<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="m4.96 12.09l-.84-6.14h11.26c3.52 0 5.28 0 6.17 1.05a3 3 0 0 1 .37.54c.65 1.21.01 2.85-1.26 6.13c-.64 1.64-.96 2.46-1.6 2.97q-.16.12-.33.22c-.71.42-1.59.42-3.35.42H10.9c-2.5 0-3.74 0-4.59-.74s-1.02-1.98-1.35-4.45" />\n\t\t<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4.6 9.25L3.94 4.9a2.45 2.45 0 0 0-2.42-2.1" />\n\t\t<circle cx="8.25" cy="19.11" r="1.83" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" transform="rotate(90 8.25 19.11)" />\n\t\t<circle cx="17.27" cy="19.11" r="1.83" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" transform="rotate(90 17.27 19.11)" />\n\t\t<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="m15.62 12.34l-.5.49c-1 1-1.5 1.5-2.11 1.5c-.62 0-1.12-.5-2.13-1.5l-.49-.5M13 9.05v4.88" />\n\t</g>\n</svg>'
GRID='<svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">\n\t<g fill="none">\n\t\t<rect width="7.75" height="7.75" x="21.51" y="10.34" fill="currentColor" opacity=".2" rx="2" transform="rotate(-180 21.51 10.34)" />\n\t\t<rect width="7.75" height="7.75" x="10.24" y="13.25" fill="currentColor" opacity=".2" rx="2" transform="rotate(-180 10.24 13.25)" />\n\t\t<rect width="7.75" height="7.75" x="19.2" y="21.45" fill="currentColor" opacity=".2" rx="2" transform="rotate(-180 19.2 21.45)" />\n\t\t<rect width="7.75" height="7.75" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" rx="2" transform="matrix(1 0 0 -1 13.76 10.34)" />\n\t\t<rect width="7.75" height="7.75" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" rx="2" transform="matrix(1 0 0 -1 2.49 13.25)" />\n\t\t<rect width="7.75" height="7.75" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" rx="2" transform="matrix(1 0 0 -1 11.45 21.45)" />\n\t</g>\n</svg>'
IC='src/components/icons'; PV='src/pages/soft-preview.vue'
made=[]; skipped=[]
for nm,svg in (('ICartSoft',CART),('IGridSoft',GRID)):
    P=IC+'/'+nm+'.vue'
    if os.path.isfile(P):
        ex=open(P,encoding='utf-8').read()
        if 'soft-icon' in ex or 'cart-soft' in ex: skipped.append(nm); continue
        sys.exit('ABORT '+P+' ada bukan soft')
    C=wrap(svg)
    for ch in C:
        if ord(ch)>127: sys.exit('MELESET non-ASCII '+nm)
    for m in ('currentColor','viewBox="0 0 24 24"','</svg>','<template>','</template>'):
        if m not in C: sys.exit('MELESET '+m+' di '+nm)
    if C.count('</template>')!=1: sys.exit('MELESET tag '+nm)
    open(P,'w',encoding='utf-8',newline='\n').write(C); made.append(nm)
PC='''<!-- soft-pack -->
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
'''
for ch in PC:
    if ord(ch)>127: sys.exit('MELESET non-ASCII PV')
for m in ('soft-pack','ICartSoft from','IGridSoft from','component :is'):
    if m not in PC: sys.exit('MELESET '+m+' PV')
if PC.count('</template>')!=1 or PC.count('</style>')!=1: sys.exit('MELESET tag PV')
open(PV,'w',encoding='utf-8',newline='\n').write(PC)
print('OK soft-pack: bikin', made or '-', '| skip-udah', skipped or '-', '| preview', PV)

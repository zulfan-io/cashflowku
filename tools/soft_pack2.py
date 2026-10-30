import os,sys
def wrap(svg):
    s=svg.replace('\t','  ')
    if '\t' in s: sys.exit('MELESET tab sisa')
    body='\n'.join(('  '+l if l.strip() else l) for l in s.split('\n'))
    return '<!-- soft-icon -->\n<template>\n'+body+'\n</template>\n'
GP='<svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">\n\t<g fill="none" stroke="currentColor" stroke-width="1.5">\n\t\t<path stroke-linecap="round" stroke-linejoin="round" d="M17.25 8.625v.125m.25 0a.25.25 0 1 1-.5 0a.25.25 0 0 1 .5 0m-2.75 2.375v.125m.25 0a.25.25 0 1 1-.5 0a.25.25 0 0 1 .5 0" />\n\t\t<path d="M6.707 5c-.475 0-.713 0-1.027.107s-.43.197-.661.376C2.352 7.543.76 13.077 3.225 17.525c.55.99 1.664 1.475 2.797 1.475c1.19 0 2.255-.738 2.672-1.852L9.125 16c.127-.337.19-.506.295-.634a1 1 0 0 1 .45-.313c.158-.053.338-.053.698-.053h2.864c.36 0 .54 0 .697.053a1 1 0 0 1 .451.313c.105.128.168.297.295.634l.43 1.148A2.85 2.85 0 0 0 17.979 19c1.133 0 2.247-.484 2.797-1.475c2.464-4.448.874-9.982-1.793-12.042c-.232-.18-.347-.269-.662-.376C18.007 5 17.77 5 17.295 5z" />\n\t\t<path stroke-linecap="round" stroke-linejoin="round" d="M7.995 8v4M10 9.995H6" />\n\t</g>\n</svg>'
IC='src/components/icons'; PV='src/pages/soft-preview.vue'
made=[]; skipped=[]
for nm,svg in (('IGamepadSoft',GP),):
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
'''
for ch in PC:
    if ord(ch)>127: sys.exit('MELESET non-ASCII PV')
for m in ('soft-pack','IGamepadSoft from','component :is'):
    if m not in PC: sys.exit('MELESET '+m+' PV')
if PC.count('</template>')!=1 or PC.count('</style>')!=1: sys.exit('MELESET tag PV')
open(PV,'w',encoding='utf-8',newline='\n').write(PC)
print('OK soft-pack2: bikin', made or '-', '| skip', skipped or '-', '| preview', PV)

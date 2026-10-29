import os,sys
P='src/components/Dots.vue'
if os.path.isfile(P):
    if 'dt-dot' in open(P,encoding='utf-8').read(): sys.exit('udah, skip')
    sys.exit('ABORT: Dots.vue udah ada bukan buatan gue')
C='''<script setup>
defineProps<{ count: number; active: number }>()
</script>

<template>
  <div class="dt-row">
    <span v-for="i in count" :key="i" class="dt-dot" :class="{ on: i - 1 === active }"></span>
  </div>
</template>

<style scoped>
.dt-row { display: flex; gap: 5px; align-items: center; justify-content: center; }
.dt-dot { width: 6px; height: 6px; border-radius: 50%; background: #ddd; transition: background .2s, width .2s; }
.dt-dot.on { background: #FF7A45; width: 14px; border-radius: 999px; }
</style>
'''
for ch in C:
    if ord(ch)>127: sys.exit('MELESET non-ASCII')
for m in ['dt-dot','defineProps','#FF7A45']:
    if m not in C: sys.exit('MELESET marker '+m)
open(P,'w',encoding='utf-8',newline='\n').write(C)
print('OK Dots',P)

import os,sys
P='src/components/NotifDot.vue'
if os.path.isfile(P):
    if 'nd-dot' in open(P,encoding='utf-8').read(): sys.exit('udah, skip')
    sys.exit('ABORT: NotifDot.vue udah ada bukan buatan gue')
C='''<script setup>
defineProps<{ on?: boolean }>()
</script>

<template>
  <span v-if="on" class="nd-dot"></span>
</template>

<style scoped>
.nd-dot { position: absolute; top: -2px; right: -2px; width: 9px; height: 9px; border-radius: 50%; background: #FF3B30; border: 2px solid #fff; box-sizing: content-box; }
</style>
'''
for ch in C:
    if ord(ch)>127: sys.exit('MELESET non-ASCII')
for m in ['nd-dot','#FF3B30','position: absolute']:
    if m not in C: sys.exit('MELESET marker '+m)
open(P,'w',encoding='utf-8',newline='\n').write(C)
print('OK NotifDot',P)

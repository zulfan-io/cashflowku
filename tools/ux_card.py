import os,sys
P='src/components/CProductCardThin.vue'
RAW='''<script setup lang="ts">
import { computed } from 'vue'
import type { Product } from '~/schema/catalog'

const props = defineProps<{ product: Product }>()
const emit = defineEmits<{ (e: 'select', p: Product): void }>()

const priceText = computed(() => {
  const p = props.product
  if (p.price != null) return 'Rp' + p.price.toLocaleString('id-ID')
  const ms = (p.models || []).map(m => m.price).filter(v => v != null)
  if (!ms.length) return '-'
  const mn = Math.min(...ms)
  const mx = Math.max(...ms)
  return mn === mx ? 'Rp' + mn.toLocaleString('id-ID') : 'Rp' + mn.toLocaleString('id-ID') + ' - Rp' + mx.toLocaleString('id-ID')
})
const soldText = computed(() => (props.product.sold || 0).toLocaleString('id-ID'))
const out = computed(() => (props.product.stock || 0) <= 0)
</script>

<template>
  <article class="thin" @click="emit('select', props.product)">
    <div class="ph">
      <img v-if="props.product.image" :src="props.product.image" :alt="props.product.name" />
      <span v-else class="ph-t">foto</span>
      <span v-if="out" class="badge">Habis</span>
    </div>
    <div class="body">
      <h3 class="nm">{{ props.product.name }}</h3>
      <p class="pr">{{ priceText }}</p>
      <div class="mt">
        <span class="rt">{{ (props.product.rating || 0).toFixed(1) }}</span>
        <span class="sd">{{ soldText }} terjual</span>
      </div>
    </div>
  </article>
</template>

<style scoped>
.thin { background: #fff; border: 1px solid #eee; border-radius: 12px; overflow: hidden; cursor: pointer; transition: transform .15s, box-shadow .15s; }
.thin:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(0,0,0,.08); }
.ph { position: relative; aspect-ratio: 1 / 1; background: linear-gradient(135deg, #f3f3f3, #e9e9e9); display: flex; align-items: center; justify-content: center; }
.ph img { width: 100%; height: 100%; object-fit: cover; }
.ph-t { font-size: 12px; color: #aaa; }
.badge { position: absolute; top: 6px; left: 6px; background: rgba(0,0,0,.6); color: #fff; font-size: 10px; padding: 2px 6px; border-radius: 6px; }
.body { padding: 8px; }
.nm { font-size: 13px; font-weight: 600; line-height: 1.3; margin: 0 0 4px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.pr { font-size: 15px; color: #FF6600; font-weight: 800; margin: 0; }
.mt { display: flex; align-items: center; justify-content: space-between; margin-top: 4px; }
.rt { font-size: 11px; color: #f5a623; font-weight: 700; }
.sd { font-size: 11px; color: #888; }
</style>
'''
lines=[];bad=[]
for i,l in enumerate(RAW.split('\n'),1):
    l=l.replace('\t','  ').rstrip()
    for ch in l:
        if ord(ch)>127: bad.append((i,hex(ord(ch))))
    lines.append(l)
txt='\n'.join(lines)+'\n'
if bad:
    print('[MELESET] %s %d char non-ASCII, TIDAK ditulis:'%(P,len(bad)))
    for i,h in bad[:8]: print('  baris %d %s'%(i,h))
    sys.exit(1)
os.makedirs(os.path.dirname(P),exist_ok=True)
old=open(P,encoding='utf-8').read() if os.path.isfile(P) else None
if old==txt: print('>>',P,'udah sama, skip'); sys.exit(0)
open(P,'w',encoding='utf-8',newline='\n').write(txt)
print('OK tulis %s (%d baris, ASCII, no-tab, no-trailing)'%(P,txt.count('\n')))
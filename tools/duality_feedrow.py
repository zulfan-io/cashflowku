import os,sys
P='src/pages/duality.vue'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
if 'feedRows' in t: sys.exit('udah baris, skip')
FEED_OLD='''.feed { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin: 10px 0 12px; }
@media (min-width: 640px) { .feed { grid-template-columns: repeat(auto-fill, minmax(170px, 1fr)); gap: 12px; } }'''
FEED_NEW='''.feedrow { margin: 8px 0; }
.feedrow .lbl { font-size: 13px; font-weight: 700; color: #1a1a1a; padding: 0 2px 4px; }
.feed { display: flex; gap: 10px; overflow-x: auto; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; scrollbar-width: none; margin: 4px 0; }
.feed::-webkit-scrollbar { display: none; }
.feed > * { flex: 0 0 auto; width: 30vw; max-width: 150px; scroll-snap-align: start; }'''
TPL_OLD='''    <main class="feed">
      <TransitionGroup name="rise">
        <CProductCardThin
          v-for="(p, i) in feed"
          :key="p.id"
          :product="p"
          class="rise-item"
          :style="{ transitionDelay: (i * 60) + 'ms' }"
          @select="onSelect"
          @love="onLove"
          @share="onShare"
          :love-count="loveCounts[p.id] || 0"
          :share-count="shareCounts[p.id] || 0"
        />
      </TransitionGroup>
    </main>'''
TPL_NEW='''    <section v-for="(row, ri) in feedRows" :key="ri" class="feedrow">
      <div class="lbl">{{ rowLabels[ri] || 'Rekomendasi' }}</div>
      <main class="feed">
        <CProductCardThin
          v-for="p in row"
          :key="p.id + '-' + ri"
          :product="p"
          @select="onSelect"
          @love="onLove"
          @share="onShare"
          :love-count="loveCounts[p.id] || 0"
          :share-count="shareCounts[p.id] || 0"
        />
      </main>
    </section>'''
CMP_OLD='const feed = ref(placeholderFeed())\nconst src = ref(\'demo\')'
CMP_NEW='''const feed = ref(placeholderFeed())
const src = ref('demo')
const rowLabels = ['Rekomendasi Untukmu', 'Produk Terlaris', 'Flash Sale', 'Baru Datang']
const feedAll = computed(() => { const f = feed.value; return f.length >= 15 ? f : [...f, ...f, ...f] })
const feedRows = computed(() => { const out = []; for (let i = 0; i < feedAll.value.length; i += 5) out.push(feedAll.value.slice(i, i + 5)); return out })'''
errs=[]
for o,n in [(FEED_OLD,FEED_NEW),(TPL_OLD,TPL_NEW),(CMP_OLD,CMP_NEW)]:
    c=t.count(o)
    if c!=1: errs.append('count=%d: %r'%(c,o[:30]))
    else:
        for ch in n:
            if ord(ch)>127: errs.append('non-ASCII: %r'%n[:30]); break
        t=t.replace(o,n)
if errs:
    print('[MELESET FEEDROW] TIDAK ditulis:'); [print('  ',e) for e in errs]; sys.exit(1)
if 'feedRows' not in t or '.feedrow' not in t: sys.exit('MELESET marker baris')
if 'grid-template-columns: repeat(2, 1fr)' in t: sys.exit('MELESET feed masih vertikal')
if t.count('position: fixed')!=1: sys.exit('MELESET botnav rusak')
if 'grid-auto-columns: 52px' not in t: sys.exit('MELESET widget belum kecil (jalankan widget tool dulu)')
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK feed baris horizontal',P)

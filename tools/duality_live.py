import os,sys
P='src/pages/duality.vue'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
if 'onMounted' in t: sys.exit('udah ke-patch, skip')
R=[
("import { ref, computed } from 'vue'\n",
 "import { ref, computed, onMounted } from 'vue'\nimport { supabase } from '~/utils/supabase'\n"),
("""const feed = ref([
  mk(1, 'Kemeja Flanel Oversize', 89000, 32, 1240, 4.8),
  mk(2, 'Celana Kargo Dewasa', null, 0, 870, 4.6),
  mk(3, 'Hoodie Fleece Premium', 135000, 14, 2100, 4.9),
  mk(4, 'Sepatu Sneakers Retro', 199000, 7, 540, 4.3),
  mk(5, 'Tas Ransel Anti Air', 159000, 21, 3300, 4.7),
  mk(6, 'Jam Tangan Digital Sport', 75000, 3, 410, 4.5)
])
feed.value[1].models = [
  { id: 2, sku: 'SKU2A', price: 120000, stock: 5, variation_index: [], is_default: false, product_id: 2 },
  { id: 3, sku: 'SKU2B', price: 150000, stock: 9, variation_index: [], is_default: true, product_id: 2 }
]""",
"""function placeholderFeed() {
  const f = [
    mk(1, 'Kemeja Flanel Oversize', 89000, 32, 1240, 4.8),
    mk(2, 'Celana Kargo Dewasa', null, 0, 870, 4.6),
    mk(3, 'Hoodie Fleece Premium', 135000, 14, 2100, 4.9),
    mk(4, 'Sepatu Sneakers Retro', 199000, 7, 540, 4.3),
    mk(5, 'Tas Ransel Anti Air', 159000, 21, 3300, 4.7),
    mk(6, 'Jam Tangan Digital Sport', 75000, 3, 410, 4.5)
  ]
  f[1].models = [
    { id: 2, sku: 'SKU2A', price: 120000, stock: 5, variation_index: [], is_default: false, product_id: 2 },
    { id: 3, sku: 'SKU2B', price: 150000, stock: 9, variation_index: [], is_default: true, product_id: 2 }
  ]
  return f
}
function mapOffer(o) {
  const price = o.price != null ? Number(o.price) : null
  return {
    id: o.id, name: o.title || 'Produk', image: o.image_url || null,
    sold: 0, rating: 0, price, stock: 0, variants: [], wholesale: [],
    models: price != null ? [{ id: o.id, sku: 'AFF' + o.id, price, stock: 0, variation_index: [], is_default: true, product_id: o.id }] : []
  }
}
const feed = ref(placeholderFeed())
const src = ref('demo')
onMounted(async () => {
  try {
    const { data, error } = await supabase
      .from('shoper_offers')
      .select('*')
      .eq('active', true)
      .limit(24)
    if (!error && data && data.length) {
      feed.value = data.map(mapOffer)
      src.value = 'live'
    }
  } catch (e) {}
})"""),
("      <span class=\"tag\">katalog affiliate + widget pintasan</span>\n",
 "      <span class=\"tag\">katalog affiliate + widget pintasan</span>\n      <span class=\"badge\" :class=\"src\">{{ src }}</span>\n"),
(".tag { font-size: 12px; color: #888; }\n",
 ".tag { font-size: 12px; color: #888; }\n.badge { margin-left: auto; font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 999px; letter-spacing: .5px; }\n.badge.demo { background: #FFE0C2; color: #B34700; }\n.badge.live { background: #D8F5DC; color: #1B7A2E; }\n"),
("  .tag { color: #999; }\n",
 "  .tag { color: #999; }\n  .badge.demo { background: #3a2410; color: #FFB877; }\n  .badge.live { background: #12301a; color: #7CE09A; }\n"),
]
for o,n in R:
    c=t.count(o)
    if c!=1: sys.exit('MELESET count=%d: %r'%(c,o[:30]))
    t=t.replace(o,n)
for ch in t:
    if ord(ch)>127: sys.exit('MELESET non-ASCII')
for m in ['onMounted','placeholderFeed','mapOffer','badge','</style>']:
    if m not in t: sys.exit('MELESET marker '+m)
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK patch',P)

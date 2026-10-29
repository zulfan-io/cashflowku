import os,sys
P='src/components/CProductCardThin.vue'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
if "emit('love'" in t: sys.exit('udah ada love/share, skip')
R=[
('const props = defineProps<{ product: Product }>()',
 'const props = defineProps<{ product: Product; loveCount?: number; shareCount?: number }>()'),
("const emit = defineEmits<{ (e: 'select', p: Product): void }>()",
 "const emit = defineEmits<{ (e: 'select', p: Product): void; (e: 'love', p: Product): void; (e: 'share', p: Product): void }>()"),
('      <div class="mt">\n        <span class="rt">{{ (props.product.rating || 0).toFixed(1) }}</span>\n        <span class="sd">{{ soldText }} terjual</span>\n      </div>',
 '      <div class="mt">\n        <span class="rt">{{ (props.product.rating || 0).toFixed(1) }}</span>\n        <span class="sd">{{ soldText }} terjual</span>\n      </div>\n      <div class="act">\n        <button class="act-b" @click.stop="emit(\'love\', props.product)">&#9825; {{ loveCount || 0 }}</button>\n        <button class="act-b" @click.stop="emit(\'share\', props.product)">&#8618; {{ shareCount || 0 }}</button>\n      </div>'),
('.pr { font-size: 15px; color: #FF6600; font-weight: 800; margin: 0; }',
 '.pr { font-size: 15px; color: #FF7A45; font-weight: 800; margin: 0; }'),
('</style>',
 '.act { display: flex; gap: 8px; margin-top: 6px; }\n.act-b { flex: 1; border: 1px solid #eee; background: #fafafa; border-radius: 8px; padding: 4px 0; font-size: 11px; color: #666; cursor: pointer; transition: background .15s, color .15s; }\n.act-b:active { background: #FFE9DF; color: #FF7A45; }\n</style>'),
]
errs=[]
for o,n in R:
    c=t.count(o)
    if c!=1: errs.append('count=%d: %r'%(c,o[:30]))
    else:
        for ch in n:
            if ord(ch)>127: errs.append('non-ASCII: %r'%n[:30]); break
        t=t.replace(o,n)
if errs:
    print('[MELESET CARD] TIDAK ditulis:'); [print('  ',e) for e in errs]; sys.exit(1)
if "#FF6600" in t: sys.exit('MELESET card masih #FF6600')
for m in ["emit('love'",'.act-b','#FF7A45']:
    if m not in t: sys.exit('MELESET marker card '+m)
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK card love/share+coral',P)

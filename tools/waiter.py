import os,sys,subprocess,json
IC='src/components/icons'; PV='src/pages/theme-preview.vue'
try: CFGD=json.load(open('src/data/icons.json',encoding='utf-8'))
except Exception as e: sys.exit('NGGAK BACA icons.json: %s'%e)
themes=CFGD.get('themes',{})
need=[]
for t in themes.values():
    for n in t.get('icons',[]):
        if n not in need: need.append(n)
miss=[n for n in need if not os.path.isfile(IC+'/'+n+'.vue')]
if miss: sys.exit('MELESET: nama di config NOL ada file -> %s'%miss)
if os.path.isfile(PV):
    ex=open(PV,encoding='utf-8').read()
    if 'const REG' in ex: sys.exit('udah tuas-fix (const REG ada), skip idempotent')
    # versi glob lama (NOL const REG) -> kita overwrite, NOL exit
imports='\n'.join("import %s from '~/components/icons/%s.vue'"%(n,n) for n in need)
reg='{ '+', '.join("'%s': %s"%(n,n) for n in need)+' }'
PC='''<!-- tuas -->
<script setup lang="ts">
import cfg from '~/data/icons.json'
'''+imports+'''
const REG = '''+reg+'''
function resolve(name: string) { return REG[name] || null }
const themes = (cfg as any).themes as Record<string, any>
</script>

<template>
  <div class="tw">
    <div class="tw-note">TUAS (import eksplisit, NOL glob/auto-import). Tiap blok = 1 tema dari icons.json. Tengah = DIPILIH (naik+nyala), lain = DIAM (abu). Merah = nama di config NOL ada file (cek menu waiter).</div>
    <div v-for="(t, tn) in themes" :key="tn" class="tw-card">
      <div class="tw-head"><span class="tw-name">{{ tn }}</span><span class="tw-desc">{{ t.desc }}</span></div>
      <div class="tw-row">
        <span v-for="(ic, ii) in t.icons" :key="ii" class="tw-ic" :class="{ on: ii === 2 }" :style="ii === 2 ? { color: t.palette[ii] } : { color: t.idle }">
          <component :is="resolve(ic)" v-if="resolve(ic)" />
          <em v-else class="tw-miss">{{ ic }}</em>
        </span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.tw { max-width: 480px; margin: 0 auto; padding: 24px 16px 80px; font-family: system-ui, sans-serif; color: #1a1a1a; background: #f7f7f7; min-height: 100vh; }
.tw-note { font-size: 12px; color: #888; line-height: 1.5; margin-bottom: 16px; }
.tw-card { background: #fff; border: 1px solid #eee; border-radius: 14px; padding: 14px 16px 18px; margin-bottom: 14px; }
.tw-head { display: flex; flex-direction: column; margin-bottom: 10px; }
.tw-name { font-size: 13px; font-weight: 700; color: #333; }
.tw-desc { font-size: 11px; color: #aaa; }
.tw-row { display: flex; gap: 22px; justify-content: center; }
.tw-ic { font-size: 30px; display: inline-flex; transition: transform .25s cubic-bezier(.34,1.56,.64,1), filter .2s, opacity .2s; }
.tw-ic.on { transform: translateY(-3px) scale(1.14); filter: drop-shadow(0 4px 7px rgba(0,0,0,.22)); }
.tw-miss { font-size: 10px; color: #e11d48; font-style: normal; }
</style>
'''
for ch in PC:
    if ord(ch)>127: sys.exit('MELESET non-ASCII PV')
if 'import.meta.glob' in PC: sys.exit('MELESET: glob nyelip lagi (versi fix harus NOL glob)')
for m in ('tuas','const REG','REG[name]','component :is','import cfg','tw-ic.on'):
    if m not in PC: sys.exit('MELESET marker '+m+' PV')
if PC.count('</template>')!=1 or PC.count('</style>')!=1: sys.exit('MELESET tag PV')
open(PV,'w',encoding='utf-8',newline='\n').write(PC)
print('OK tuas fix: import eksplisit', len(need), 'ikon ->', need)
r=subprocess.run(['ls',IC],capture_output=True,text=True)
files=sorted([f for f in r.stdout.split('\n') if f.endswith('.vue')])
print('=== MENU WAITER (folder lokal, NOL iconify) ===')
for i,f in enumerate(files,1): print('%3d. %s'%(i,f[:-4]))
print('=== lo teriak nomor per tema, gue config+registry ===')

import os,sys,json
CFG='src/data/icons.json'; PV='src/pages/theme-preview.vue'
WL={'IHome','ICart','IShop','INotify','IAccount','IStar','IHeart','IBasket','IApplication','ITime','ISearch','IProd','IOrder','IWishList'}
for f in (CFG,PV):
    if os.path.isfile(f):
        ex=open(f,encoding='utf-8').read()
        if 'tuas' in ex: sys.exit('udah tuas, skip')
        sys.exit('ABORT '+f+' ada bukan buatan gue')
CFGD={
  "_note":"TUAS tema shoper. Ganti palet/ikon di sini = ganti tema, NOL nyentuh kode. Nama ikon HARUS ada di src/components/icons/. Lapis4 (server) nyusul.",
  "themes":{
    "navbar-permen":{"desc":"navbar utama: hidup, warna-warni, candy","idle":"#9a9a9a","icons":["IHome","IShop","IApplication","INotify","IAccount"],"palette":["#FF6A2B","#2F6BFF","#7C4DFF","#FFB300","#00B894"]},
    "toko-elegan":{"desc":"toko/affiliate: tenang, monokrom restrained ala IG","idle":"#cbd5e1","icons":["IHome","IShop","IApplication","INotify","IAccount"],"palette":["#111827","#475569","#6B7280","#78716C","#52525B"]},
    "widget-serius":{"desc":"widget kategori affiliate: tegas, warna fungsi","idle":"#94a3b8","icons":["IStar","IHeart","IBasket","IApplication","ITime"],"palette":["#0D9488","#E11D48","#D97706","#4F46E5","#0284C7"]}
  }
}
for tn,t in CFGD["themes"].items():
    for n in t["icons"]:
        if n not in WL: sys.exit('MELESET nama %s di tema %s (NOL ada di whitelist harta lo)'%(n,tn))
    if len(t["icons"])!=len(t["palette"]): sys.exit('MELESET %s icons!=palette'%(tn))
CJS=json.dumps(CFGD,indent=2,ensure_ascii=False)
for ch in CJS:
    if ord(ch)>127 and ch not in 'éü': pass
if any(ord(ch)>127 for ch in CJS): sys.exit('MELESET non-ASCII di config')
os.makedirs('src/data',exist_ok=True)
open(CFG,'w',encoding='utf-8',newline='\n').write(CJS+'\n')
PC='''<!-- tuas -->
<script setup lang="ts">
import cfg from '~/data/icons.json'
const files = import.meta.glob('../components/icons/*.vue', { eager: true }) as Record<string, { default: any }>
function resolve(name: string) {
  const key = Object.keys(files).find((k) => k.endsWith('/' + name + '.vue'))
  return key ? files[key].default : null
}
const themes = (cfg as any).themes as Record<string, any>
</script>

<template>
  <div class="tw">
    <div class="tw-note">TUAS tema. Tiap blok = 1 tema dari icons.json. Ganti palet/ikon di config = ganti tema, NOL nyentuh kode. Tengah = DIPILIH (naik+nyala), lain = DIAM (abu). Slot kosong = nama ikon NOL ada di folder (cek whitelist).</div>
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
for m in ('tuas','icons.json','import.meta.glob','resolve(ic)','tw-ic.on'):
    if m not in PC: sys.exit('MELESET '+m+' PV')
if PC.count('</template>')!=1 or PC.count('</style>')!=1: sys.exit('MELESET tag PV')
open(PV,'w',encoding='utf-8',newline='\n').write(PC)
print('OK tuas: config', CFG, '+ preview', PV, '| tema:', list(CFGD['themes'].keys()))

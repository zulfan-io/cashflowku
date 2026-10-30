import os,sys,re,json
IC='src/components/icons'; PV='src/pages/theme-preview.vue'; CFG='src/data/icons.json'
PAL={
 'IHome':('#FFB38A','#FF6A2B'),'IShop':('#9CC4FF','#2F6BFF'),'IApplication':('#C4B0FF','#7C4DFF'),
 'INotify':('#FFE0A3','#FFB300'),'IAccount':('#A7F3D9','#00B894'),'IStar':('#FFD9A8','#F59E0B'),
 'IHeart':('#FFB3C7','#EC4899'),'IBasket':('#FFC9A8','#EA580C'),'ITime':('#A8D8FF','#0EA5E9'),
}
try: CFGD=json.load(open(CFG,encoding='utf-8'))
except Exception as e: sys.exit('NGGAK BACA icons.json: %s'%e)
themes=CFGD.get('themes',{})
if not themes: sys.exit('config NOL themes')
def body_of(nm):
    P=IC+'/'+nm+'.vue'
    if not os.path.isfile(P): sys.exit('MELESET file NOL ada: '+nm)
    t=open(P,encoding='utf-8').read()
    m=re.search(r'<svg[\s\S]*?</svg>',t)
    if not m: sys.exit('MELESET NOL <svg> di '+nm)
    s=m.group(0).replace('"',"'").replace('#','%23')
    s=re.sub(r'\s+',' ',s).strip()
    return 'url("data:image/svg+xml,%s")'%s
need=[]
for tn,t in themes.items():
    new=[]
    for slot in t.get('icons',[]):
        nm=slot if isinstance(slot,str) else slot.get('n')
        if nm not in need: need.append(nm)
        if nm not in PAL: sys.exit('MELESET %s NOL di palet default (tambahin PAL atau ganti nama)'%nm)
        if isinstance(slot,dict) and 'm' in slot:
            new.append(slot); continue
        lt,bs=PAL[nm]
        new.append({'n':nm,'lite':lt,'base':bs,'m':body_of(nm)})
    t['icons']=new
if os.path.isfile(PV):
    ex=open(PV,encoding='utf-8').read()
    if 'tw-grad' in ex: sys.exit('udah grad2, skip idempotent')
imports='\n'.join("import %s from '~/components/icons/%s.vue'"%(n,n) for n in need)
reg='{ '+', '.join("'%s': %s"%(n,n) for n in need)+' }'
HEAD='''<!-- tw-grad -->
<script setup lang="ts">
import { ref } from 'vue'
import cfg from '~/data/icons.json'
'''
MID='''
const REG = '''+reg+'''
function comp(name: string) { return REG[name] || null }
const themes = (cfg as any).themes as Record<string, any>
const act = ref<Record<string, number>>(Object.fromEntries(Object.keys(themes).map((k) => [k, 2])))
</script>

<template>
  <div class="tw">
    <div class="tw-note">2-WARNA via mask (gradient di BADAN ikon, BUKAN 3D). TEKEN = aktif (2-tone + glow + naik), lain = DIAM (abu flat). Warna = lite/base di icons.json, ganti 1 baris hex = ganti rasa.</div>
    <div v-for="(t, tn) in themes" :key="tn" class="tw-card">
      <div class="tw-head"><span class="tw-name">{{ tn }}</span><span class="tw-desc">{{ t.desc }} - teken ganti aktif</span></div>
      <div class="tw-row">
        <button v-for="(ic, ii) in t.icons" :key="ii" class="tw-ic" :class="{ on: act[tn] === ii }"
          :style="{ '--m': ic.m, '--lite': act[tn] === ii ? ic.lite : t.idle, '--base': act[tn] === ii ? ic.base : t.idle, color: act[tn] === ii ? ic.base : t.idle }"
          @click="act[tn] = ii"></button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.tw { max-width: 480px; margin: 0 auto; padding: 24px 16px 80px; font-family: system-ui, sans-serif; color: #1a1a1a; background: #f7f7f7; min-height: 100vh; }
.tw-note { font-size: 12px; color: #888; line-height: 1.5; margin-bottom: 16px; }
.tw-card { background: #fff; border: 1px solid #eee; border-radius: 14px; padding: 14px 16px 18px; margin-bottom: 14px; }
.tw-head { display: flex; flex-direction: column; margin-bottom: 12px; }
.tw-name { font-size: 13px; font-weight: 700; color: #333; }
.tw-desc { font-size: 11px; color: #aaa; }
.tw-row { display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; }
.tw-ic { border: 0; background: transparent; cursor: pointer; width: 30px; height: 30px; padding: 0; display: inline-flex; -webkit-mask: var(--m) center / contain no-repeat; mask: var(--m) center / contain no-repeat; background: linear-gradient(180deg, var(--lite), var(--base)); transition: transform .26s cubic-bezier(.34,1.56,.64,1), filter .22s, opacity .2s; }
.tw-ic:not(.on) { opacity: .55; }
.tw-ic.on { transform: translateY(-3px) scale(1.16); filter: drop-shadow(0 5px 10px currentColor); }
</style>
'''
PC=HEAD+MID
bad=[(i,PC[i]) for i in range(len(PC)) if ord(PC[i])>127]
if bad:
    print('=== NON-ASCII KETEMU (guard nunjukin, bukan nge-block buta) ===')
    for i,ch in bad[:10]:
        ctx=PC[max(0,i-25):i]+'>>'+ch+'<<'+PC[i+1:i+26]
        print('pos=%d ord=%d char=%r | konteks: %s'%(i,ord(ch),ch,ctx))
    sys.exit('MELESET non-ASCII PV (liat posisi di atas = byte-nya, bukan tebakanku)')
if 'import.meta.glob' in PC: sys.exit('MELESET: glob nyelip')
MK=('tw-grad','const REG','@click','act[tn] = ii','linear-gradient(180deg, var(--lite), var(--base))','-webkit-mask: var(--m)',"'--m': ic.m")
miss=[m for m in MK if m not in PC]
if miss:
    print('=== HASIL CEK MARKER PC (True=ada, False=hilang) ===')
    for m in MK: print('  %-55s %s'%(m[:55], 'OK' if m in PC else 'HILANG'))
    sys.exit('MELESET marker PC hilang: %s'%miss)
if PC.count('</template>')!=1 or PC.count('</style>')!=1: sys.exit('MELESET tag PV')
# cek CONFIG terpisah: data-URI mask HARUS ada di config (bukan PC) - ini perbaikan salah-alamat dosa-31
cm=0
for tn,t in themes.items():
    for slot in t['icons']:
        if not (isinstance(slot,dict) and str(slot.get('m','')).startswith('url("data:image/svg+xml,')):
            sys.exit('MELESET config: slot %s di %s NOL data-URI mask (body_of gagal?)'%(slot.get('n'),tn))
        cm+=1
print('CONFIG OK: %d slot punya data-URI mask (data-URI = di config, BUKAN PC)'%cm)
open(CFG,'w',encoding='utf-8',newline='\n').write(json.dumps(CFGD,indent=2,ensure_ascii=False)+'\n')
open(PV,'w',encoding='utf-8',newline='\n').write(PC)
print('OK grad2: 2-warna mask ASCII-clean, ikon:', len(need), '| tema:', list(themes.keys()))
print('ganti warna contoh (lo pegang tuas, NOL nyentuh kode):')
print("  sed -i 's/#FFB38A/#6EE7B7/; s/#FF6A2B/#10B981/' src/data/icons.json && git add src/data/icons.json && git commit -m demo && git push")

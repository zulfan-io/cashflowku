import os,sys,subprocess,json
IC='src/components/icons'; PV='src/pages/ph-preview.vue'
NAMES=[('IPhHouse','house-fill'),('IPhCart','shopping-cart-fill'),('IPhGrid','squares-four-fill'),('IPhBell','bell-fill'),('IPhUser','user-fill')]
def fetch(slug):
    url='https://api.iconify.design/ph/%s.json'%slug
    try:
        r=subprocess.run(['curl','-s','--max-time','20',url],capture_output=True,text=True)
    except FileNotFoundError:
        sys.exit('CURL NOL ADA di Termux lo, install: pkg install curl')
    if r.returncode!=0: sys.exit('CURL GAGAL %s rc=%d'%(slug,r.returncode))
    if not r.stdout.strip(): sys.exit('API KOSONG %s (nama salah? network?)'%slug)
    try: d=json.loads(r.stdout)
    except Exception: sys.exit('API NON-JSON %s: %r'%(slug,r.stdout[:80]))
    if 'body' not in d: sys.exit('API NOL body %s -> %r'%(slug,str(d)[:80]))
    return d
made=[]
for nm,slug in NAMES:
    P=IC+'/'+nm+'.vue'
    if os.path.isfile(P):
        ex=open(P,encoding='utf-8').read()
        if 'ph-fetch' in ex: continue
        sys.exit('ABORT '+P+' ada bukan ph')
    d=fetch(slug)
    vb=d.get('viewBox','0 0 256 256'); w=d.get('width','1em'); h=d.get('height','1em')
    body=d['body'].strip()
    if 'currentColor' not in body: sys.exit('MELESET %s NOL currentColor (warna mati!)'%slug)
    svg='<svg xmlns="http://www.w3.org/2000/svg" width="%s" height="%s" viewBox="%s">%s</svg>'%(w,h,vb,body)
    C='<!-- ph-fetch -->\n<template>\n  '+svg+'\n</template>\n'
    for ch in C:
        if ord(ch)>127: sys.exit('MELESET non-ASCII '+nm)
    if C.count('</template>')!=1: sys.exit('MELESET tag '+nm)
    open(P,'w',encoding='utf-8',newline='\n').write(C); made.append(nm)
imports='\n'.join("import %s from '~/components/icons/%s.vue'"%(n,n) for n,_ in NAMES)
arr='const icons = [%s]'%', '.join(n for n,_ in NAMES)
PC='''<!-- ph-fetch -->
<script setup lang="ts">
'''+imports+'''
'''+arr+'''
const cols = ['#FF6A2B', '#2F6BFF', '#7C4DFF', '#FFB300', '#00B894']
</script>

<template>
  <div class="ph">
    <div class="ph-note">Phosphor fill, ditarik dari API iconify (NOL nebak koordinat). Baris 1 = SEMUA DIAM (abu, tenang ala IG). Baris 2 = palet 5 warna serumah. Baris 3 = simulasi navbar, tengah DIPILIH (warna + naik + nyala, hidup ala candy). Lo nilai rasa, terus gue colok duality.</div>
    <div class="ph-lab">DIAM (inactive)</div>
    <div class="ph-row ph-idle">
      <span v-for="(ic,ii) in icons" :key="ii" class="ph-ic"><component :is="ic" /></span>
    </div>
    <div class="ph-lab">PALET (5 warna serumah)</div>
    <div class="ph-row">
      <span v-for="(ic,ii) in icons" :key="ii" class="ph-ic" :style="{ color: cols[ii] }"><component :is="ic" /></span>
    </div>
    <div class="ph-lab">NAVBAR SIMULASI (tengah dipilih)</div>
    <div class="ph-row ph-nav">
      <span v-for="(ic,ii) in icons" :key="ii" class="ph-ic" :class="{ on: ii === 2 }" :style="ii === 2 ? { color: cols[ii] } : {}"><component :is="ic" /></span>
    </div>
  </div>
</template>

<style scoped>
.ph { max-width: 480px; margin: 0 auto; padding: 24px 16px 80px; font-family: system-ui, sans-serif; color: #1a1a1a; background: #f7f7f7; min-height: 100vh; }
.ph-note { font-size: 12px; color: #888; line-height: 1.5; margin-bottom: 16px; }
.ph-lab { font-size: 11px; color: #aaa; letter-spacing: .5px; margin: 10px 0 4px; }
.ph-row { display: flex; gap: 22px; justify-content: center; padding: 18px; background: #fff; border: 1px solid #eee; border-radius: 14px; }
.ph-nav { background: #fff; border-top: 1px solid #eee; border-radius: 0 0 14px 14px; }
.ph-ic { font-size: 30px; display: inline-flex; transition: transform .25s cubic-bezier(.34,1.56,.64,1), filter .2s, opacity .2s; }
.ph-idle .ph-ic { color: #9a9a9a; opacity: .5; filter: grayscale(1); }
.ph-ic.on { transform: translateY(-3px) scale(1.14); filter: drop-shadow(0 4px 7px rgba(0,0,0,.22)); }
</style>
'''
for ch in PC:
    if ord(ch)>127: sys.exit('MELESET non-ASCII PV')
for m in ('ph-fetch','IPhHouse from','IPhUser from','component :is','ph-idle','ph-ic.on'):
    if m not in PC: sys.exit('MELESET '+m+' PV')
if PC.count('</template>')!=1 or PC.count('</style>')!=1: sys.exit('MELESET tag PV')
open(PV,'w',encoding='utf-8',newline='\n').write(PC)
print('OK ph-fetch: bikin', made or '(5 udah ada)', '| preview', PV)

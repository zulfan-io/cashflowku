import os,sys
ENV='.env'
CLI='src/utils/supabase.js'
URL='https://vwthbjuowhhvldxlhhtp.supabase.co'
KEY='sb_publishable_y6z4LSsFf1wICpdSFI8hxQ_W2GpDJ5u'
# .env: merge-safe, buang baris VITE_SUPABASE_* lama, tambah yang baru, sisanya utuh.
old=[]
if os.path.isfile(ENV):
    old=[l for l in open(ENV,encoding='utf-8').read().split('\n') if l and not l.startswith('VITE_SUPABASE_')]
new=old+['VITE_SUPABASE_URL='+URL,'VITE_SUPABASE_ANON_KEY='+KEY]
env_txt='\n'.join(new)+'\n'
# supabase.js: pola sama kayak axios-instance lo (import.meta.env), guard biar nggak mati senyap.
cli_txt='''import { createClient } from '@supabase/supabase-js'

const url = import.meta.env.VITE_SUPABASE_URL
const key = import.meta.env.VITE_SUPABASE_ANON_KEY
if (!url || !key) throw new Error('VITE_SUPABASE_URL / VITE_SUPABASE_ANON_KEY kosong - cek .env')

export const supabase = createClient(url, key)
'''
def chk(name,txt):
    bad=[(i,hex(ord(c))) for i,l in enumerate(txt.split('\n'),1) for c in l if ord(c)>127]
    if bad:
        print('[MELESET] %s non-ASCII:'%name)
        for i,h in bad[:8]: print('  baris %d %s'%(i,h))
        sys.exit(1)
chk('.env',env_txt); chk(CLI,cli_txt)
os.makedirs(os.path.dirname(CLI),exist_ok=True)
oe=open(ENV,encoding='utf-8').read() if os.path.isfile(ENV) else None
oc=open(CLI,encoding='utf-8').read() if os.path.isfile(CLI) else None
if oe==env_txt and oc==cli_txt: print('>> udah sama, skip'); sys.exit(0)
open(ENV,'w',encoding='utf-8',newline='\n').write(env_txt)
open(CLI,'w',encoding='utf-8',newline='\n').write(cli_txt)
print('OK tulis',ENV,'+',CLI,'(client netral, publishable key, guard anti-senyap)')
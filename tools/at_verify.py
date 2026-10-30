import re,sys
P='supabase/functions/accesstrade/index.ts'
s=open(P,encoding='utf-8').read()
CH=[
 ('serve=Deno.serve (no pinned std import)','Deno.serve(' in s),
 ('JWT alg HS256','alg: "HS256"' in s),
 ('payload sub=UID','sub: UID' in s),
 ('payload iat epoch','iat:' in s),
 ('sign HMAC SHA-256 via subtle','crypto.subtle.sign("HMAC"' in s),
 ('header X-Accesstrade-User-Type','X-Accesstrade-User-Type' in s),
 ('base gurkha.accesstrade.global','https://gurkha.accesstrade.global' in s),
 ('wire path /creatives/custom','/creatives/custom' in s),
 ('UID dari vault (bukan literal)','Deno.env.get("ACCESSTRADE_USER_UID")' in s),
 ('KEY dari vault (bukan literal)','Deno.env.get("ACCESSTRADE_SECRET_KEY")' in s),
 ('CORS preflight OPTIONS','"OPTIONS"' in s),
 ('ANTI-LEAK: no MD5/password di hot fn','MD5(' not in s),
 ('ANTI-LEAK: UID/KEY cm env-get','const UID = Deno.env.get' in s and 'const KEY = Deno.env.get' in s),
 ('ANTI-LEAK: no long secret literal',not re.search(r'(UID|KEY)\s*=\s*"[A-Za-z0-9_\-]{16,}"',s)),
]
fail=0
for i,(nm,ok) in enumerate(CH,1):
    print('%2d %-44s %s'%(i,nm,'PASS' if ok else 'FAIL')); fail+= 0 if ok else 1
print('VERDICT:', 'ALL PASS - fn patuh doc + invariant §1' if fail==0 else '%d FAIL - JANGAN deploy'%fail)
sys.exit(1 if fail else 0)

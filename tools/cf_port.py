import os,sys
R='/*  /index.html  200\n'
H='/manifest.webmanifest\n  Content-Type: application/manifest+json\n'
os.makedirs('public',exist_ok=True)
for fn,body in [('_redirects',R),('_headers',H)]:
    p='public/'+fn
    if os.path.isfile(p) and open(p,encoding='utf-8').read()==body:
        print('>>',fn,'udah bener, skip'); continue
    open(p,'w',encoding='utf-8').write(body)
    print('OK tulis',p,'(%d byte)'%len(body))
print('vite auto-copy public/* -> dist/, Cloudflare baca dist/_redirects + dist/_headers')
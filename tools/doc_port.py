import os,sys
MARK='<!-- PORT-MANIFEST v1 -->'
BODY=MARK+"""
## VISI PORT-COLOK (dualitas + database)
- DUALITAS UI: feed-bawah = kartu AFFILIATE (accesstrade); floating = GRID WIDGET ala Shopee (max 8 slot). Gadget & web ikut e-commerce, smooth semulus bulu.
- REWARD: poin game -> PULSA GRATIS khusus dari owner. Database = nyawa.
- TANGKEP MEMBER: email + HP + OTP = member = database berharga (kampanye ngumpulin data).
- PORT/MANIFEST: campaign/game/network BARU = tambah objek di src/data/ports.json, NOL nyentuh kode = "tinggal nyambungin port".
- SUMBER EKSTERNAL: accesstrade (affiliate), games-gratis (provider embed), voucher pulsa/marketplace (shopee/blibli/tiktok/lazada).
- SETTINGAN: sistem port siap-panggil, klien klik kayak production besar (shopee/lazada).
- STATUS JUJUR: manifest = REL KOSONG. DOM BELUM KEBUKTI (build 1m41s belum green). Platform-free: menang di CF/Netlify/apa pun, tinggal colok.
"""
for p in ['csttan.md','LEGODONE.md']:
    if not os.path.isfile(p): print('>>',p,'NGGAK ADA, skip (bukan error, file emang belum ada)'); continue
    s=open(p,encoding='utf-8').read()
    if MARK in s: print('>>',p,'udah ke-append, skip'); continue
    open(p,'a',encoding='utf-8').write(('\n' if not s.endswith('\n') else '')+BODY+'\n')
    print('OK append',p)
print('>> doc nampung visi lo, manifest berikutnya = isi rel-nya')
import os,sys
P='LEGODONE.md'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P+' (jalanin dari ~/cashflowku)')
t=open(P,encoding='utf-8').read()
if 'GUNUNG 8' in t: sys.exit('udah ke-simpan, skip')
B=chr(9744); C=chr(9745); AR=chr(8594); D=chr(8212); M=chr(183)
L=[
'## GUNUNG 8 '+D+' SOSMED COMMERCE (2 demo '+M+' ramu Coi 13:00)',
'> Yin-yang Coi: '+AR+' commerce berjiwa social. 2 demo = 2 sisi sumbu, BUKAN 2 rasa beda.',
'',
'### DEMO 1 '+D+' SOCIAL COMMERCE (/sc1) '+M+' panggung = orang',
'- '+B+' hero = rail story bulat (24 jam, wajah/preview) '+AR+' feed post orang, produk numpang di dalam post',
'- '+B+' navbar ikon-saja (Instagram): aktif filled, notif = titik merah',
'- '+B+' dot posisi carousel '+M+' '+B+' love/share = verb utama post',
'',
'### DEMO 2 '+D+' COMMERCE SOCIAL MEDIA (/sc2) '+M+' panggung = barang, berbahasa tenang',
'- '+B+' hero = katalog produk (baris duality) '+AR+' tiap card dipakaikan furniture social',
'- '+B+' seller story-circle di card '+M+' '+AR+' '+B+' '+C+' backend story 24 jam SUDAH ADA (shoper_status.expires_at + RLS)',
'- '+B+' navbar ikon+label (Duolicious) '+M+' '+AR+' '+B+' dot posisi + notif titik hidup di sini juga',
'',
'### PRIMITIF SHARED (dipakai 2 demo, 1 sumber truth)',
'- '+B+' StoryCircle.vue '+M+' bulat, wajah/preview, tap '+AR+' story 24 jam (frontend BELUM dibangun)',
'- '+B+' Dots.vue '+M+' indikator posisi carousel',
'- '+B+' NotifDot.vue '+M+' titik merah, bukan teks',
'- '+C+' backend story = shoper_status (expires_at now()+1day, RLS > now(), purge) '+M+' SUDAH jadi di DB',
'',
'### ATURAN RAMU',
'- '+B+' 2 demo NOL nyentuh duality.vue / list.vue yang udah hidup '+M+' file baru /sc1 /sc2',
'- '+B+' yin-yang = KOMPOSISI primitif, bukan CSS baru '+M+' rasa tenang dijaga di 2 sisi',
'- '+B+' gate Coi: acc split sc1/sc2 di atas '+AR+' bilang "gas sc" '+AR+' AI tulis 2 page + 3 primitif dari byte',
]
SEC='\n'.join(L)+'\n'
ki=t.find('RINGKAS')
if ki!=-1:
    ls=t.rfind('\n',0,ki)+1
    t2=t[:ls]+SEC+t[ls:]
else:
    t2=t.rstrip('\n')+'\n\n'+SEC
if 'GUNUNG 8' not in t2 or 'StoryCircle' not in t2: sys.exit('MELESET insert')
open(P,'w',encoding='utf-8',newline='\n').write(t2)
print('OK legodone +GUNUNG 8 (', SEC.count(B),'kotang baru )')

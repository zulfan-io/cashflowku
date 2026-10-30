#  LEGODONE — 1 LEMBAR STATUS (dipanggil via $legodone, privat di git)
> Ringkasan 1 layar. Detail = csttan.md. Centang di sini = niat; centang di csttan = bukti.

## FRIDA — 1 rumah 1 gerbang
- ☑ parkir, hukum lo dipegang
- ☐ tombol CONVERT — re-probe anchor LIVE (→ §7)

## SHOPER — shoper-co.netlify.app (LIVE, privat vault)
- ☑ 8 batu nembus: ranjau vitest → node18 → iconify → swiper(skip SSR) → deploy LIVE
- ☑ rebrand shoper (teks/merah/logo/aset/hero/CGift/hide mockup)
- ☑ GUNUNG 1 DB OFFER AFFILIATE - skema nunggu byte ACCESSTRADE (lihat 8)
- ☑ GUNUNG 2 API (part1 fixture+kartu) — beneran ganti fixture (→ §8)
- ☐ GUNUNG 1.5 KATALOG tp-o.tk — adapter+fixture+debug kelar (cc8e3f5); skema TS + colok halaman nyusul
- ☐ GUNUNG 3 SEO/SSR — ssr.noExternal swiper, verify codespace dulu (→ §8)
- ☐ GUNUNG 4 Automation Meta — tunggu API hidup (→ §8)
- ☐ GUNUNG 5 SEM — JANGAN sentuh smp 1-4 hijau (→ §8)
- ☐ GUNUNG 6 Affiliate/terkenal — distribusi > fitur (→ §8)
- ☐ domain custom shoper.co/.id — 10 menit UI, BESOK (→ §8)

## NEXT PROJECT
- ☐ quack-fire-2d — codespace lo udah ada (catet dari gh list ronde awal)

## 🔫 ARSENAL API ACCESSTRADE — "gua disini, ini senjata gue"
> Ini bukan tempelan doc. Ini suara gua yang ngomong: endpoint mana yang gua pegang, mana yang gua tunggu, dan gimana gua rakitnya jadi shoper. Basis: https://gurkha.accesstrade.global (ID/SG/MY). Thailand/Vietnam beda — gua nggak pake.

### 1. AUTH CHAIN — 3 langkah yang bikin 90% dev affiliate mental di hari pertama (gua udah lewatin)
- Langkah A (provisioning): `GET /publishers/auth/{email}` → header `Authorization: SHA256(email+':'+MD5(password))` → return `{ userUid, secretKey, accountId }`.
- Langkah B (bikin JWT): HS256. Header `{alg:'HS256'}`. Payload `{ sub: userUid, iat: epochDetik }`. Tanda tangan pake `secretKey` dari Langkah A.
- Langkah C (setiap request): header `Authorization: Bearer <jwt>` + `X-Accesstrade-User-Type: publisher`.
- >> CATATAN KESELAMATAN (FRIDA gua): `secretKey` ROTATE otomatis pas gua ganti password ACCESSTRADE. Jadi token bocor semalem = MATI. Dan `secretKey`/JWT **HARAM** ada di front-end — mereka hidup di **Netlify env var**, dipanggil lewat Serverless Function. Browser gua NELEPON API langsung = CORS gagal + key bocor. Gua nggak ngulang vulnerability gua ke produk gua sendiri.

### 2. SET-UP PROPERTI — Website APIs (LENGKAP di doc gua, ini yang gua eksekusi duluan)
- List: `GET /v1/publishers/me/sites` · Detail: `GET /v1/publishers/me/sites/{id}` · Create: `PUT /v1/publishers/me/sites` (return `{id}`) · Update: `PUT` (body sama + `id`) · Delete: `DELETE /v1/publishers/me/sites/{id}`.
- Pilihan enum buat shoper-co.netlify.app (gua yang putusin, doc cuma nawar):
  - `type`: **CASHBACK** atau **COUPON** (visi gua "card semua brand affiliate" = dua-duanya sah; >> GUA HARUS PILIH 1 sebelum create).
  - `categories`: **maks 2** (constraint doc — gua nggak bisa spam; kandidat: E-commerce + Games).
  - `traffic`: ORGANIC_SEARCH (target SEO gua) / lainnya.
  - `leadGeneration`: CASHBACK / PRICE_COMPARISON / PRODUCT_AND_SERVICE_REVIEW.
- Status site: REVIEWING → APPROVED / REJECTED / DELETED. Gua daftarin, gua tunggu APPROVED, baru gua tembak.

### 3. ALUR "GUA GINIIN DAN JADILAH" — 5 langkah, jujur berhenti di yang kebukti
1. Gua daftarin properti shoper-co.netlify.app via `PUT sites` (type + 2 kategori) → status REVIEWING.
2. Gua auth: provisioning → JWT → Bearer. (semua di Netlify function, bukan browser.)
3. Gua tarik daftar campaign → masukin skema `affiliateOffer` → render CGiftRow/CGiftCards. **[PEGANG: Campaign API belum di doc]**
4. Gua generate link ter-track → pasang di tombol melayang `CFloatLink`. **[PEGANG: Link Generation API belum di doc]**
5. Gua track klik→konversi (sub-id) → komisi → `totalpayment`. **[PEGANG: Conversion/Report API belum di doc]**
- >> JADILAH: shoper bukan demo UI lagi — dia mesin klik-out yang ngomong langsung ke ACCESSTRADE, pake senjata yang gua pegang di atas.

### 4. HUTANG NARASI (yang belum bisa gua omongin karena belum ada byte-nya)
- [PEGANG] Campaign API (list/filter offer)
- [PEGANG] Link Generation / Custom Link API (jantung widget floating)
- [PEGANG] Conversion / Report API (atribusi komisi)
- Aturan: gua NOL cor kode buat langkah 3-5 sampe 3 byte ini ada di doc. Struktur ini berhenti ngomong di sini, bukan ngarang.
<!-- PORT-MANIFEST v1 -->
## VISI PORT-COLOK (dualitas + database)
- DUALITAS UI: feed-bawah = kartu AFFILIATE (accesstrade); floating = GRID WIDGET ala Shopee (max 8 slot). Gadget & web ikut e-commerce, smooth semulus bulu.
- REWARD: poin game -> PULSA GRATIS khusus dari owner. Database = nyawa.
- TANGKEP MEMBER: email + HP + OTP = member = database berharga (kampanye ngumpulin data).
- PORT/MANIFEST: campaign/game/network BARU = tambah objek di src/data/ports.json, NOL nyentuh kode = "tinggal nyambungin port".
- SUMBER EKSTERNAL: accesstrade (affiliate), games-gratis (provider embed), voucher pulsa/marketplace (shopee/blibli/tiktok/lazada).
- SETTINGAN: sistem port siap-panggil, klien klik kayak production besar (shopee/lazada).
- STATUS JUJUR: manifest = REL KOSONG. DOM BELUM KEBUKTI (build 1m41s belum green). Platform-free: menang di CF/Netlify/apa pun, tinggal colok.

## GUNUNG 8 — SOSMED COMMERCE (2 demo · ramu Coi 13:00)
> Yin-yang Coi: → commerce berjiwa social. 2 demo = 2 sisi sumbu, BUKAN 2 rasa beda.

### DEMO 1 — SOCIAL COMMERCE (/sc1) · panggung = orang
- ☑ hero = rail story bulat (24 jam, wajah/preview) → feed post orang, produk numpang di dalam post
- ☑ navbar ikon-saja (Instagram): aktif filled, notif = titik merah
- ☑ dot posisi carousel · ☐ love/share = verb utama post

### DEMO 2 — COMMERCE SOCIAL MEDIA (/sc2) · panggung = barang, berbahasa tenang
- ☑ hero = katalog produk (baris duality) → tiap card dipakaikan furniture social
- ☑ seller story-circle di card · → ☐ ☑ backend story 24 jam SUDAH ADA (shoper_status.expires_at + RLS)
- ☑ navbar ikon+label (Duolicious) · → ☐ dot posisi + notif titik hidup di sini juga

### PRIMITIF SHARED (dipakai 2 demo, 1 sumber truth)
- ☑ StoryCircle.vue · bulat, wajah/preview, tap → story 24 jam (frontend BELUM dibangun)
- ☑ Dots.vue · indikator posisi carousel
- ☑ NotifDot.vue · titik merah, bukan teks
- ☑ backend story = shoper_status
- ☐ story viewer penuh (swipe/progress/posting dari shoper_status) = GELOMBANG C, NOL nebak scope (expires_at now()+1day, RLS > now(), purge) · SUDAH jadi di DB

### ATURAN RAMU
- ☑ 2 demo NOL nyentuh duality.vue / list.vue yang udah hidup · file baru /sc1 /sc2
- ☑ yin-yang = KOMPOSISI primitif, bukan CSS baru · rasa tenang dijaga di 2 sisi
- ☑ gate Coi: acc split sc1/sc2 di atas → bilang "gas sc" → AI tulis 2 page + 3 primitif dari byte
## MASUKAN COI - log ide SEBELUM ngoding (rule Coi)
> Aturan: tiap masukan positif soal projek -> kesini dulu, baru gue ngoding. Inbox mentah, bukan task bercentang.

- 2026-10-29 19:27 :: RULE META: tiap masukan positif soal projek -> log ke MASUKAN ini dulu, BARU ngoding. Inbox mentah != task bercentang.
- 2026-10-29 19:27 :: YIN-YANG Coi (2 sumbu): APA = commerce<->social ; BAHASA = teriak<->tenang. Shoper = commerce BERBAHASA social. Pamer lewat angka+simbol+ruang kosong, BUKAN badge teriak. 2 fork referensi: Instagram (navbar ikon-saja) + Duolicious (ikon+label, foto overlay) -> diwujudkan sc1/sc2.
- 2026-10-29 19:27 :: FUNNEL psikologis (3 angka 1 napas): etalase duality = 4x5=20 card, plafon KELIHATAN (setengah-infinity; orang belum commit -> melimpah tapi terkendali). Masuk /list = infinity cap 100 (100 = FINIS bukan plafon toko; closure = otak suka garis akhir). Next = BAB berikutnya (100 = ukuran gigitan, bukan ukuran toko).
- 2026-10-29 19:27 :: DEFINISI 'rapi' Coi: route jelas (file-based, NOL dynamic-nebak); .bak = git commit (NOL file sampah); struktur script->template->style konsisten; indent 2 spasi; lang=ts WAJIB kalau ada TS di script (dosa sc1 indent-1 + dosa lang=ts build merah = pelajaran).
- 2026-10-29 19:27 :: SPESIFIKASI MEDIA sosial: video dibatasi beberapa detik + dikompres (RAM/MB Supabase gak bengkak), foto juga. Hapus otomatis 1 hari = cron BENERAN delete (bukan cuma sembunyi via RLS).
- 2026-10-29 19:27 :: SHARE+LOVE lintas kampanye: share nempel ke SEMUA objek (produk/game/affiliate/status), bukan cuma status. Love WAJIB tercatat & bisa diliat PUBLIK (anon) biar orang tau 'love kesebar berapa'. Backend udah jadi (shoper_loves/shares + trigger recount).
- 2026-10-29 19:27 :: STORY 24 jam = FEEL penting. Bulat = wajah/preview gambar (affordance universal; IG & Duolicious pake). Tap = viewer. Gelombang C (belum): swipe antar-story, progress-bar, posting story beneran dari shoper_status.
- 2026-10-29 19:27 :: 2 DEMO terpisah = strategi: sc-preview = workshop ngetes 1 bata; sc1/sc2 = 2 prototipe rasa biar Coi bisa BANDHINGIN & milih. Merge/ganti-halaman-utama = GATE owner, NOL AI putusin. Yang kalah dibuang, yang menang dikembangin.
- 2026-10-29 20:01 :: KEPUTUSAN Coi 19:37: sc1 MENANG. Transisi sosmed = NUMPANG (sisip rail story sc1 di atas duality, antara header & chips), BUKAN ganti/buang. Yin-yang = toko berbahasa sosmed, transisi di 1 layar. Veto 'tab' kalau mau duality->tab & sc1->utama.
- 2026-10-29 20:04 :: VETO Coi 20:01: injeksi OK (oh y). Ring story BIRU IG #0095F6, notif TETEP tangerin. sc1/sc2 NOL berubah (backward-compat via prop ring opsional).
- 2026-10-29 20:43 :: PENELITIAN PSIKOLOGI Coi 20:28: widget 2-baris SALAH di lensa otak (scarcity=kurang keliatan, 2-baris=kelar di tempat=bunuh nagih). Fix: 1 baris 12 slot kepotong=geser=nagih. Pembunuh keseruan asli=bukan baris, tapi label 'segera' dobel-dobel=noise. Foto: HP 3+1 kepotong (scarcity+foto gede), desktop 5-6 (subitizing<=5, 7=capek). Feed udah bener tanpa sadar, yang miring cuma widget.
- 2026-10-29 20:47 :: FOKUS Coi 20:43: scarcity = mesin utama UI shoper, bukan hiasan. Widget 1-baris-12-slot-kepotong + matiin 'segera' dobel + foto HP 3+1. Ronde depan patch dari byte, NOL nebak anchor.
- 2026-10-29 22:36 :: IDEA Coi 22:xx #1: candy gue gagal karena MONOKROM coral. Fix = multi-warna per ikon (level Shopee/Trip). 3D beneran (level Tiket) = NOL dari SVG, butuh aset Figma -> pakai JPG 3D lo dari ImageKilat (Jalur B).
- 2026-10-29 22:36 :: IDEA Coi 22:xx #2: ikon widget = KATEGORI AFFILIATE beneran (pesawat=tiket, hotel=nginap), BUKAN hiasan. Ini jawab 'serius vs rame': serius = tiap ikon wakili duit.
- 2026-10-29 22:36 :: IDEA Coi 22:xx #3: 'nonton' = SAH sebagai kategori affiliate langganan streaming (Vidio/WeTV/iflix, legal, komisi). Player BAJAKAN gratis-no-iklan = NOL dibangun (takedown = 60 jam mati). Dashboard bikin lo colok provider legal mana pun.
- 2026-10-29 22:36 :: IDEA Coi 22:xx #4: SUPER ADMIN DASHBOARD = wajah hukum port-colok lo (ganti provider dari UI, NOL redeploy). Lincah != legal, tapi lincah = web nggak mati pas 1 provider tumbang. GitHub manual = fallback, dashboard = UX.
- 2026-10-29 23:16 :: KEPUTUSAN: navbar pakai ikon repo sendiri (IHome/ICart/INotify/IAccount/IApplication) via import manual, BUKAN CIcon buta; ikon saja NOL label; animasi 2.5D rotateX+bounce sekali; GAME=IApplication sementara (gamepad belum ada di repo).
- 2026-10-30 08:28 :: ICartSoft.vue <- andrtsx:shopping-cart-out (outline imut, fill+stroke mix). ATURAN: 1 keluarga buat semua ikon navbar, HARAM campur filled+outline. Lo milih keluarga: andrtsx / ion-outline / ion-filled.
- 2026-10-30 08:36 :: IGridSoft.vue <- andrtsx:grid-random (duotone, serumah ICartSoft). Keluarga = andrtsx, HARAM campur ion-filled.
- 2026-10-30 08:43 :: IGamepadSoft.vue <- hugeicons:gamepad-01 (pure stroke 1.5, TANPA fill .2 duotone). CAMPUR SET disengaja Coi; toleran asal stroke sama, lo nilai di preview.
- 2026-10-30 13:07 :: STOK ikon (belum dirakit): ISearchBI <- bootstrap-icons:search · viewBox16 + fill solid + no-stroke = KELUARGA LAIN, HARAM campur navbar soft(stroke1.5/24). Kemungkinan niat: header search-bar (aman, berdiri sendiri) ATAU navbar (janggal, cari yang stroke 1.5/24). Lo nentuin pas rakit.
- 2026-10-30 14:09 :: KEPUTUSAN gas: navbar = Phosphor FILL (currentColor, 1 desainer, MIT, NOL credit). Jangkar SVG = API iconify via curl, BUKAN ingatan AI (NOL nebak koordinat). 5 nama resmi: house/shopping-cart/squares-four/bell/user -fill. Rasa = blok imut (lo lari ke filled, bukan garis IG).
- 2026-10-30 15:16 :: VISI TUAS Coi: ikon = 4 lapis. (1) GIT=jangkar, file lokal, NOL runtime-fetch. (2) CONFIG icons.json=tuas, ganti 1 baris=ganti tema, NOL nyentuh kode. (3) PREVIEW=peramu. (4) SERVER=bonus narik set baru SEKALI ke lapis1, NOL runtime. Paduan asumsi lo: server=mudah, git=aman, config=panggil-panggil. Lapis1-3 pakai harta repo (IHome/IShop/IApplication/INotify/IAccount + IStar/IHeart/IBasket/ITime), NOL sentuh server ronde ini.
- 2026-10-30 15:50 :: SINKRON 3 (web>aku>kau): web=jangkar folder lokal (50 file, kebukti ls), aku=pilih dari menu nomor, kau=waiter bacain+ragit. KEPUTUSAN: server iconify MATI buat endpoint ikon di Termux lo (collections hidup, /set/icon.json kosong) -> LUPAKAN 15-besar-iconify, menu=folder lokal. Tuas merah karena auto-import+glob bentrok -> buang glob, import eksplisit (pola CNav kebukti). Waiter: ls|cat -n = menu, lo teriak nomor, gue config+registry.
- 2026-10-30 16:45 :: ACC Coi: navbar-permen FINAL. Upgrade = 2-WARNA Flutter-ish via MASK (SVG file lo=jangkaran, gradient CSS=isi badan). BUKAN 3D (batas jujur). Config default palet = gue yang nulis (lo tinggal teken), ganti 1 baris hex = ganti rasa. Menu-visual 57 = RONDE LAIN (lo acc 9 dulu, 57=widget). Review menu teks = belum gampang, dicatat.
- 2026-10-30 16:58 :: COLOK duality: lo bener 145-152 kurang buat colok buta; solusinya BUKAN nagih lo, tapi tool ASSERT anchor (script setup / label button / style / id tabs) -> kalau kurang, tool teriak, NOL build merah diam. Palet dari icons.json AKTUAL (zamrud rumah 3331ad9 ikut). onTab NOL disentuh: class act + t.on udah template lo pake, gue cuma ganti isi button + inject biStyle. Atomic: 1 assert gagal = NOL nulis.

## NGELÓG — trace pencapaian (dibawah legodone, rule Coi korporat)
- 2026-10-30 17:11 :: GUNUNG 3 SEO/SSR mendarat. CF build #0a0d9bc7 commit b6b2ad1 Node22.23.4 = Success (716 file, .html ke-prerender = SEO kebukti). Timeline tembok yang diruntuhin 90 ronde: swiper(CJS) -> workbox-window(CJS) -> noExternal true(collateral @vue/server-renderer node:stream) -> list manual[swiper,workbox] -> pinia _s(useToast col-0 axios-instance.js, 85 ronde buta .js) -> axios localStorage+error.response(reading data) -> dashboard document($ is not defined, jQuery) -> supabase WebSocket(Node20->22). 3 luka tersisa: env VITE_BASE_DOMAIN kosong, $/jQuery SSR, API builder-block(errno-111 akibat env). vite-ssg 0.17 NOL fail-fast = hijau tapi setengah halaman kosong.

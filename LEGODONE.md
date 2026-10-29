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
- ☐ hero = rail story bulat (24 jam, wajah/preview) → feed post orang, produk numpang di dalam post
- ☐ navbar ikon-saja (Instagram): aktif filled, notif = titik merah
- ☐ dot posisi carousel · ☐ love/share = verb utama post

### DEMO 2 — COMMERCE SOCIAL MEDIA (/sc2) · panggung = barang, berbahasa tenang
- ☐ hero = katalog produk (baris duality) → tiap card dipakaikan furniture social
- ☐ seller story-circle di card · → ☐ ☑ backend story 24 jam SUDAH ADA (shoper_status.expires_at + RLS)
- ☐ navbar ikon+label (Duolicious) · → ☐ dot posisi + notif titik hidup di sini juga

### PRIMITIF SHARED (dipakai 2 demo, 1 sumber truth)
- ☐ StoryCircle.vue · bulat, wajah/preview, tap → story 24 jam (frontend BELUM dibangun)
- ☐ Dots.vue · indikator posisi carousel
- ☐ NotifDot.vue · titik merah, bukan teks
- ☑ backend story = shoper_status (expires_at now()+1day, RLS > now(), purge) · SUDAH jadi di DB

### ATURAN RAMU
- ☐ 2 demo NOL nyentuh duality.vue / list.vue yang udah hidup · file baru /sc1 /sc2
- ☐ yin-yang = KOMPOSISI primitif, bukan CSS baru · rasa tenang dijaga di 2 sisi
- ☐ gate Coi: acc split sc1/sc2 di atas → bilang "gas sc" → AI tulis 2 page + 3 primitif dari byte

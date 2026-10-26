# csttan.md — Peta Dinamis shoper (SUMBER KEBENARAN TUNGGAL)
> Aturan main: file ini OTORITAS. Kepala asisten labil (5x salah hipotesis), disk tidak.
> Kalau konflik, file ini yang menang. Coret [x] pas kelar, tambah baris pas nemu utang baru.
> Jangan andalkan ingatan obrolan — andalkan file ini.

## 0. STATUS — snapshot 2026-10-24 (~24 jam kerja, semua sudah dibuktikan pakai byte)
- [x] Hero: 12M -> webm 420K GERAK (swipe-hero.webm)
- [x] Brand teks: shoper di src (17 file) + locales (15 bahasa) + nama (Pasar Kilat/e-shopee -> shoper)
- [x] Merah Shopee #ee4d2d -> orange shoper #FF7A1A (10 file css/vue)
- [x] Logo: kado orange vektor (public/logo.svg + IBrand.vue sidebar) — placeholder berwajah lo, bukan paten final
- [x] Aset raster: PNG gajah 11M -> WebP 4.9M (resize 1024 + q80, ekstensi jujur)
- [x] Interaksi awal: CGiftCards (Kejutan Hari Ini, flip) + CGiftRow (Deretan Kejutan, 8 kartu aset lo)
- [x] Mockup "Shopee Mall" (section 137) -> HIDDEN reversible (v-if=false), file gambar ditinggal di disk
- [x] Ranjau template: vitest di AutoImport -> dicabut (optimizeDeps.exclude + globals), vite 3333 hidup bersih (ready 2724ms, ranjau 0, html 1)
- [i] VITE: hidup di :3333, vonis 3 angka hijau. README.md masih nyimpen screenshot e-shopee template = BUKAN bocor runtime, tapi bocor mental (bikin panik) -> rewrite README = P1

## 1. BACKLOG DINAMIS (P0=visual-butuh-alat / P1=interaksi+doc / P2=sistem / PARKIR)
### P0 — butuh alat yang belum ada di net 4G lo jam segini (JANGAN dipaksa malam ini)
- [ ] rembg: cabut kotak abu/putih di ~24 aset (avatar/badge/trophy/gift/bell/sparkle/sticker) -> WebP transparan. Butuh pip ~170MB + model ONNX. WiFi enak + mata seger.
- [ ] Translate dashboard Vietnam (Cho xac nhan / Don giam gia / ...) -> id/en. Ini KERJAAN NULIS, bukan tebas. Kamar i18n terpisah.
- [ ] Lottie 19-23 (flash-badge-pulse / cart-add-pop / success-check-draw / empty-cart-wave / coin-stack) = DESAIN di LottieFiles, mp4->lottie MUSTAHIL (fisika).
- [ ] Mascot / ikon signature kursi 24 = KONSEP lo belum nemu. Benih: kado orange + pita + siluet keranjang. Lo yang putusin, gue nggak paksa.
- [ ] Verifikasi KONTEN /img/brand/1..19: logo Shopee (bocor -> cabut) vs logo merchant affiliate (legit -> SIMPAN, konteks AccesTrade lo). File udah ada, isi belum dilihat.
### P1 — interaksi & doc (bisa malam ini/besok, zero-net)
- [ ] Implement spec DOM JS §2 (mulai .a persist gift) — SETELAH lo approve §2
- [ ] Rewrite README.md (buang screenshot e-shopee, ganti muka shoper) — nutup "bocor mental"
### P2 — sistem / jaring executable
- [ ] tools/health.sh — vonis web sehat tanpa perlu tanya asisten (lihat §3)
### PARKIR — hukum lo sendiri
- [ ] FRIDA (tombol CONVERT) — 1 rumah 1 gerbang, nunggu lo bilang gas + gue re-probe anchor LIVE

## 2. ARSITEKTUR DOM JS — CETAK BIRU (lo APPROVE dulu, baru gue cor. Ini jawaban "kehebatan sistem dipikir dari sekarang")
Prinsip: bukan nempelin onclick per tombol, tapi 1 KERANGKA yang bikin tombol ke-N gratis & nggak saling merusak.
- 2.1 STATE LAYER: src/composables/useShoperState.js — 1 store reactive + auto-persist localStorage (prefix "shoper:"). Semua fitur (gift opened, cart, claimed coupon, spin result) baca/tulis ke SINI. Nggak pakai Pinia (berat, belum perlu). Refresh != reset.
- 2.2 EVENT BUS: src/composables/bus.js — mini emit/on. Event: gift:open, coupon:claim, cart:add, spin:result. Header badge / toast / confetti LANGGANAN, bukan dipanggil langsung. Komponen terpisah tapi nyambung = SISTEM.
- 2.3 OPTIMISTIC + FALLBACK: aksi UI dulu (localStorage), sync backend kemudian (pas API ada). API mati -> localStorage = truth. Web nggak mati = anti-badai. CATATAN: proxy /api/v2 -> tp-o.tk UDAH ADA di vite.config lo, jadi 2.5.e bukan mimpi, infra-nya udah nempel.
- 2.4 REVERSIBLE FLAG: src/config/features.js = { giftPersist:true, cartBadge:true, couponClaim:true, spinWheel:false, checkoutApi:false }. Tiap fitur di belakang flag. Badai? Matiin 1 baris. Nggak perlu revert git.
- 2.5 ROADMAP TOMBOL (kecil -> besar, tiap step 1 commit reversible, lo bisa berhenti di mana aja):
  a. persist CGiftCards: ganti reactive -> useShoperState, hapus teks "reset kalau refresh". [KLEIN — next setelah approve]
  b. add-to-cart di CGiftRow/produk -> emit cart:add -> badge header naik. [SEDANG]
  c. claim coupon (kupon affiliate style AccesTrade) -> coupon:claim -> toast + localStorage. [SEDANG]
  d. spin wheel "Kejutan" -> spin:result -> confetti + reward ke state. [BESAR — butuh aset spinner/lottie]
  e. checkout connect /api/v2 (proxy udah ada). [BESAR — backend]

## 3. JARING ANTI-BADAI — aturan main (biar asisten nggak amatir lagi; lo bisa nagih pakai daftar ini)
- Reversible dulu, hapus belakangan: hide/disable > delete. File kerjaan JANGAN dibuang, dipindah/di-flag.
- Commit SPESIFIK (git add <file>), BUKAN git add -A. Pesan commit tanpa "!".
- Vite lifecycle: health-check -> SIGTERM (graceful) -> verify port KOSONG -> start -> verify log BARU (/tmp/dev2.log). JANGAN -9 buta (itu yang nyobek cache kemaren).
- Peta di DISK (file ini), bukan di kepala asisten. Asisten salah hipotesis 5x karena megang state volatile.
- BLUEPRINT (spec §2) sebelum COR (kode). Lo approve, asisten implement. Nggak ngecor dulu mikir belakangan.
- VONIS pakai BYTE (curl/grep/wc/log), bukan perasaan. JANGAN nyebut akar sebelum liat log mentah (kesalahan ronde clipboard-gigit & cache-sobek).
- 1 blok <= ~40 baris. Blok raksasa = sumber crash clipboard. PECAH. Risiko (heredoc) ditaruh di file yang BELUM dibaca runtime (doc), bukan file Vue.
- tools/health.sh (P2) = jaring executable: 1 perintah -> vonis vite hidup / ranjau mati / aset ada / git sinkron, tanpa perlu tanya asisten.

## 4. LANGKAH BERIKUTNYA (setelah lo baca file ini)
1. Lo baca §2. Approve apa adanya, ATAU koreksi (misal "skip spin wheel dulu", "cart beneran pakai API").
2. Ronde berikutnya asisten kerjain §2.5.a (persist gift — KLEIN, reversible, zero-net) + bikin tools/health.sh (§3 jaring executable). SATU-SATU, blok pendek.
3. P0 (rembg/translate/lottie/mascot) = besok, WiFi + mata seger. Jangan dipaksa malam ini.

## 5. BLUEPRINT ANIMASI — "ladang animasi, sistem anti-badai, render seringan bulu"
> Revisi urutan §4: ANIMASI POC jadi prioritas §2.5.a-prime (lo nagih JIWA dulu, persist gift nyusul). File ini dinamis — urutan bisa digeser, tapi aturan §3 nggak.

### 5.1 Prinsip "seringan bulu" (terukur, bukan janji)
- GPU-only: animasi CUMA pakai transform + opacity. HARAM animasi top/left/width/height/margin (trigger layout/reflow = jank = bukan bulu).
- 1 orchestrator: SATU requestAnimationFrame loop buat semua animasi. BUKAN 50 setInterval/setTimeout terpisah (itu resep battery-drain + tab freeze).
- IntersectionObserver: animasi jalan CUMA pas elemen keliatan. Off-screen = dorman (pause). Scroll panjang = tetap 60fps.
- prefers-reduced-motion: user yang set "kurangi gerakan" di OS = animasi MATI, konten tetep ada. Ini bukan opsional, ini aksesibilitas + احترام.
- will-change secukupnya: cuma di elemen yang beneran animasi, dilepas pas selesai (will-change permanen = boros VRAM = HP low-end nge-lag).
- Vektor dulu: ikon/simbol = SVG (scalable, ~1-3KB, tajam di semua DPI). Raster (webp) cuma buat foto produk. Lottie/Rive cuma buat yang kompleks & butuh timeline (nyusul, bukan sekarang).
- Cara UKUR bulu: DevTools > Performance > rekam scroll. Bar hijau = OK, bar merah = jank. ATAU uji mata: scroll di HP lo, kalau nggak patah-patah = lulus. "Bulu" = metrik, bukan kata.

### 5.2 Engine (kerangka, bukan tempelan onclick)
- src/composables/useAnim.js — 1 modul: daftar animasi terdaftar, 1 rAF loop, IntersectionObserver auto-pause, baca prefers-reduced-motion SEKALI di awal, expose register(el, keyframes)/unregister. Semua komponen animasi LEWAT ini, nggak ada yang bikin loop sendiri.
- src/config/features.js (dari §2.4) nambah flag animasi: { animGiftFlip:true, animSunMorning:true, animRainAfternoon:false, ... }. Badai? Matiin 1 baris, animasi off, konten on. Nggak perlu revert git.
- Aturan colok: komponen animasi ditulis sebagai file STANDALONE dulu, diverifikasi utuh (wc/tail), BARU dicolok ke index pas lo approve. Nggak pernah nulis langsung ke runtime.

### 5.3 Roadmap "tanam 1 pohon dulu" (jangan cor hutan buta)
1. POC-1: Matahari ⛅ pagi (diskon pagi) — SVG matahari + awan, translate3d + opacity, lewat useAnim, reduced-motion aware. 1 file, reversible, zero-net, zero-dep. LO LIAT TUMBUH dulu.
2. POC-2..4: siang ☀️ / sore 🌇 / malam 🌙 — variasiin dari POC-1 (same engine, beda keyframe & palet). Murah karena kerangkanya udah ada.
3. Baru setelah 4 musim jalan mulus: tombol melayang (fixed + translate3d + spring CSS), flash-sale countdown tik-tok, kado bounce pas di-claim.
4. Lottie/Rive cuma buat yang timeline-nya nggak bisa di-CSS (misal kado buka 3D). Itu besok/bulan depan, bukan sekarang.

### 5.4 Snippet bukti teknis (TEKS di doc, BUKAN file runtime — nol risiko)
// useAnim.js inti (ringkas): loop tunggal + IO pause + reduced-motion
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches
const reg = new Map(); let raf = 0
function tick(t){ for(const [el,fn] of reg) fn(t); raf = requestAnimationFrame(tick) }
function register(el, fn){ if(reduce) return; reg.set(el, fn); if(!raf) raf = requestAnimationFrame(tick)
  const io = new IntersectionObserver(([e])=>{ e.isIntersecting ? reg.set(el,fn) : reg.delete(el) }); io.observe(el) }
// CSS matahari (GPU-only): transform+opacity doang
// .sun{ will-change:transform,opacity; animation: peek 6s ease-in-out infinite }
// @keyframes peek{ 0%,100%{transform:translate3d(0,8px,0);opacity:.6} 50%{transform:translate3d(0,-6px,0);opacity:1} }
// @media (prefers-reduced-motion:reduce){ .sun{animation:none;opacity:1} }

## 6. RITUAL SINKRON — 1 PETA, 2 RUMAH (jawaban "g kau gabungkan")
> csttan.md = SUMBER KEBENARAN TUNGGAL. Hidup di GIT. Termux & codespace BACA FILE SAMA via pull. JANGAN bikin 2 salinan (resep divergensi 26 jam).
- Aturan pindah rumah: SEBELUM kerja di rumah mana pun -> `git pull origin main` dulu. Setelah -> kerja -> commit spesifik -> push. Rumah nggak pernah "ketinggalan peta".
- $health = vonis kondisi rumah SEKARANG (vite hidup? git sinkron? uncommitted berapa?). Lo nggak perlu nanya asisten "web sehat ga" -> ketik `health`, disk yang jawab.
- Kondisi Terkini (snapshot ronde ini): fix ranjau vitest = KE-GIT (77f660a) -> cold-start nggak bisa bikin hitam lagi. health.sh + sun-poc + peta = KE-GIT (8b051fd). vite sesi codespace ini MATI karena restart (NORMAL, tinggal start, bukan benerin).
- Dosa yang dipetain: asisten 5x salah hipotesis karena megang peta di CHAT (volatile). Ronde ini pindah ke DISK (persistent). Mulai sekarang: update §0/§6 DI FILE ini sebelum ngapa-ngapain, bukan di kepala.


----- ✅ SELESAI (csttan.md) -----
  ✅ GUNUNG 1: skema AffiliateOffer TS (19 field, doc ACCESSTRADE telanjang) - 27c093f
  ✅ GUNUNG 2 part1: fixture promos.json + kartu Agoda + tombol KLAIM noopener - 74bdc11
  ✅ GUNUNG 1.5 b1+b4: adapter tpoNormalize (norm-envelope-before-dot, unknown->product) + fixture 3 shape + runner - cc8e3f5
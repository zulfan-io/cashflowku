<template>
  <section class="gift-cards p-5" aria-labelledby="gift-cards-title">
    <div class="gc-head text-center mb-5">
      <h2 id="gift-cards-title" class="text-3xl font-semibold">Kejutan Hari Ini</h2>
      <p class="text-lg opacity-80">
        Buka satu kartu, lihat kejutanmu. Demo UI, belum terhubung ke backend.
      </p>
    </div>

    <div class="gc-grid">
      <button
        v-for="card in cards"
        :key="card.id"
        class="gc-card"
        :class="{ opened: card.opened }"
        @click="openCard(card)"
        :aria-pressed="card.opened"
        :aria-label="card.opened ? card.reward : 'Kartu kejutan tertutup'"
      >
        <span class="gc-inner">
          <span class="gc-face gc-front">
            <img :src="card.image" :alt="card.label" class="gc-img" />
            <span class="gc-tag">{{ card.label }}</span>
          </span>

          <span class="gc-face gc-back">
            <span class="gc-reward">{{ card.reward }}</span>
            <span class="gc-note">{{ card.note }}</span>
          </span>
        </span>
      </button>
    </div>

    <p class="gc-foot text-center mt-4">
      Kartu reset kalau halaman di-refresh. Nanti bisa diikat ke akun/user.
    </p>
  </section>
</template>

<script setup>
import { reactive } from 'vue'

const cards = reactive([
  {
    id: 'gift',
    label: 'Kado',
    image: '/img/gen/gift-box-open.webp',
    reward: 'Diskon 10%',
    note: 'Demo — belum klaim',
    opened: false
  },
  {
    id: 'flash',
    label: 'Flash',
    image: '/img/gen/sticker-discount.webp',
    reward: 'Gratis Ongkir',
    note: 'Demo — belum klaim',
    opened: false
  },
  {
    id: 'trophy',
    label: 'Trofi',
    image: '/img/gen/trophy.webp',
    reward: 'Koin Kejutan',
    note: 'Demo — belum klaim',
    opened: false
  }
])

function openCard(card) {
  if (!card.opened) card.opened = true
}
</script>

<style scoped>
.gift-cards {
  max-width: 1100px;
  margin: 0 auto;
}

.gc-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
}

.gc-card {
  appearance: none;
  border: 0;
  background: transparent;
  padding: 0;
  cursor: pointer;
  perspective: 1000px;
}

.gc-inner {
  display: block;
  position: relative;
  width: 100%;
  aspect-ratio: 3 / 4;
  transform-style: preserve-3d;
  transition: transform 0.55s cubic-bezier(0.2, 0.7, 0.2, 1);
}

.gc-card.opened .gc-inner {
  transform: rotateY(180deg);
}

.gc-face {
  position: absolute;
  inset: 0;
  backface-visibility: hidden;
  border-radius: 1rem;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
}

.gc-front {
  background: linear-gradient(160deg, #FF7A1A, #ffb066);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  padding: 1rem;
}

.gc-img {
  width: 72%;
  height: 62%;
  object-fit: contain;
  filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.22));
}

.gc-tag {
  font-weight: 700;
  color: #FFF7EC;
  letter-spacing: 0.02em;
}

.gc-back {
  transform: rotateY(180deg);
  background: #111827;
  color: #FFF7EC;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 1rem;
  border: 2px solid #FF7A1A;
}

.gc-reward {
  font-size: 1.5rem;
  font-weight: 800;
  color: #FF7A1A;
  text-align: center;
}

.gc-note {
  font-size: 0.9rem;
  opacity: 0.75;
  text-align: center;
}

.gc-foot {
  opacity: 0.65;
  font-size: 0.9rem;
}

@media (prefers-reduced-motion: reduce) {
  .gc-inner {
    transition: none;
  }
}
</style>

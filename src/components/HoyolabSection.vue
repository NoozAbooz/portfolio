<template>
  <div class="hoyolab-section">
    <div v-if="loading" class="d-flex align-center ga-3 py-8">
      <v-progress-circular indeterminate color="primary" />
      <p class="text-body-1 text-medium-emphasis mb-0">Loading Hoyolab data...</p>
    </div>

    <v-alert
      v-else-if="error"
      type="error"
      variant="tonal"
      title="Could not load Hoyolab data"
      :text="error"
      class="mb-4"
    />

    <v-alert
      v-else-if="gameCards.length === 0"
      type="info"
      variant="tonal"
      title="No Hoyolab game data found"
      text="The endpoint returned no supported game entries."
      class="mb-4"
    />

    <v-row v-else dense>
      <v-col
        v-for="card in gameCards"
        :key="card.key"
        cols="12"
        md="6"
      >
        <HoyolabPlayerCard
          :game-data="card.data"
          :game-key="card.key"
          :game-title="card.title"
        />
      </v-col>
    </v-row>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'

import HoyolabPlayerCard from './HoyolabPlayerCard.vue'

interface GameData {
  player: {
    info: {
      name: string
      uid: string
      level: number
      images: {
        icon: string
        background: string
      }
    }
    stats: {
      activeDays: number
      avatarNum: number
      achievementNum: number | null
      chestNum: number | null
      abyssProcess: string | null
    }
  }
  realtime: {
    stamina: {
      amount: string
      recover: number
      reserve?: {
        amount: string
        full: boolean
      }
    }
    expedition: string
    daily: {
      task: string
      extraReward?: boolean
    }
    weeklyBoss: string
  }
}

interface HoyolabResponse {
  ts: number
  hkrpg?: GameData
  nap?: GameData
  gi?: GameData
}

const loading = ref(true)
const error = ref<string | null>(null)
const payload = ref<HoyolabResponse | null>(null)

const gameCards = computed(() => {
  const output: Array<{ key: 'hkrpg' | 'nap' | 'gi'; title: string; data: GameData }> = []
  if (payload.value?.hkrpg) {
    output.push({
      key: 'hkrpg',
      title: 'Honkai: Star Rail',
      data: payload.value.hkrpg,
    })
  }

  if (payload.value?.nap) {
    output.push({
      key: 'nap',
      title: 'Zenless Zone Zero',
      data: payload.value.nap,
    })
  }

  if (payload.value?.gi) {
    output.push({
      key: 'gi',
      title: 'Genshin Impact',
      data: payload.value.gi,
    })
  }

  return output
})

async function loadHoyolabData() {
  loading.value = true
  error.value = null

  try {
    const response = await fetch('/api/hoyolab', { method: 'GET' })
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`)
    }

    payload.value = (await response.json()) as HoyolabResponse
  } catch {
    error.value = 'Check API route setup.'
  } finally {
    loading.value = false
  }
}

onMounted(async () => {
  await loadHoyolabData()
})
</script>

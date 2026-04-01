<template>
  <v-card color="surface-container-high" class="hoyo-card">
    <div class="hoyo-banner" :style="bannerStyle">
      <div class="hoyo-banner-overlay d-flex align-center ga-4 pa-4">
        <v-avatar size="56" rounded="lg" class="hoyo-avatar">
          <v-img :src="gameData.player.info.images.icon" :alt="`${gameTitle} avatar`" cover />
        </v-avatar>

        <div>
          <div class="d-flex align-center ga-2 flex-wrap mb-1">
            <h2 class="text-h5 font-weight-bold mb-0 text-high-emphasis title-wrap">
              {{ gameData.player.info.name }}
            </h2>
            <v-chip size="small" color="primary" variant="flat" class="font-weight-medium">
              Lv. {{ gameData.player.info.level }}
            </v-chip>
          </div>
          <div class="d-flex align-center ga-1">
            <p class="text-body-2 text-medium-emphasis mb-0">
              UID: {{ gameData.player.info.uid }}
            </p>
            <v-tooltip :text="copiedUid ? 'Copied' : 'Copy UID'" location="top">
              <template #activator="{ props: tooltipProps }">
                <v-btn
                  v-bind="tooltipProps"
                  icon="mdi-content-copy"
                  variant="text"
                  size="x-small"
                  density="comfortable"
                  class="uid-copy-btn"
                  :aria-label="copiedUid ? 'UID copied' : 'Copy UID'"
                  @click="copyUid"
                />
              </template>
            </v-tooltip>
          </div>
        </div>
      </div>
    </div>

    <v-card-text class="pa-4 pa-md-5">
      <h3 class="text-h6 text-high-emphasis mb-3">Overview</h3>
      <div class="stats-grid mb-5">
        <div v-for="stat in overviewStats" :key="stat.label" class="stat-cell">
          <p class="text-h5 font-weight-bold text-high-emphasis mb-0">{{ stat.value }}</p>
          <p class="text-body-2 text-medium-emphasis mb-0">{{ stat.label }}</p>
        </div>
      </div>

      <h3 class="text-h6 text-high-emphasis mb-3">Real-Time notes</h3>
      <div class="stats-grid">
        <div v-for="stat in realtimeStats" :key="stat.label" class="stat-cell">
          <p class="text-h5 font-weight-bold text-high-emphasis mb-0">{{ stat.value }}</p>
          <p class="text-body-2 text-medium-emphasis mb-0">{{ stat.label }}</p>
        </div>
      </div>
    </v-card-text>
  </v-card>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'

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

const props = defineProps<{
  gameData: GameData
  gameKey: 'hkrpg' | 'nap' | 'gi'
  gameTitle: string
}>()

const copiedUid = ref(false)

async function copyUid() {
  try {
    await navigator.clipboard.writeText(props.gameData.player.info.uid)
    copiedUid.value = true
    setTimeout(() => {
      copiedUid.value = false
    }, 1400)
  } catch {
    copiedUid.value = false
  }
}

const bannerStyle = computed(() => {
  const background = props.gameData.player.info.images.background
  if (!background) {
    return {
      background:
        'linear-gradient(105deg, rgba(var(--v-theme-primary), 0.38), rgba(var(--v-theme-surface-container-highest), 0.8))',
    }
  }

  return {
    backgroundImage: `linear-gradient(180deg, rgba(0,0,0,0.22) 0%, rgba(0,0,0,0.74) 100%), url(${background})`,
  }
})

const overviewStats = computed(() => {
  const stats = props.gameData.player.stats

  const characterLabel =
    props.gameKey === 'hkrpg'
      ? 'Characters'
      : props.gameKey === 'nap'
        ? 'Agents'
        : 'Characters'

  const abyssLabel =
    props.gameKey === 'hkrpg'
      ? 'MoC'
      : props.gameKey === 'nap'
        ? 'Proxy'
        : 'Abyss'

  return [
    {
      label: 'Active days',
      value: stats.activeDays,
    },
    {
      label: characterLabel,
      value: stats.avatarNum,
    },
    {
      label: abyssLabel,
      value: stats.abyssProcess ?? '--',
    },
    {
      label: 'Chests',
      value: stats.chestNum ?? '--',
    },
    {
      label: 'Achievements',
      value: stats.achievementNum ?? '--',
    },
  ]
})

const realtimeStats = computed(() => {
  const realtime = props.gameData.realtime

  const staminaLabel =
    props.gameKey === 'hkrpg'
      ? 'Power'
      : props.gameKey === 'nap'
        ? 'Battery'
        : 'Resin'

  const dailyLabel =
    props.gameKey === 'hkrpg'
      ? 'Training'
      : props.gameKey === 'nap'
        ? 'Daily task'
        : 'Commission'

  return [
    {
      label: staminaLabel,
      value: realtime.stamina.amount,
    },
    {
      label: 'Expeditions',
      value: realtime.expedition,
    },
    {
      label: dailyLabel,
      value: realtime.daily.task,
    },
    {
      label: 'Weekly Boss',
      value: realtime.weeklyBoss,
    },
  ]
})
</script>

<style scoped>
.hoyo-card {
  border: 1px solid rgba(var(--v-theme-outline-variant), 0.45);
}

.hoyo-banner {
  position: relative;
  isolation: isolate;
  background-size: cover;
  background-position: center 28%;
  overflow: hidden;
}

.hoyo-banner::after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 24px;
  pointer-events: none;
  z-index: 0;
  background: linear-gradient(
    180deg,
    rgba(var(--v-theme-surface-container-high), 0) 0%,
    rgba(var(--v-theme-surface-container-high), 0.58) 100%
  );
}

.hoyo-banner-overlay {
  position: relative;
  z-index: 1;
  min-height: 110px;
}

.hoyo-avatar {
  border: 1px solid rgba(var(--v-theme-outline-variant), 0.65);
}

.uid-copy-btn {
  opacity: 0.85;
}

.uid-copy-btn:hover {
  opacity: 1;
  background: rgba(var(--v-theme-on-surface), 0.08);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  border: 1px solid rgba(var(--v-theme-outline-variant), 0.5);
  border-radius: 8px;
  overflow: hidden;
}

.stat-cell {
  padding: 12px 10px;
  text-align: center;
  background: rgb(var(--v-theme-surface-container));
  border-right: 1px solid rgba(var(--v-theme-outline-variant), 0.45);
}

.stat-cell:last-child {
  border-right: 0;
}

.title-wrap {
  word-wrap: break-word;
  overflow-wrap: break-word;
}

@media (max-width: 960px) {
  .stats-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .stat-cell {
    border-bottom: 1px solid rgba(var(--v-theme-outline-variant), 0.45);
  }

  .stat-cell:nth-child(2n) {
    border-right: 0;
  }
}
</style>
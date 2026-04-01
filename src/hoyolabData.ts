export interface GameData {
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

export interface HoyolabResponse {
  ts: number
  hkrpg?: GameData
  nap?: GameData
  gi?: GameData
}

const CACHE_TTL_MS = 5 * 60 * 1000

let cachedPayload: HoyolabResponse | null = null
let cachedAt = 0
let inFlightRequest: Promise<HoyolabResponse> | null = null

function hasFreshCache(): boolean {
  return !!cachedPayload && Date.now() - cachedAt < CACHE_TTL_MS
}

async function fetchHoyolabData(): Promise<HoyolabResponse> {
  const response = await fetch('/api/hoyolab', { method: 'GET' })
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`)
  }

  const payload = (await response.json()) as HoyolabResponse
  cachedPayload = payload
  cachedAt = Date.now()
  return payload
}

export async function getHoyolabData(forceRefresh = false): Promise<HoyolabResponse> {
  if (!forceRefresh && hasFreshCache()) {
    return cachedPayload as HoyolabResponse
  }

  if (inFlightRequest) {
    return inFlightRequest
  }

  inFlightRequest = fetchHoyolabData()

  try {
    return await inFlightRequest
  } finally {
    inFlightRequest = null
  }
}

export function preloadHoyolabData() {
  return getHoyolabData().catch(() => null)
}

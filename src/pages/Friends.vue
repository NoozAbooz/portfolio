<template>
  <v-container class="bg-surface">
    <div class="py-8">
      <v-btn to="/" variant="text" prepend-icon="mdi-arrow-left" class="mb-4">
        Back to Home
      </v-btn>

      <h1 class="text-h2 text-md-h1 font-weight-bold mb-3 title-wrap">
        <span class="climate-font">Friends</span>
      </h1>
      <p class="text-h6 text-medium-emphasis mb-6">
        Cool people I know and their GitHub stats
      </p>

      <v-row dense>
        <v-col
          v-for="(friend, index) in friendsConfig"
          :key="friend.username"
          cols="12"
        >
          <v-card color="surface-container-high">
            <v-card-text class="pa-6">
              <v-row align="center">
                <v-col cols="12" md="auto" class="text-center">
                  <v-avatar size="96" rounded="lg">
                    <v-img
                      :src="friendStates[index].data?.avatar_url || friend.avatarOverride"
                      :alt="friend.displayName"
                    />
                  </v-avatar>
                </v-col>

                <v-col cols="12" md="">
                  <div class="mb-2">
                    <h2 class="text-h4 font-weight-bold title-wrap">
                      {{ friend.displayName }}
                    </h2>
                    <p class="text-body-2 text-medium-emphasis mb-0">
                      @{{ friend.username }}
                    </p>
                  </div>

                  <p
                    v-if="friendStates[index].data?.bio"
                    class="text-body-1 text-medium-emphasis mb-3"
                  >
                    {{ friendStates[index].data?.bio }}
                  </p>
                  <p
                    v-else-if="friend.note"
                    class="text-body-1 text-medium-emphasis mb-3"
                  >
                    {{ friend.note }}
                  </p>

                  <div v-if="friendStates[index].loading" class="text-body-2">
                    Loading GitHub data…
                  </div>
                  <div
                    v-else-if="friendStates[index].error"
                    class="text-body-2 text-error"
                  >
                    {{ friendStates[index].error }}
                  </div>
                  <div
                    v-else-if="friendStates[index].data"
                    class="d-flex flex-wrap ga-4 mb-3"
                  >
                    <div class="text-body-2">
                      <span class="text-high-emphasis font-weight-medium">
                        {{ friendStates[index].data?.followers }}
                      </span>
                      <span class="text-medium-emphasis"> followers</span>
                    </div>
                    <div class="text-body-2">
                      <span class="text-high-emphasis font-weight-medium">
                        {{ friendStates[index].data?.following }}
                      </span>
                      <span class="text-medium-emphasis"> following</span>
                    </div>
                    <div class="text-body-2">
                      <span class="text-high-emphasis font-weight-medium">
                        {{ friendStates[index].data?.public_repos }}
                      </span>
                      <span class="text-medium-emphasis"> public repos</span>
                    </div>
                    <div
                      v-if="friendStates[index].data?.location"
                      class="text-body-2"
                    >
                      <v-icon
                        size="small"
                        class="me-1"
                        icon="mdi-map-marker"
                      />
                      <span class="text-medium-emphasis">
                        {{ friendStates[index].data?.location }}
                      </span>
                    </div>
                  </div>

                  <div class="d-flex ga-3 flex-wrap mt-2">
                    <v-btn
                      :href="
                        friendStates[index].data?.html_url ||
                        `https://github.com/${friend.username}`
                      "
                      target="_blank"
                      variant="flat"
                      color="secondary-container"
                      prepend-icon="mdi-github"
                    >
                      GitHub Profile
                    </v-btn>
                  </div>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

interface FriendConfig {
  username: string
  displayName: string
  avatarOverride?: string
  note?: string
}

interface GithubUser {
  login: string
  name: string | null
  avatar_url: string
  html_url: string
  bio: string | null
  followers: number
  following: number
  public_repos: number
  public_gists: number
  location: string | null
}

interface FriendState {
  loading: boolean
  error: string | null
  data: GithubUser | null
}

const friendsConfig: FriendConfig[] = [
  {
    username: 'Sir-Encoded',
    displayName: 'Sir-Encoded',
    note: 'Cool person I know who builds awesome stuff',
  },
  {
    username: 'Botspot',
    displayName: 'Botspot',
    avatarOverride: 'https://github.com/Botspot.png',
  }
]

const friendStates = ref<FriendState[]>(
  friendsConfig.map(() => ({
    loading: true,
    error: null,
    data: null
  }))
)

onMounted(async () => {
  await Promise.all(
    friendsConfig.map(async (friend, index) => {
      try {
        const response = await fetch(`https://api.github.com/users/${friend.username}`)
        if (!response.ok) {
          throw new Error('Failed to load GitHub profile')
        }
        const data: GithubUser = await response.json()
        friendStates.value[index] = {
          loading: false,
          error: null,
          data
        }
      } catch (error) {
        friendStates.value[index] = {
          loading: false,
          error: 'Could not load GitHub data.',
          data: null
        }
      }
    })
  )
})
</script>

<style scoped>
.title-wrap {
  word-wrap: break-word;
  overflow-wrap: break-word;
  hyphens: auto;
  max-width: 100%;
}
</style>


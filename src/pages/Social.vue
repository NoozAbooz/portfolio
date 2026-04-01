<template>
  <v-container class="bg-surface">
    <div class="py-8">
      <v-btn to="/" variant="text" prepend-icon="mdi-arrow-left" class="mb-4">
        Back to Home
      </v-btn>

      <h1 class="md:text-h1 sm:text-h2 text-md-h1 font-weight-bold mb-3 title-wrap">
        <span class="climate-font">Social</span>
      </h1>
      <p class="text-h6 text-medium-emphasis mb-6">
        Friends and social media profiles.
      </p>

      <v-tabs
        v-model="activeTab"
        bg-color="surface-container"
        color="primary"
        class="mb-6"
      >
        <v-tab value="github" prepend-icon="mdi-github">GitHub</v-tab>
        <v-tab value="hoyolab" prepend-icon="mdi-account-group">HoYoLAB</v-tab>
      </v-tabs>

      <v-window v-model="activeTab">
        <v-window-item value="github">
          <v-row dense>
            <v-col
              v-for="(social, index) in socialConfig"
              :key="social.username"
              cols="12"
            >
              <v-card color="surface-container-high">
                <v-card-text class="pa-6">
                  <v-row align="center">
                    <v-col cols="12" md="auto" class="text-center">
                      <v-avatar size="96" rounded="lg">
                        <v-img
                          :src="socialStates[index].data?.avatar_url || social.avatarOverride"
                          :alt="social.displayName"
                        />
                      </v-avatar>
                    </v-col>

                    <v-col cols="12" md="">
                      <div class="mb-2">
                        <h2 class="text-h4 font-weight-bold title-wrap">
                          {{ social.displayName }}
                        </h2>
                        <p class="text-body-2 text-medium-emphasis mb-0">
                          @{{ social.username }}
                        </p>
                      </div>

                      <p
                        v-if="socialStates[index].data?.bio"
                        class="text-body-1 text-medium-emphasis mb-3"
                      >
                        {{ socialStates[index].data?.bio }}
                      </p>
                      <p
                        v-else-if="social.note"
                        class="text-body-1 text-medium-emphasis mb-3"
                      >
                        {{ social.note }}
                      </p>

                      <div v-if="socialStates[index].loading" class="text-body-2">
                        Loading GitHub data...
                      </div>
                      <div
                        v-else-if="socialStates[index].error"
                        class="text-body-2 text-error"
                      >
                        {{ socialStates[index].error }}
                      </div>
                      <div
                        v-else-if="socialStates[index].data"
                        class="d-flex flex-wrap ga-4 mb-3"
                      >
                        <div class="text-body-2">
                          <span class="text-high-emphasis font-weight-medium">
                            {{ socialStates[index].data?.followers }}
                          </span>
                          <span class="text-medium-emphasis"> followers</span>
                        </div>
                        <div class="text-body-2">
                          <span class="text-high-emphasis font-weight-medium">
                            {{ socialStates[index].data?.following }}
                          </span>
                          <span class="text-medium-emphasis"> following</span>
                        </div>
                        <div class="text-body-2">
                          <span class="text-high-emphasis font-weight-medium">
                            {{ socialStates[index].data?.public_repos }}
                          </span>
                          <span class="text-medium-emphasis"> public repos</span>
                        </div>
                        <div
                          v-if="socialStates[index].data?.location"
                          class="text-body-2"
                        >
                          <v-icon
                            size="small"
                            class="me-1"
                            icon="mdi-map-marker"
                          />
                          <span class="text-medium-emphasis">
                            {{ socialStates[index].data?.location }}
                          </span>
                        </div>
                      </div>

                      <div class="d-flex ga-3 flex-wrap mt-2">
                        <v-btn
                          :href="
                            socialStates[index].data?.html_url ||
                            `https://github.com/${social.username}`
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
        </v-window-item>

        <v-window-item value="hoyolab">
          <HoyolabSection />
        </v-window-item>
      </v-window>
    </div>
  </v-container>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

import HoyolabSection from '../components/social/hoyolab/HoyolabSection.vue'

interface SocialConfig {
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

interface SocialState {
  loading: boolean
  error: string | null
  data: GithubUser | null
}

const socialConfig: SocialConfig[] = [
  {
    username: 'Botspot',
    displayName: 'Botspot',
    avatarOverride: 'https://github.com/Botspot.png',
  },
  {
    username: 'Sir-Encoded',
    displayName: 'Sir-Encoded',
    note: 'kawaii frog',
  },
]

const socialStates = ref<SocialState[]>(
  socialConfig.map(() => ({
    loading: true,
    error: null,
    data: null
  }))
)

const activeTab = ref<'github' | 'hoyolab'>('github')

onMounted(async () => {
  await Promise.all(
    socialConfig.map(async (social, index) => {
      try {
        const response = await fetch(`https://api.github.com/users/${social.username}`)
        if (!response.ok) {
          throw new Error('Failed to load GitHub profile')
        }
        const data: GithubUser = await response.json()
        socialStates.value[index] = {
          loading: false,
          error: null,
          data
        }
      } catch (error) {
        socialStates.value[index] = {
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


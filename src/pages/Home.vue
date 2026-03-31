<template>
  <v-container fluid class="fill-height bg-surface home-page-container">
    <v-row justify="center" align="center">
      <v-col cols="auto" style="max-width: 100%">
        <v-card color="surface-container-high" class="mx-auto">
          <v-card-text class="pa-8 pa-md-12">
            <v-row align="center">
              <v-col cols="12" md="auto" class="text-center">
                <v-avatar size="160" rounded="lg">
                  <v-img src="pfp.webp" alt="profile picture" />
                </v-avatar>
              </v-col>

              <v-col cols="12" md="">
                <div :class="$vuetify.display.mdAndUp ? '' : 'text-center'">
                  <h1 class="text-h2 text-md-h1 font-weight-bold mb-3">
                    Hey, I'm <span class="climate-font">Nooz</span>
                  </h1>

                  <p class="text-h6 text-medium-emphasis mb-4">
                    I make circuit boards and contribute to FOSS software.
                  </p>

                  <div class="mb-6">
                    <h2 class="text-high-emphasis mb-3">Skills</h2>
                    <div class="d-flex flex-wrap ga-2" :class="$vuetify.display.mdAndUp ? '' : 'justify-center'">
                      <v-chip class="lang-chip" color="primary" variant="elevated">C++</v-chip>
                      <v-chip class="lang-chip" color="primary" variant="elevated">KiCAD</v-chip>
                      <v-chip class="lang-chip" color="secondary" variant="elevated">Fusion360</v-chip>
                      <v-chip class="lang-chip" color="tertiary" variant="elevated">Python</v-chip>
                      <v-chip class="lang-chip" color="tertiary" variant="elevated">Inventor</v-chip>
                    </div>
                  </div>

                  <div class="d-flex ga-3 flex-wrap" :class="$vuetify.display.mdAndUp ? '' : 'justify-center'">
                    <v-btn href="https://github.com/NoozAbooz" target="_blank" variant="flat" prepend-icon="mdi-github"
                      color="secondary-container">
                      GitHub
                    </v-btn>
                    <v-btn to="/social" variant="flat" prepend-icon="mdi-account-multiple"
                      color="secondary-container">
                      Social
                    </v-btn>

                    <v-menu transition="fast-scale-transition" location="bottom end" :close-delay="50" :open-delay="0">
                      <template v-slot:activator="{ props }">
                        <v-btn v-bind="props" variant="flat" color="secondary-container" class="menu-btn">
                          <v-icon>mdi-dots-horizontal</v-icon>
                        </v-btn>
                      </template>
                      <div class="custom-menu">
                        <v-btn href="https://discord.com/users/606191901871439903" target="_blank" variant="flat"
                          class="menu-item-btn">
                          <span class="btn-icon" aria-hidden="true">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 126.644 96" width="18" height="18"
                              fill="currentColor" focusable="false" aria-hidden="true">
                              <path
                                d="M81.15,0c-1.2376,2.1973-2.3489,4.4704-3.3591,6.794-9.5975-1.4396-19.3718-1.4396-28.9945,0-.985-2.3236-2.1216-4.5967-3.3591-6.794-9.0166,1.5407-17.8059,4.2431-26.1405,8.0568C2.779,32.5304-1.6914,56.3725.5312,79.8863c9.6732,7.1476,20.5083,12.603,32.0505,16.0884,2.6014-3.4854,4.8998-7.1981,6.8698-11.0623-3.738-1.3891-7.3497-3.1318-10.8098-5.1523.9092-.6567,1.7932-1.3386,2.6519-1.9953,20.281,9.547,43.7696,9.547,64.0758,0,.8587.7072,1.7427,1.3891,2.6519,1.9953-3.4601,2.0457-7.0718,3.7632-10.835,5.1776,1.97,3.8642,4.2683,7.5769,6.8698,11.0623,11.5419-3.4854,22.3769-8.9156,32.0509-16.0631,2.626-27.2771-4.496-50.9172-18.817-71.8548C98.9811,4.2684,90.1918,1.5659,81.1752.0505l-.0252-.0505ZM42.2802,65.4144c-6.2383,0-11.4159-5.6575-11.4159-12.6535s4.9755-12.6788,11.3907-12.6788,11.5169,5.708,11.4159,12.6788c-.101,6.9708-5.026,12.6535-11.3907,12.6535ZM84.3576,65.4144c-6.2637,0-11.3907-5.6575-11.3907-12.6535s4.9755-12.6788,11.3907-12.6788,11.4917,5.708,11.3906,12.6788c-.101,6.9708-5.026,12.6535-11.3906,12.6535Z" />
                             </svg>
                          </span>
                          Discord
                        </v-btn>

                        <v-btn href="https://www.youtube.com/@NoozAbooz" target="_blank" variant="flat"
                          class="menu-item-btn">
                          <span class="btn-icon" aria-hidden="true">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18"
                              fill="currentColor" focusable="false" aria-hidden="true">
                              <path
                                d="M10,15L15.19,12L10,9V15M21.56,7.17C21.69,7.64 21.78,8.27 21.84,9.07C21.91,9.87 21.94,10.56 21.94,11.16L22,12C22,14.19 21.84,15.8 21.56,16.83C21.31,17.73 20.73,18.31 19.83,18.56C19.36,18.69 18.5,18.78 17.18,18.84C15.88,18.91 14.69,18.94 13.59,18.94L12,19C7.81,19 5.2,18.84 4.17,18.56C3.27,18.31 2.69,17.73 2.44,16.83C2.31,16.36 2.22,15.73 2.16,14.93C2.09,14.13 2.06,13.44 2.06,12.84L2,12C2,9.81 2.16,8.2 2.44,7.17C2.69,6.27 3.27,5.69 4.17,5.44C4.64,5.31 5.5,5.22 6.82,5.16C8.12,5.09 9.31,5.06 10.41,5.06L12,5C16.19,5 18.8,5.16 19.83,5.44C20.73,5.69 21.31,6.27 21.56,7.17Z" />
                            </svg>
                          </span>
                          Youtube
                        </v-btn>

                        <v-btn href="https://www.youtube.com/@210.kawaii" target="_blank" variant="flat"
                          class="menu-item-btn">
                          <span class="btn-icon" aria-hidden="true">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18"
                              fill="currentColor" focusable="false" aria-hidden="true">
                              <path
                                d="M10,15L15.19,12L10,9V15M21.56,7.17C21.69,7.64 21.78,8.27 21.84,9.07C21.91,9.87 21.94,10.56 21.94,11.16L22,12C22,14.19 21.84,15.8 21.56,16.83C21.31,17.73 20.73,18.31 19.83,18.56C19.36,18.69 18.5,18.78 17.18,18.84C15.88,18.91 14.69,18.94 13.59,18.94L12,19C7.81,19 5.2,18.84 4.17,18.56C3.27,18.31 2.69,17.73 2.44,16.83C2.31,16.36 2.22,15.73 2.16,14.93C2.09,14.13 2.06,13.44 2.06,12.84L2,12C2,9.81 2.16,8.2 2.44,7.17C2.69,6.27 3.27,5.69 4.17,5.44C4.64,5.31 5.5,5.22 6.82,5.16C8.12,5.09 9.31,5.06 10.41,5.06L12,5C16.19,5 18.8,5.16 19.83,5.44C20.73,5.69 21.31,6.27 21.56,7.17Z" />
                            </svg>
                          </span>
                          Youtube (VRC)
                        </v-btn>

                      </div>
                    </v-menu>

                    <v-btn to="/projects" variant="flat" color="primary" prepend-icon="mdi-folder-multiple">
                      Projects
                    </v-btn>
                    <v-btn href="https://blog.nooz.dev" target="_blank" variant="flat" color="primary" prepend-icon="mdi-post-outline">
                      Blog
                    </v-btn>
                  </div>
                </div>
              </v-col>
            </v-row>

          </v-card-text>
        </v-card>

      </v-col>
    </v-row>

    <div class="discord-embed-wrap text-center">
      <a href="https://discord.com/users/606191901871439903" target="_blank" rel="noopener noreferrer"
        class="discord-embed-link" aria-label="Open Discord profile">
        <img src="https://lanyard.cnrad.dev/api/606191901871439903?hideBadges=true&borderRadius=50&hideProfile=true&bg=2b2930&idleMessage=🎵 Hiding in your Wi-Fi 🎵"
          alt="Discord profile status" class="discord-embed-img" loading="lazy" />
      </a>
    </div>
  </v-container>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'

function appendPrefetchLink(href: string) {
  if (document.head.querySelector(`link[rel="prefetch"][href="${href}"]`)) {
    return
  }

  const link = document.createElement('link')
  link.rel = 'prefetch'
  link.as = 'document'
  link.href = href
  document.head.appendChild(link)
}

function preloadPages() {
  // Warm route chunks for faster first navigation.
  void import('./Social.vue')
  void import('./Projects.vue')
  appendPrefetchLink('/social')
  appendPrefetchLink('/projects')
}

onMounted(() => {
  const requestIdle = (window as Window & {
    requestIdleCallback?: (callback: () => void) => number
  }).requestIdleCallback

  if (requestIdle) {
    requestIdle(preloadPages)
    return
  }

  setTimeout(preloadPages, 120)
})
</script>

<style scoped>
/* Material 3 compliant styles - no custom backdrop filters or glows */

.footer {
  border-top: 1px solid rgba(var(--v-theme-outline-variant), 0.45);
  padding-top: 16px;
}

.footer-logo {
  border: 1px solid rgba(var(--v-theme-outline-variant), 0.45);
}

.btn-icon {
  display: inline-flex;
  align-items: center;
  margin-right: 8px;
}

.btn-icon svg {
  width: 18px;
  height: 18px;
  display: block;
  fill: currentColor;
}

/* Custom Material 3 menu with button styling */
.custom-menu {
  background: rgb(var(--v-theme-surface-container));
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1), 0 8px 16px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  padding: 8px 0;
  min-width: 160px;
  transition: all 0.15s cubic-bezier(0.4, 0, 0.2, 1);
}

.menu-item-btn {
  justify-content: start;
  border-radius: 0 !important;
  margin: 0 !important;
  min-height: 40px !important;
  transition: all 0.15s cubic-bezier(0.4, 0, 0.2, 1);
}

.menu-item-btn:hover {
  background-color: rgba(var(--v-theme-on-surface), 0.08) !important;
  transform: translateX(4px);
}

.menu-item-btn:active {
  transform: translateX(2px);
}

.menu-btn {
  min-width: 48px !important;
  width: 48px !important;
  padding: 0 8px !important;
}

.home-page-container {
  position: relative;
}

.discord-embed-wrap {
  position: absolute;
  left: 50%;
  bottom: 30px;
  transform: translateX(-50%);
  z-index: 1;
}

.discord-embed-link {
  display: inline-flex;
  width: min(100%, 340px);
}

.discord-embed-img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 12px;
}

@media (max-width: 600px) {
  .discord-embed-wrap {
    position: static;
    margin: 16px;
    transform: none;
  }

  .discord-embed-link {
    width: 100%;
    max-width: none;
  }
}

/* Fast scale transition for quick menu opening */
.fast-scale-transition-enter-active,
.fast-scale-transition-leave-active {
  transition: transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.1s cubic-bezier(0.4, 0, 0.2, 1);
}

.fast-scale-transition-enter-from,
.fast-scale-transition-leave-to {
  transform: scale(0.9);
  opacity: 0;
}
</style>

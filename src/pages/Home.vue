<template>
  <v-container fluid class="fill-height bg-surface">
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
                    I make circuits and build hardware.
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
                    <v-btn href="https://blog.nooz.dev" target="_blank" variant="flat" prepend-icon="mdi-post-outline"
                      color="secondary-container">
                      Blog
                    </v-btn>
                    <!-- <v-btn href="https://discord.com/users/606191901871439903" target="_blank" variant="flat"
                      color="secondary-container">
                      <span class="btn-icon" aria-hidden="true">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 126.644 96" width="18" height="18"
                          fill="currentColor" focusable="false" aria-hidden="true">
                          <path
                            d="M81.15,0c-1.2376,2.1973-2.3489,4.4704-3.3591,6.794-9.5975-1.4396-19.3718-1.4396-28.9945,0-.985-2.3236-2.1216-4.5967-3.3591-6.794-9.0166,1.5407-17.8059,4.2431-26.1405,8.0568C2.779,32.5304-1.6914,56.3725.5312,79.8863c9.6732,7.1476,20.5083,12.603,32.0505,16.0884,2.6014-3.4854,4.8998-7.1981,6.8698-11.0623-3.738-1.3891-7.3497-3.1318-10.8098-5.1523.9092-.6567,1.7932-1.3386,2.6519-1.9953,20.281,9.547,43.7696,9.547,64.0758,0,.8587.7072,1.7427,1.3891,2.6519,1.9953-3.4601,2.0457-7.0718,3.7632-10.835,5.1776,1.97,3.8642,4.2683,7.5769,6.8698,11.0623,11.5419-3.4854,22.3769-8.9156,32.0509-16.0631,2.626-27.2771-4.496-50.9172-18.817-71.8548C98.9811,4.2684,90.1918,1.5659,81.1752.0505l-.0252-.0505ZM42.2802,65.4144c-6.2383,0-11.4159-5.6575-11.4159-12.6535s4.9755-12.6788,11.3907-12.6788,11.5169,5.708,11.4159,12.6788c-.101,6.9708-5.026,12.6535-11.3907,12.6535ZM84.3576,65.4144c-6.2637,0-11.3907-5.6575-11.3907-12.6535s4.9755-12.6788,11.3907-12.6788,11.4917,5.708,11.3906,12.6788c-.101,6.9708-5.026,12.6535-11.3906,12.6535Z" />
                        </svg>
                      </span>
                      Discord
                    </v-btn> -->

                    <!-- <v-menu transition="fast-scale-transition" location="bottom end" :close-delay="50" :open-delay="0">
                      <template v-slot:activator="{ props }">
                        <v-btn v-bind="props" variant="flat" color="secondary-container" class="menu-btn">
                          <v-icon>mdi-dots-horizontal</v-icon>
                        </v-btn>
                      </template>
                      <div class="custom-menu">
                        <v-btn href="https://bsky.app/profile/" target="_blank" variant="flat"
                          class="menu-item-btn">
                          <span class="btn-icon" aria-hidden="true">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="18" height="18"
                              fill="currentColor" focusable="false" aria-hidden="true">
                              <path
                                d="M13.873 3.805C21.21 9.332 29.103 20.537 32 26.55v15.882c0-.338-.13.044-.41.867-1.512 4.456-7.418 21.847-20.923 7.944-7.111-7.32-3.819-14.64 9.125-16.85-7.405 1.264-15.73-.825-18.014-9.015C1.12 23.022 0 8.51 0 6.55 0-3.268 8.579-.182 13.873 3.805ZM50.127 3.805C42.79 9.332 34.897 20.537 32 26.55v15.882c0-.338.13.044.41.867 1.512 4.456 7.418 21.847 20.923 7.944 7.111-7.32 3.819-14.64-9.125-16.85 7.405 1.264 15.73-.825 18.014-9.015C62.88 23.022 64 8.51 64 6.55c0-9.818-8.578-6.732-13.873-2.745Z" />
                            </svg>
                          </span>
                          Bluesky
                        </v-btn>
                        <v-btn href="https://twitter.com/" target="_blank" variant="flat"
                          class="menu-item-btn">
                          <span class="btn-icon" aria-hidden="true">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="18" height="18"
                              fill="currentColor" focusable="false" aria-hidden="true">
                              <path d="M30.917 6.728c-1.026 0.465-2.217 0.805-3.464 0.961l-0.061 0.006c1.268-0.771 2.222-1.952 2.687-3.354l0.013-0.044c-1.124 0.667-2.431 1.179-3.82 1.464l-0.082 0.014c-1.123-1.199-2.717-1.946-4.485-1.946-3.391 0-6.14 2.749-6.14 6.14 0 0.496 0.059 0.979 0.17 1.441l-0.008-0.042c-5.113-0.254-9.613-2.68-12.629-6.366l-0.025-0.031c-0.522 0.873-0.831 1.926-0.831 3.052 0 0.013 0 0.026 0 0.039v-0.002c0 0.001 0 0.003 0 0.005 0 2.12 1.075 3.989 2.709 5.093l0.022 0.014c-1.026-0.034-1.979-0.315-2.811-0.785l0.031 0.016v0.075c0 0.001 0 0.002 0 0.002 0 2.961 2.095 5.434 4.884 6.014l0.040 0.007c-0.484 0.135-1.040 0.212-1.614 0.212-0.406 0-0.802-0.039-1.186-0.113l0.039 0.006c0.813 2.459 3.068 4.212 5.739 4.264l0.006 0c-2.072 1.638-4.721 2.627-7.602 2.627-0.005 0-0.009 0-0.014 0h0.001c-0.515-0.001-1.022-0.031-1.521-0.089l0.061 0.006c2.663 1.729 5.92 2.757 9.418 2.757 0.005 0 0.009 0 0.014 0h-0.001c0.037 0 0.082 0 0.126 0 9.578 0 17.343-7.765 17.343-17.343 0-0.039-0-0.077-0-0.116l0 0.006c0-0.262 0-0.524-0.019-0.786 1.21-0.878 2.229-1.931 3.042-3.136l0.028-0.044z" />
                            </svg>
                          </span>
                          Twitter
                        </v-btn>
                        <v-btn href="https://reddit.com/user/" target="_blank" variant="flat"
                          class="menu-item-btn">
                          <span class="btn-icon" aria-hidden="true">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="18" height="18"
                              fill="currentColor" focusable="false" aria-hidden="true">
                              <path d="M32,15.5c0-2.5-2-4.5-4.5-4.5c-1.1,0-2.1,0.4-2.9,1.1c-2-1.1-4.5-1.8-7-2l1.9-3.7L22,7.6c0,0.1,0,0.2,0,0.4 c0,1.7,1.3,3,3,3s3-1.3,3-3s-1.3-3-3-3c-0.8,0-1.5,0.3-2.1,0.8l-3.5-1.7c-0.5-0.2-1.1,0-1.3,0.4L15.4,10c-2.9,0.1-5.7,0.8-7.9,2.1 C6.6,11.4,5.6,11,4.5,11C2,11,0,13,0,15.5c0,1.5,0.8,3,2,3.8c0,0.3,0,0.5,0,0.7c0,5.5,6.3,10,14,10s14-4.5,14-10c0-0.2,0-0.5,0-0.7 C31.2,18.5,32,17,32,15.5z" />
                            </svg>
                          </span>
                          Reddit
                        </v-btn>
                        <v-btn href="https://t.me/" target="_blank" variant="flat"
                          class="menu-item-btn">
                          <span class="btn-icon" aria-hidden="true">
                            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18"
                              fill="currentColor" focusable="false" aria-hidden="true">
                              <path
                                d="M19.2,4.4L2.9,10.7c-1.1,0.4-1.1,1.1-0.2,1.3l4.1,1.3l1.6,4.8c0.2,0.5,0.1,0.7,0.6,0.7c0.4,0,0.6-0.2,0.8-0.4 c0.1-0.1,1-1,2-2l4.2,3.1c0.8,0.4,1.3,0.2,1.5-0.7l2.8-13.1C20.6,4.6,19.9,4,19.2,4.4z M17.1,7.4l-7.8,7.1L9,17.8L7.4,13l9.2-5.8 C17,6.9,17.4,7.1,17.1,7.4z" />
                            </svg>
                          </span>
                          Telegram
                        </v-btn>
                      </div>
                    </v-menu> -->

                    <v-btn to="/projects" variant="flat" color="primary" prepend-icon="mdi-folder-multiple">
                      Projects
                    </v-btn>
                    <v-btn to="/friends" variant="flat" color="primary" prepend-icon="mdi-account-multiple">
                      Friends
                    </v-btn>
                  </div>
                </div>
              </v-col>
            </v-row>

          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

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

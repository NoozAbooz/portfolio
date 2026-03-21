<template>
  <v-container fluid class="fill-height bg-surface">
    <v-row justify="center" align="center">
      <v-col cols="12" sm="10" md="8" lg="6">
        <v-card color="surface-container-high" class="mx-auto">
          <v-card-text class="pa-8 pa-md-12 text-center">
            <p class="text-overline text-medium-emphasis mb-2">Error 404</p>

            <h1 class="text-h2 text-md-h1 font-weight-bold mb-3">
              <span class="climate-font">Page Missing</span>
            </h1>

            <p class="text-h6 text-medium-emphasis mb-8">
              The page you requested does not exist or may have been moved.
            </p>

            <div class="d-flex flex-wrap justify-center ga-3">
              <v-btn to="/" variant="flat" color="primary" prepend-icon="mdi-home">
                Back to Home
              </v-btn>
              <v-btn href="https://blog.nooz.dev" target="_blank" rel="noopener noreferrer" variant="flat" color="secondary-container" prepend-icon="mdi-post-outline">
                Visit Blog
              </v-btn>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
// Material 3 themed 404 page
</script>

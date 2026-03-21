<template>
  <v-app>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
// Material 3 expressive design root component
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');

body {
  margin: 0;
  padding: 0;
  font-family: 'Google Sans Flex', sans-serif;
  overflow-x: hidden;
}

/* Climate Crisis font utility */
.climate-font {
  font-family: 'Climate Crisis', 'Climate Crisis Regular', serif;
  font-weight: 400;
}

/* Language chips - rounded square and even padding */
.lang-chip {
  border-radius: 6px !important;
  padding-inline: 8px !important; /* left/right = 8px */
  padding-block: 6px !important;  /* top/bottom = 6px */
}

/* Smaller chips (Vuetify small modifier) */
.v-chip--size-small.lang-chip,
.v-chip--small.lang-chip {
  padding-inline: 6px !important;
  padding-block: 4px !important;
}

/* Prevent FOUC */
#app {
  min-height: 100vh;
}

.v-application {
  visibility: visible !important;
}
</style>

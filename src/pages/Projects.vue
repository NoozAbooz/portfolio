<template>
    <v-container class="bg-surface">
        <div class="py-8">
            <v-btn to="/" variant="text" prepend-icon="mdi-arrow-left" class="mb-4">
                Back to Home
            </v-btn>

            <h1 class="md:text-h1 sm:text-h2 text-md-h1 font-weight-bold mb-3 title-wrap">
                <span class="climate-font">Projects</span>
            </h1>
            <p class="text-h6 text-medium-emphasis mb-6">
                List of projects I've built and (maybe) maintain
            </p>

            <v-row dense>
                <v-col v-for="project in projects" :key="project.title" cols="12">
                    <v-card color="surface-container-high">
                        <v-card-text class="pa-6">
                            <v-row align="center">
                                <v-col cols="12" md="">
                                    <div class="d-flex align-center mb-2">
                                        <v-avatar v-if="project.logo" size="38" rounded="lg" class="project-logo mr-2">
                                            <v-img :src="project.logo" :alt="`${project.title} logo`" cover />
                                        </v-avatar>
                                        <h2 class="text-h4 font-weight-bold title-wrap">{{ project.title }}</h2>
                                    </div>
                                    <p class="text-body-1 text-medium-emphasis mb-2">{{ project.description }}</p>

                                    <div class="d-flex flex-wrap ga-2 mb-2">
                                        <v-chip class="lang-chip" v-for="lang in project.languages" :key="lang.name" :color="lang.color"
                                            variant="elevated" size="small">
                                            <v-icon v-if="!lang.image" start :icon="lang.icon" />
                                            <svg v-else-if="lang.name === 'Dart'" xmlns="http://www.w3.org/2000/svg"
                                                height="15.4333px" viewBox="0 -960 960 960" width="15.4333px"
                                                class="lang-icon-svg">
                                                <path
                                                    d="M236-345 100-480l440-440h271L236-345ZM540-40 303-277l237-237h271L574-277 811-40H540Z" />
                                            </svg>
                                            <img v-else :src="lang.image" :alt="lang.name" class="lang-icon" />
                                            {{ lang.name }}
                                        </v-chip>
                                    </div>

                                    <div v-if="project.badges.length > 0" class="d-flex flex-wrap ga-2">
                                        <img v-for="(badge, index) in project.badges" :key="index" :src="badge"
                                            :alt="'Badge ' + index" />
                                    </div>
                                </v-col>

                                <v-col v-if="project.image" cols="12" md="3" class="d-flex align-center">
                                    <v-img :src="project.image" :alt="`${project.title} preview`" class="project-image-preview"
                                        contain @click="openLightbox(project)" />
                                </v-col>

                                <v-col cols="12" md="auto">
                                    <div class="d-flex flex-column ga-2">
                                        <v-btn v-for="link in project.links" :key="link.text" :href="link.url"
                                            target="_blank" variant="flat" color="secondary-container"
                                            :prepend-icon="link.icon" block>
                                            {{ link.text }}
                                        </v-btn>
                                    </div>
                                </v-col>
                            </v-row>
                        </v-card-text>
                    </v-card>
                </v-col>
            </v-row>
        </div>

        <v-dialog v-model="lightboxOpen" max-width="1200">
            <v-card color="surface-container-high">
                <v-card-title class="d-flex align-center justify-space-between">
                    <span class="text-h6">{{ activeProject?.title }}</span>
                    <v-btn icon="mdi-close" variant="text" @click="lightboxOpen = false" />
                </v-card-title>
                <v-card-text class="pa-2 pa-md-4">
                    <v-img v-if="activeProject?.image" :src="activeProject.image" :alt="`${activeProject.title} full image`"
                        class="project-image-lightbox" contain />
                </v-card-text>
            </v-card>
        </v-dialog>
    </v-container>
</template>

<script setup lang="ts">
// Material 3 Projects page component
import { ref } from 'vue'

interface ProjectData {
    repo: string
    languages: string
    description: string
    counters?: string
    website?: string
    logo?: string
    image?: string
}

interface ProcessedProject {
    title: string
    description: string
    logo?: string
    image?: string
    languages: Array<{ name: string; color: string; icon: string; image?: string }>
    badges: string[]
    links: Array<{ text: string; url: string; icon: string }>
}

const projectsData: ProjectData[] = [
    {
        repo: 'Amog-OS/AmogOS',
        languages: 'linux',
        description: 'Among Us-themed Linux distribution, based on Debian',
        counters: 'stars,downloads',
        website: 'https://amog-os.github.io',
        logo: 'https://avatars.githubusercontent.com/u/92421659?s=200&v=4',
        image: 'https://camo.githubusercontent.com/141b5cf8e0965626397f2321e3a3aaf5ec33c7b01f1eaad5ca6aa1cb668366bd/68747470733a2f2f692e706f7374696d672e63632f6d32596d397158742f3133303533333936382d64373937653833642d653634332d346336322d393236342d3764343663326236376234382e706e67',
    },
    {
        repo: 'NoozAbooz/210K-PushBack-2026',
        languages: 'vex,c++',
        description: 'Autonomous movement library for the VEX Robotics competition',
        counters: 'stars',
        website: 'https://210k.westernmech.ca',
        logo: 'https://github.com/NoozAbooz/210K-PushBack-2026/blob/v4/logo.png?raw=true'
    },
    {
        repo: 'NoozAbooz/mcpi-reborn-extended',
        languages: 'c++',
        description: 'Extended modding fork for Minecraft Pi Edition [🪦]',
        counters: 'stars,downloads',
        logo: 'https://github.com/NoozAbooz/mcpi-reborn-extended/blob/main/logo.png?raw=true',
        image: 'https://private-user-images.githubusercontent.com/44128563/241611767-bcfab15a-ef0b-4601-b614-81e203945bcd.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzQzOTc1MTEsIm5iZiI6MTc3NDM5NzIxMSwicGF0aCI6Ii80NDEyODU2My8yNDE2MTE3NjctYmNmYWIxNWEtZWYwYi00NjAxLWI2MTQtODFlMjAzOTQ1YmNkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAzMjUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMzI1VDAwMDY1MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTkyYjhhZmViYzk0ODJjMmY4MDliNzQwMzk1YjJjY2UyZDVhZDJjMzA1YTdlZjBmYTNjODBjOWMzM2M1MWYzYjkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.QkRT7ZV0Ce_-Lld6TUKZAeu-Pr1qmDl-dIy2DzukzOI',
    },
    {
        repo: 'NoozAbooz/NoozBoard',
        languages: 'kicad',
        description: 'A custom devboard for the RP2040 microcontroller',
        image: 'https://private-user-images.githubusercontent.com/44128563/506831336-97eca597-97be-41b6-b7b5-8578fe9f976b.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzQzOTc0MDcsIm5iZiI6MTc3NDM5NzEwNywicGF0aCI6Ii80NDEyODU2My81MDY4MzEzMzYtOTdlY2E1OTctOTdiZS00MWI2LWI3YjUtODU3OGZlOWY5NzZiLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAzMjUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMzI1VDAwMDUwN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTM1Yzk0MWMyYjIxOTQwYjUzYzlmNzhiNTA5YjI3OTU4MmJmYjc5NjljNGQ4MjRkMjVjODZiYzIwYWI5M2U0NTYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.Xc3oTkaAidnpf9IiHMPmcio-Xr9Zx7eRts3jqo1gSyI'
    },
    {
        repo: 'NoozAbooz/robotevents-scout',
        languages: 'vex,javascript',
        description: 'Chrome extension for pulling API statistics on robotevents.com',
        logo: 'https://github.com/NoozAbooz/robotevents-scout/blob/main/media/icon128.png?raw=true'
    },
    {
        repo: 'NoozAbooz/Milkis-Discord-Bot',
        languages: 'python',
        description: 'Role-assigning Discord bot for users repping certain status messages',
        counters: 'stars',
        logo: 'https://github.com/NoozAbooz/Milkis-Discord-Bot/blob/v3/icon.png?raw=true'
    },
]

const languageConfig: Record<string, { color: string; icon: string; image?: string }> = {
    kotlin: { color: 'primary', icon: 'mdi-language-kotlin' },
    go: { color: 'secondary', icon: 'mdi-language-go' },
    dart: { color: 'tertiary', icon: 'mdi-code-braces', image: '/flutter.svg' },
    python: { color: 'primary', icon: 'mdi-language-python' },
    typescript: { color: 'secondary', icon: 'mdi-language-typescript' },
    javascript: { color: 'tertiary', icon: 'mdi-language-javascript' },
    linux: { color: 'tertiary', icon: 'mdi-linux' },
    "c++": { color: 'primary', icon: 'mdi-language-cpp' },
    kicad: { color: 'secondary', icon: 'mdi-integrated-circuit-chip' },
    vex: { color: 'tertiary', icon: 'mdi-robot' }
}

function processProjects(data: ProjectData[]): ProcessedProject[] {
    return data.map(project => {
        const hasSlash = project.repo.includes('/')
        const repoName = hasSlash ? project.repo.split('/')[1] : project.repo
        const title = repoName.charAt(0) + repoName.slice(1)

        // Process languages
        const languages = project.languages.split(',').map(lang => {
            const trimmedLang = lang.trim().toLowerCase()
            const config = languageConfig[trimmedLang] || { color: 'primary', icon: 'mdi-code-tags' }
            return {
                name: trimmedLang.charAt(0).toUpperCase() + trimmedLang.slice(1),
                color: config.color,
                icon: config.icon,
                image: config.image
            }
        })

        // Generate badges
        const badges: string[] = []
        if (project.counters) {
            const counters = project.counters.split(',').map(c => c.trim())
            if (hasSlash && counters.includes('stars')) {
                badges.push(`https://img.shields.io/github/stars/${project.repo}?style=flat-square&logo=github`)
            }
            if (hasSlash && counters.includes('downloads')) {
                badges.push(`https://img.shields.io/github/downloads/${project.repo}/total?style=flat-square&logo=github`)
            }
        }

        // Generate links
        const links: Array<{ text: string; url: string; icon: string }> = []
        if (project.website) {
            links.push({
                text: 'Visit Website',
                url: project.website,
                icon: 'mdi-web'
            })
        }
        if (hasSlash) {
            links.push({
                text: 'View on GitHub',
                url: `https://github.com/${project.repo}`,
                icon: 'mdi-github'
            })
        }

        return {
            title,
            description: project.description,
            logo: project.logo,
            image: project.image,
            languages,
            badges,
            links
        }
    })
}

const projects = processProjects(projectsData)
const lightboxOpen = ref(false)
const activeProject = ref<ProcessedProject | null>(null)

function openLightbox(project: ProcessedProject): void {
    activeProject.value = project
    lightboxOpen.value = true
}
</script>

<style scoped>
/* Material 3 compliant styles */
.project-logo {
    border: 1px solid rgba(var(--v-theme-outline-variant), 0.5);
    flex-shrink: 0;
}

.lang-icon {
    width: 24px;
    height: 24px;

    .lang-icon-svg {
        width: 24px;
        height: 24px;
        margin-right: 8px;
        fill: currentColor;
    }

    margin-right: 8px;
    object-fit: contain;
}

/* Prevent title overflow on mobile devices */
.title-wrap {
    word-wrap: break-word;
    overflow-wrap: break-word;
    hyphens: auto;
    max-width: 100%;
}

.project-image-preview {
    border-radius: 14px;
    cursor: zoom-in;
    width: 100%;
    height: auto;
    max-height: 220px;
    background-color: rgba(var(--v-theme-surface-variant), 0.35);
}

.project-image-lightbox {
    max-height: 78vh;
}
</style>

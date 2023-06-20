<script setup lang="ts">
import { computed } from "@vue/reactivity"
import { useStore } from "vuex";

const store = useStore()
const dark = computed(() => store.state.isDark)
const getAssets = (path: string) => {
    return new URL(`/src/assets/${path}`, import.meta.url).href
}
</script>

<template>
    <div class="min-h-screen grid place-items-center bg-gradient-to-b relative"
        :class="dark ? 'from-indigo-900 via-indigo-800 to-blue-400' : 'from-sky-300 via-sky-100 to-sky-300'">
        <div style="transition: transform .5s;"
            :class="dark ? 'scale-[100%] bg-sky-100 shadow-blue-400' : 'scale-[75%] bg-amber-200 shadow-amber-400'"
            class="moon w-32 h-32 sm:w-44 sm:h-44 rounded-full absolute top-[calc(5vh+2.5rem)] right-[20vw] shadow-[0_0_100px_20px]">
        </div>
        <div :class="dark ? 'inv' : ''"
            class="absolute bottom-0 left-0 w-full h-full overflow-hidden [&>img]:absolute [&>img]:bottom-0">
            <img v-for="i in 5" rel="preload" loading="lazy" :alt="`cloud-${i}`" :src="getAssets(`cloud${i}.avif`)"
                :style="`--i:${i}`" />
        </div>
        <div :class="dark ? 'text-indigo-200' : 'text-sky-600'"
            class="z-[1] px-[6vw] py-[calc(1rem+4vw)] flex flex-col items-center font-bold">
            <div class="text-[5rem] flex items-center gap-2">
                <span>4</span>
                <button id="toggle" aria-label="toggle-button" style="transition: color .4s;"
                    @click="store.commit('toggleTheme')"
                    :class="dark ? 'fa-sun bg-indigo-100 shadow-indigo-400 text-indigo-600 hover:text-indigo-900 active:text-indigo-600' : 'fa-moon bg-sky-100 shadow-sky-400 text-sky-600 hover:text-sky-900 active:text-sky-600'"
                    class="fa-solid grid place-items-center shadow-[inset_0_0_15px_3px] w-[4.25rem] h-[4.25rem] text-4xl rounded-full">
                </button>
                <span>4</span>
            </div>
            <span class="text-center -translate-y-3">Oopss... Halaman yang kamu cari tidak ditemukan</span>
        </div>
    </div>
</template>

<style scoped>
@media screen and (max-height: 400px) {
    .moon {
        display: none;
    }
}
</style>
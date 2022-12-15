<script setup lang="ts">
import { onMounted, ref, toRefs } from "vue"
import cloud1 from '@/assets/cloud1.png'
import cloud2 from '@/assets/cloud2.png'
import cloud3 from '@/assets/cloud3.png'
import cloud4 from '@/assets/cloud4.png'
import cloud5 from '@/assets/cloud5.png'
import { useDark, useToggle } from '@vueuse/core';
const isDark = useDark();
const toggleDark = useToggle(isDark);

const props = defineProps({
    code: {
        type: String,
        default: '404'
    },
    message: {
        type: String,
        default: 'Oopss... Halaman yang kamu cari tidak ditemukan'
    }
})

const { code, message } = toRefs(props)

const c1 = ref()
const c2 = ref()
const c3 = ref()
const c4 = ref()
const c5 = ref()

onMounted(() => {
    let cl1 = new Image();
    cl1.src = cloud1
    let cl2 = new Image();
    cl2.src = cloud2
    let cl3 = new Image();
    cl3.src = cloud3
    let cl4 = new Image();
    cl4.src = cloud4
    let cl5 = new Image();
    cl5.src = cloud5
    cl1.onload = () => {
        c1.value = cl1.src
        c2.value = cl2.src
        c3.value = cl3.src
        c4.value = cl4.src
        c5.value = cl5.src
    }
})
</script>
<template>
    <section
        class="relative min-w-screen min-h-screen bg-gradient-to-b from-sky-400 via-amber-50 to-sky-200 dark:from-indigo-900 dark:via-indigo-800 dark:to-blue-400">
        <div style="transition: transform .5s;"
            class="hidden md:block w-44 h-44 scale-[75%] dark:scale-[100%] rounded-full bg-amber-200 dark:bg-sky-100 absolute top-[20vh] right-[20vw] shadow-[0_0_100px_20px] shadow-amber-400 dark:shadow-blue-400">
        </div>
        <div v-for="i in 60" :key="i" v-once
            :style="`top: calc(${Math.round(80 * Math.random())}vh - 6.5rem); left: calc(${Math.round(90 * Math.random())}vw - 4rem); width: ${.2 * Math.random()}rem;  height: ${.2 * Math.random()}rem; animation-duration: ${(i % 7) + 3}s`"
            class="stars translate-x-[-1rem] dark:rotate-[54deg] dark:rounded-full dark:bg-sky-100 dark:absolute dark:shadow-[0_0_6px_2px] dark:shadow-blue-500">
        </div>
        <div class="absolute w-full bottom-0 h-28 bg-gradient-to-b from-[rgba(0,0,0,0)] to-white dark:to-blue-400">
        </div>
        <div
            class="inv absolute top-0 left-0 w-full h-0 dark:h-full overflow-hidden [&>img]:absolute [&>img]:bottom-0 [&>img]:max-w-full">
            <img rel="preload" loading="lazy" :src="c1" style="--i:1" />
            <img rel="preload" loading="lazy" :src="c2" style="--i:2" />
            <img rel="preload" loading="lazy" :src="c3" style="--i:3" />
            <img rel="preload" loading="lazy" :src="c4" style="--i:4" />
            <img rel="preload" loading="lazy" :src="c5" style="--i:5" />
        </div>
        <div
            class="absolute top-0 left-0 w-full h-full dark:h-0 overflow-hidden [&>img]:absolute [&>img]:bottom-0 [&>img]:max-w-full">
            <img rel="preload" loading="lazy" :src="c1" style="--i:1" />
            <img rel="preload" loading="lazy" :src="c2" style="--i:2" />
            <img rel="preload" loading="lazy" :src="c3" style="--i:3" />
            <img rel="preload" loading="lazy" :src="c4" style="--i:4" />
            <img rel="preload" loading="lazy" :src="c5" style="--i:5" />
        </div>
        <div
            class="absolute w-full px-6 bottom-16 text-sky-600 dark:text-sky-100 flex flex-col justify-center items-center">
            <h1 class="!text-[4.25rem] text-center font-extrabold leading-10">{{ code }}</h1>
            <p class="text-lg text-center font-bold mt-6">{{ message }}</p>
        </div>
        <div @click="toggleDark()"
            class="w-12 h-12 grid place-items-center cursor-pointer rounded-full dark:bg-amber-200 bg-sky-100 absolute md:top-[calc(20vh-1rem)] top-4 right-20 md:right-[calc(20vw+10rem)] shadow-[inset_0_0_15px_3px] dark:shadow-amber-400 shadow-blue-600">
            <i class="text-xl"
                :class="[`fa-solid fa-${isDark ? 'sun' : 'moon'}`, isDark ? 'text-amber-700' : 'text-blue-600']"></i>
        </div>
        <slot></slot>
    </section>
</template>

<style scoped>
.stars {
    animation: stars ease-in-out infinite;
}

@keyframes stars {
    0% {
        box-shadow: none;
    }

    25% {
        box-shadow: 0 0 3px 1px;
    }

    50% {
        box-shadow: 0 0 6px 2px;
    }

    75% {
        box-shadow: 0 0 3px 1px;
    }

    100% {
        box-shadow: none;
    }
}

.left-0 img {
    animation: cloud calc(10s * var(--i)) linear infinite;
}

.inv img {
    filter: brightness(0) saturate(100%) invert(66%) sepia(34%) saturate(6212%) hue-rotate(193deg) brightness(108%) contrast(96%)
}

@keyframes cloud {
    0% {
        transform: translateX(-100%);
    }

    100% {
        transform: translateX(100%);
    }
}
</style>
<script setup lang="ts">
import { toRefs } from '@vue/reactivity';
const props = defineProps({
    fill: String,
    core: String,
    layer: String,
    is: {
        type: String,
        default: 'ring'
    },
    width: {
        type: Number,
        default: 24
    },
})

const { fill, core, layer, is, width } = toRefs(props);
const at = 'http://www.w3.org/2000/svg'
</script>

<template>
    <div :id="is">
        <svg v-if="is === 'scale-dots'" :width="width" :height="width" viewBox="0 0 24 24" :xmlns="at">
            <circle class="spinner_b2T7" cx="4" cy="12" r="3" :class="fill" />
            <circle class="spinner_b2T7 spinner_YRVV" cx="12" cy="12" r="3" :class="fill" />
            <circle class="spinner_b2T7 spinner_c9oY" cx="20" cy="12" r="3" :class="fill" />
        </svg>
        <span v-if="is === 'ping'" style="display: flex; position: relative"
            :style="`height: ${width}rem; width: ${width}rem`">
            <span :class="layer" class="animate-ping absolute inline-flex h-full w-full rounded-full opacity-80"></span>
            <span :class="core" class="relative inline-flex rounded-full h-full w-full border-[.1rem] border-solid"></span>
        </span>
    </div>
</template>

<style scoped>
.spinner_b2T7 {
    animation: spinner_xe7Q .8s linear infinite
}

.spinner_YRVV {
    animation-delay: -.65s
}

.spinner_c9oY {
    animation-delay: -.5s
}

@keyframes spinner_xe7Q {

    93.75%,
    100% {
        r: 3px
    }

    46.875% {
        r: .2px
    }
}
</style>
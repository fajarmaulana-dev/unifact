<script setup lang="ts">
import { ref, toRefs } from "vue"

const props = defineProps({
    is: {
        type: String,
        default: 'success'
    },
});

const { is } = toRefs(props);
const text = ref();
if (is.value === 'success') {
    text.value = 'bg-emerald-200 dark:bg-emerald-300 text-emerald-800 dark:text-emerald-900 dark:border-emerald-400 border-emerald-800';
} if (is.value === 'error') {
    text.value = 'bg-rose-200 dark:bg-rose-300 text-rose-800 dark:text-rose-900 dark:border-rose-400 border-rose-800';
} if (is.value === 'info') {
    text.value = 'bg-sky-200 dark:bg-sky-300 text-sky-800 dark:text-sky-900 dark:border-sky-400 border-sky-800';
} if (is.value === 'warning') {
    text.value = 'bg-amber-200 dark:bg-amber-300 text-amber-800 dark:text-amber-900 dark:border-amber-400 border-amber-800';
}

const closed = ref(false)
</script>

<template>
    <section
        class="w-full border-[.15rem] border-solid py-[0.375rem] px-3 rounded-md flex justify-between items-center gap-6"
        :class="text">
        <span>
            <slot></slot>
        </span>
    </section>
</template>
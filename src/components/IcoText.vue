<script setup lang="ts">
import { ref, toRefs, computed } from '@vue/reactivity';
import { onMounted, watch } from '@vue/runtime-core'
// import { createWorker, PSM, OEM } from 'tesseract.js';
import Spinner from './Spinner.vue';
import { useStore } from 'vuex';

const emit = defineEmits(['update:modelValue', 'afterRecognize', 'onEnter', 'onPrepend']);
const props = defineProps({
    id: String,
    type: {
        type: String,
        default: 'text',
    },
    name: {
        type: String,
        default: '',
    },
    placeholder: {
        type: String,
        default: '',
    },
    modelValue: {
        type: String,
        default: ''
    },
    required: {
        type: Boolean,
        default: false
    },
    title: {
        type: String,
        default: ''
    },
    disabled: {
        type: Boolean,
        default: false
    },
    loading: {
        type: Boolean,
        default: false
    },
    autofocus: {
        type: Boolean,
        default: true
    }
})
const { id, type, name, placeholder, modelValue, required, title, disabled, loading, autofocus } = toRefs(props);
const store = useStore()
const isDark = computed(() => store.state.isDark)
const onModel = (e: any) => emit('update:modelValue', e.target.value)

const textModel = ref(modelValue.value)
const state = ref()
const start = ref()
const isRecording = ref(false)
const showPreview = ref(false)
const reset = ref(false)
const Recognition = window.SpeechRecognition || window.webkitSpeechRecognition
const sr = new Recognition()
const inbox = ref()
watch(autofocus, () => {
    if (autofocus.value) {
        inbox.value.focus()
    }
})
onMounted(() => {
    if (autofocus.value) {
        inbox.value.focus()
    }
    sr.continuous = true
    sr.interimResults = true
    sr.lang = 'id'
    sr.onstart = () => {
        console.log('SR Started')
        isRecording.value = true
        showPreview.value = true
        state.value = 'Ucapkan sesuatu ... (Saat selesai, ucapkan "remember" untuk mencari atau ucapkan "forget" untuk mereset ucapan)'
    }
    sr.onend = () => {
        console.log('SR Stopped')
        isRecording.value = false
        showPreview.value = false
        if (textModel.value.length > 0 && start.value) {
            sr.stop()
            emit('afterRecognize')
        }
    }
    sr.onresult = (evt: any) => {
        for (let i = 0; i < evt.results.length; i++) {
            const result = evt.results[i]
            console.log(result)
            const t = result[0].transcript;
            if (t.toLowerCase().includes(' remember')) {
                sr.stop()
                emit('afterRecognize')
            }
            if (t.toLowerCase().includes(' forget')) {
                sr.stop()
                reset.value = true
            }
        }
        const t = Array.from(evt.results)
            .map((result: any) => result[0])
            .map(result => result.transcript)
            .join('')

        if (reset.value === false) {
            textModel.value = t.toLowerCase().replace(' remember', '')
            state.value = textModel.value
        } else {
            textModel.value = ''
        }
        emit('update:modelValue', textModel.value)
        reset.value = false
    }
})

const ToggleMic = () => {
    if (isRecording.value) {
        start.value = false
        sr.stop()
        textModel.value = ''
        emit('update:modelValue', textModel.value)
    } else {
        sr.start()
        start.value = true
    }
}

const onEnter = () => {
    if (isRecording.value) {
        sr.stop()
        emit('afterRecognize')
    }
    else {
        emit('onEnter')
    }
}

// const src = ref()
// const img = ref(null)
// const getFile = (e: any) => {
//     const reader = new FileReader()
//     reader.onload = () => {
//         src.value = reader.result
//     }
//     reader.readAsDataURL(e.target.files[0])
//     showPreview.value = true
//     recognize()
// }

// const worker: any = createWorker({
//     logger: (m: any) => state.value = `${m.status} : ${(m.progress * 100).toFixed(2)}%`
// })

// const recognize = async () => {
//     await worker.load()
//     await worker.loadLanguage('eng+ind')
//     await worker.initialize('eng+ind', OEM.LSTM_ONLY)

//     await worker.setParameters({
//         tessedit_pageseg_mode: PSM.SINGLE_BLOCK,
//     })

//     const { data } = await worker.recognize(img.value)
//     textModel.value = data.text
//     emit('update:modelValue', textModel.value)
//     showPreview.value = false
//     emit('afterRecognize')
// }
// const file = ref()
</script>

<template>
    <section
        :class="[disabled ? (isDark ? '[&>i]:text-slate-200' : '[&>i]:text-slate-200') : (isDark ? '[&>i]:text-sky-300' : '[&>i]:text-sky-600')]"
        class="relative w-full h-[calc(2.5rem+2.5vw)] max-h-11 [&>i]:absolute [&>i]:inset-y-0 [&>i]:w-[calc(.7rem+2.5vw)] [&>i]:min-w-[2.25rem] [&>i]:grid [&>i]:place-items-center">
        <input ref="inbox"
            :title="showPreview ? `Ucapkan sesuatu ... (Saat selesai, ucapkan 'remember' untuk mencari atau ucapkan 'forget' untuk mereset ucapan)` : title"
            :required="required" :type="type" :id="id" :name="name" :placeholder="placeholder" :disabled="disabled"
            :value="showPreview ? state : modelValue" @input="onModel($event)" spellcheck="false" @keyup.enter="onEnter()"
            :class="isDark ? 'text-sky-200 disabled:border-slate-200 border-sky-300 hover:border-sky-200 focus:ring-sky-200 focus:border-sky-300 invalid:border-rose-200 invalid:text-rose-300 focus:invalid:border-rose-300 focus:invalid:ring-rose-200 invalid:hover:border-rose-200' : 'text-sky-600 disabled:border-slate-200 border-sky-600 hover:border-sky-700 focus:ring-sky-500 focus:border-sky-600 invalid:border-rose-500 invalid:text-rose-600 focus:invalid:border-rose-600 focus:invalid:ring-rose-500 invalid:hover:border-rose-700'"
            class="outline-none pr-10 w-full bg-transparent h-full py-[calc(.1rem+1vw)] px-10 md:px-[calc(1.75rem+1.75vw)] border-2 focus:outline-none rounded-md transition duration-300 disabled:cursor-not-allowed focus:ring-2 disabled:shadow-none disabled:ring-0 focus:ring-opacity-50">
        <i title="Deteksi" style="transition: .4s;" class="left-1 cursor-pointer" @click="emit('onPrepend')"
            :class="[(showPreview || loading) ? '' : 'fa-solid fa-magnifying-glass', isDark ? 'hover:text-sky-200 active:text-sky-300' : 'hover:text-sky-700 active:text-sky-600']">
            <Spinner v-if="showPreview || loading" is="scale-dots" :fill="isDark ? 'fill-sky-300' : 'fill-sky-600'" />
        </i>
        <!-- <i title="Deteksi dengan scan" style="transition: .4s;" @click="file.click()"
            class="fa-solid fa-image right-1 cursor-pointer"
            :class="isDark ? 'hover:text-sky-200 active:text-sky-300' : 'hover:text-sky-700 active:text-sky-600'"></i> -->
        <i title="Deteksi dengan ucapan" style="transition: .4s;" @click="ToggleMic(); inbox.focus()"
            class="fa-solid fa-microphone cursor-pointer right-1"
            :class="isDark ? 'hover:text-sky-200 active:text-sky-300' : 'hover:text-sky-700 active:text-sky-600'"></i>
    </section>
    <!-- <input style="display: none" ref="file" id="file" type="file" @change="getFile" />
    <img style="display: none" ref="img" :src="src" /> -->
</template>
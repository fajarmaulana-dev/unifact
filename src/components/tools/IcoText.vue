<script setup lang="ts">
import { onMounted, ref, toRefs } from 'vue';
import { createWorker, PSM, OEM } from 'tesseract.js';
import Spinner from './Spinner.vue';

const emit = defineEmits(['update:modelValue', 'afterRecognize', 'onEnter', 'onPrepend', 'onAppend', 'onMic']);
const props = defineProps({
    id: String,
    prependCursor: {
        type: String,
        default: 'cursor-default',
    },
    appendCursor: {
        type: String,
        default: 'cursor-pointer',
    },
    prependIcon: {
        type: String,
        default: 'fa-solid fa-lock',
    },
    appendIcon: {
        type: String,
        default: 'fa-solid fa-eye',
    },
    is: {
        type: String,
        default: 'basic',
    },
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
    }
})
const { id, is, type, name, placeholder, modelValue, required, title, disabled, loading } = toRefs(props);
const onModel = (e: any) => emit('update:modelValue', e.target.value)

const textModel = ref(modelValue.value)
const state = ref()
const isRecording = ref(false)
const showPreview = ref(false)
const reset = ref(false)
const Recognition = window.SpeechRecognition || window.webkitSpeechRecognition
const sr = new Recognition()
onMounted(() => {
    sr.continuous = true
    sr.interimResults = true
    sr.onstart = () => {
        console.log('SR Started')
        isRecording.value = true
        showPreview.value = true
        state.value = 'Ucapkan sesuatu ...'
    }
    sr.onend = () => {
        console.log('SR Stopped')
        isRecording.value = false
        showPreview.value = false
        if (textModel.value !== '') {
            emit('afterRecognize')
        }
    }
    sr.onresult = (evt: any) => {
        for (let i = 0; i < evt.results.length; i++) {
            const result = evt.results[i]
            if (result.isFinal) CheckForCommand(result)
        }
        const t = Array.from(evt.results)
            .map((result: any) => result[0])
            .map(result => result.transcript)
            .join('')

        if (reset.value === false) {
            textModel.value = t.toLowerCase().replace(' open', '')
            state.value = textModel.value
        } else {
            textModel.value = ''
        }
        emit('update:modelValue', textModel.value)
        reset.value = false
    }
})

const CheckForCommand = (result: any) => {
    const t = result[0].transcript;
    if (t.toLowerCase().includes(' open')) {
        sr.stop()
        emit('afterRecognize')
    }
    if (t.toLowerCase().includes(' forget')) {
        sr.stop()
        reset.value = true
    }
}
const ToggleMic = () => {
    if (isRecording.value) {
        sr.stop()
    } else {
        sr.start()
    }
}
const src = ref()
const img = ref(null)
const getFile = (e: any) => {
    const reader = new FileReader()
    reader.onload = () => {
        src.value = reader.result
    }
    reader.readAsDataURL(e.target.files[0])
    showPreview.value = true
    recognize()
}

const worker = createWorker({
    logger: (m: any) => state.value = `${m.status} : ${(m.progress * 100).toFixed(2)}%`
})

const recognize = async () => {
    await worker.load()
    await worker.loadLanguage('eng')
    await worker.initialize('eng', OEM.LSTM_ONLY)

    await worker.setParameters({
        tessedit_pageseg_mode: PSM.SINGLE_BLOCK,
    })

    const { data } = await worker.recognize(img.value)
    textModel.value = data.text
    emit('update:modelValue', textModel.value)
    showPreview.value = false
    emit('afterRecognize')
}
const file = ref()
</script>

<template>
    <section
        :class="[disabled ? '[&>i]:text-slate-200 [&>i]:dark:text-slate-200' : '[&>i]:text-sky-600 [&>i]:dark:text-sky-300']"
        class="relative w-full h-[calc(2.5rem+2.5vw)] max-h-11 [&>i]:absolute [&>i]:inset-y-0 [&>i]:w-[calc(.7rem+2.5vw)] [&>i]:min-w-[2.25rem] [&>i]:grid [&>i]:place-items-center">
        <input :required="required" :type="type" :id="id" :name="name" :placeholder="placeholder" :disabled="disabled"
            :value="showPreview ? state : modelValue" @input="onModel($event)" spellcheck="false"
            @keyup.enter="$emit('onEnter')" :class="is === 'search' ? '!pr-20 md:!pr-[calc(1.25rem+6vw)]' : ''"
            class="outline-none w-full bg-transparent h-full py-[calc(.1rem+1vw)] px-10 md:px-[calc(1.75rem+1.75vw)] text-sky-600 dark:text-sky-200 border-2 focus:outline-none rounded-md transition duration-300 disabled:cursor-not-allowed focus:ring-2 disabled:border-slate-200 dark:disabled:border-slate-200 disabled:shadow-none disabled:ring-0 border-sky-600 dark:border-sky-300 hover:border-sky-700 dark:hover:border-sky-200 focus:ring-sky-500 dark:focus:ring-sky-200 focus:ring-opacity-50 focus:border-sky-600 dark:focus:border-sky-300 invalid:border-rose-500 invalid:text-rose-600 focus:invalid:border-rose-600 focus:invalid:ring-rose-500 hover:invalid:hover:border-rose-700 dark:invalid:border-rose-200 dark:invalid:text-rose-300 dark:focus:invalid:border-rose-300 dark:focus:invalid:ring-rose-200 dark:invalid:hover:border-rose-200">
        <i :title="title" class="left-1" @click="$emit('onPrepend')"
            :class="[is === 'search' && (showPreview || loading) ? '' : is === 'search' && (!showPreview && !loading) ? 'fa-solid fa-magnifying-glass' : prependIcon, prependCursor, prependCursor === 'cursor-pointer' ? 'hover:text-sky-700 dark:hover:text-sky-200 active:text-sky-600 dark:active:text-sky-300' : '']">
            <Spinner v-if="showPreview || loading" is="scale-dots" fill="fill-sky-600 dark:fill-sky-300" />
        </i>
        <i :title="is === 'search' ? 'Cari dengan scan' : title"
            @click="is === 'search' ? file.click() : $emit('onAppend')" class="right-1"
            :class="[is === 'search' ? 'fa-solid fa-image' : appendIcon, appendCursor, appendCursor === 'cursor-pointer' ? 'hover:text-sky-700 dark:hover:text-sky-200 active:text-sky-600 dark:active:text-sky-300' : '']"></i>
        <i title="Cari dengan ucapan" v-if="is === 'search'" @click="is === 'search' ? ToggleMic() : $emit('onMic')"
            class="fa-solid fa-microphone right-9 md:right-[calc(.6rem+2.75vw)] cursor-pointer hover:text-sky-700 dark:hover:text-sky-200 active:text-sky-600 dark:active:hover:text-sky-300"></i>
    </section>
    <input style="display: none" ref="file" id="file" type="file" @change="getFile" />
    <img style="display: none" ref="img" :src="src" />
</template>
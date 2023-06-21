<script setup lang="ts">
import { computed, ref, reactive } from "@vue/reactivity";
import { onMounted } from "@vue/runtime-core";
import { useStore } from "vuex";
import IcoText from "@/components/IcoText.vue";
import Spinner from "@/components/Spinner.vue";
import Toast from "@/components/Toast.vue";
import { usePredict } from "@/api/predict";

const store = useStore()
const dark = computed(() => store.state.isDark)
const model = ref('')
const bool = reactive({
    load: false,
    open: false,
    toast: false,
    bulb: false,
    ping: true,
    focus: true
})
const { error, prediction, predict } = usePredict()

const getAssets = (path: string) => {
    return new URL(`/src/assets/${path}`, import.meta.url).href
}

const getPrediction = async () => {
    if (model.value.length > 0) {
        bool.load = true
        await predict({ text: model.value })
        bool.load = false
        if (error.value.length == 0) bool.open = true
        else bool.toast = true
    }
}

const medias = [
    { src: 'turnbackhoax.avif', to: 'http://turnbackhoax.id/' },
    { src: 'kominfo.avif', to: 'https://www.kominfo.go.id/content/all/laporan_isu_hoaks' },
    { src: 'cnnindonesia.avif', to: 'https://www.cnnindonesia.com/tag/cek-fakta' },
    { src: 'detik.avif', to: 'https://hoaxornot.detik.com/' },
    { src: 'kompas.avif', to: 'https://www.kompas.com/cekfakta' },
    { src: 'liputan6.avif', to: 'https://www.liputan6.com/cek-fakta' },
    { src: 'medcom.avif', to: 'https://www.medcom.id/cekfakta/' },
    { src: 'tempo.avif', to: 'https://cekfakta.tempo.co/' },
]

const socials = [
    { ico: 'github', url: 'https://github.com/fajarmaulana-dev' },
    { ico: 'linkedin-in', url: 'https://www.linkedin.com/in/fajar-maulana-16b98b152' },
    { ico: 'facebook', url: 'https://web.facebook.com/profile.php?id=100090702398845' },
]

const screenWidth = ref(window.innerWidth)
onMounted(async () => {
    window.addEventListener('resize', () => {
        screenWidth.value = window.innerWidth;
    })
})

const few = [['imposter', 'false', 'valid'], ['Fabricated Content/Imposter Content', 'Misleading Content/False Context/Manipulated Content', 'Valid']]
const end: any = { Misleading: 'rose', Fabricated: 'amber', Valid: 'emerald' }
const color = computed(() => `text-${end[prediction.value?.prediction?.split(' ')[0]]}-${dark.value ? '300' : '600'}`)
const detail = (prob: any) => `text-${end[prob?.class.split(' ')[0]]}-${dark.value ? '300' : '600'}`
const explanation = (i: number) => {
    return {
        text: `text-${end[few[1][i].split(' ')[0]]}-${dark.value ? '300' : '600'}`,
        other: `bg-${end[few[1][i].split(' ')[0]]}-${dark.value ? '300' : '600'} text-${dark.value ? 'slate-800' : 'teal-50'}`
    }
}

const hoaxes = [
    { title: 'Satire atau Parody', desc: 'konten tidak memiliki niat untuk merugikan, akan tetapi konten tersebut memiliki potensi untuk mengelabuhi' },
    { title: 'Misleading Content', desc: 'digunakannya informasi yang menyesatkan pada suatu konten untuk membingkai sebuah isu atau individu tertentu' },
    { title: 'Imposter Content', desc: 'konten palsu yang dibuat dengan meniru sumber aslinya' },
    { title: 'Fabricated Content', desc: 'konten yang 100% salah dan dibuat untuk merugikan serta menipu pengaksesnya' },
    { title: 'False Connection', desc: 'ketika judul, gambar, atau keterangannya tidak mendukung konten yang dipublikasikan' },
    { title: 'False Context', desc: 'ketika konten yang asli dipadankan dengan konteks informasi yang salah' },
    { title: 'Manipulated Content', desc: 'ketika informasi atau gambar yang asli dimanipulasi oleh penipu untuk mengelabuhi' },
]

const tempel = [
    { img: 'tempel1.avif', text: 'Salin narasi yang ingin dicek kebenarannya, misalnya narasi pada tautan', suffix: 'berikut ini', link: 'https://twitter.com/Qazalyn/status/1607088863268462592' },
    { img: 'tempel2.avif', text: 'Tempel pada kolom input UniFACT, kemudian tekan enter atau bisa juga dengan klik tombol "lup" di bagian kiri kolom input seperti pada tangkapan layar di bawah ini', suffix: '', link: '' },
    { img: 'tempel3.avif', text: 'Tunggu proses klasifikasi yang ditandai dengan animasi pada kolom input. Setelah selesai, bilah akan otomatis terbuka dengan hasil prediksinya. Untuk menutup bilah, klik tombol "arah ke bawah" pada bagian tengah atas bilah', suffix: '', link: '' },
]

const speech = [
    { img: 'stt1.avif', text: 'Klik tombol “microphone” pada kolom input' },
    { img: 'stt2.avif', text: 'Ucapkan narasi yang ingin dicek kebenarannya dengan jelas dan tidak terlalu cepat' },
    { img: 'stt3.avif', text: 'Untuk mengakhiri ucapan dan melihat hasil prediksi, akhiri ucapan dengan kata "remember" atau bisa juga dengan langsung menekan tombol enter. Sedangkan apabila ingin mengakhiri ucapan  dengan tujuan untuk mereset ucapan, akhiri ucapan dengan kata "forget" atau bisa juga dengan klik ulang tombol "microphone". Untuk menutup bilah, klik tombol "arah ke bawah" pada bagian tengah atas bilah' },
]
</script>

<template>
    <div class="min-h-screen grid place-items-center bg-gradient-to-b relative"
        :class="dark ? 'from-indigo-900 via-indigo-800 to-blue-400' : 'from-sky-300 via-sky-100 to-sky-300'">

        <!-- Social Media -->
        <div class="absolute z-[2] w-full top-[calc(1rem+.5vw)] left-[calc(1rem+.5vw)] flex gap-2 [&>*]:grid [&>*]:place-items-center [&>*]:shadow-[inset_0_0_15px_3px] [&>*]:w-6 [&>*]:h-6 sm:[&>*]:w-8 sm:[&>*]:h-8 [&>*]:text-sm [&>*]:sm:text-base [&>*]:rounded-full"
            :class="dark ? '[&>*]:bg-indigo-100 [&>*]:shadow-indigo-400 [&>*]:text-indigo-600 hover:[&>*]:text-indigo-900' : '[&>*]:bg-sky-100 [&>*]:shadow-sky-300 [&>*]:text-sky-600 hover:[&>*]:text-sky-900'">
            <a href="https://fajarmaulana-dev.netlify.app" target="_blank" aria-label="Go to developers blog"
                style="transition: .4s;" class="fa-solid fa-blog"></a>
            <a v-for="social, i in socials" :key="i" :href="social.url" target="_blank" style="transition: .4s;"
                :aria-label="`Go to developers ${social.ico} account`" :class="`fa-brands fa-${social.ico}`"></a>
        </div>

        <!-- Background -->
        <div :class="dark ? '[&>button]:bg-indigo-100 [&>button]:shadow-indigo-400 [&>button]:text-indigo-600 hover:[&>button]:text-indigo-900 active:[&>button]:text-indigo-600' : '[&>button]:bg-sky-100 [&>button]:shadow-sky-300 [&>button]:text-sky-600 hover:[&>button]:text-sky-900 active:[&>button]:text-sky-600'"
            class="[&>button]:grid [&>button]:place-items-center [&>button]:shadow-[inset_0_0_15px_3px] [&>button]:w-10 [&>button]:h-10 sm:[&>button]:w-12 sm:[&>button]:h-12 [&>button]:text-base sm:[&>button]:text-xl [&>button]:rounded-full [&>button]:absolute [&>button]:z-[2]">
            <div :class="dark ? '' : 'hidden'">
                <div v-for="i in Math.floor(screenWidth / 25)" :key="i" v-once
                    class="stars absolute bg-sky-100 rotate-[54deg] rounded-full"
                    :style="`top: calc(${Math.round(80 * Math.random())}vh - 6.5rem); left: calc(${Math.round(90 * Math.random())}vw - 4rem); width: ${.2 * Math.random()}rem;  height: ${.2 * Math.random()}rem; animation-duration: ${(i % 7) + 3}s`">
                </div>
            </div>
            <div :class="dark ? 'inv' : ''"
                class="absolute bottom-0 left-0 w-full h-full overflow-hidden [&>img]:absolute [&>img]:bottom-0">
                <img v-for="i in 5" rel="preload" loading="lazy" :alt="`cloud-${i}`" :src="getAssets(`cloud${i}.avif`)"
                    :style="`--i:${i}`" />
            </div>
            <div style="transition: transform .5s;"
                :class="dark ? 'scale-[100%] bg-sky-100 shadow-blue-400' : 'scale-[75%] bg-amber-200 shadow-amber-400'"
                class="moon w-32 h-32 sm:w-44 sm:h-44 rounded-full absolute top-[calc(5vh+2.5rem)] right-[20vw] shadow-[0_0_100px_20px]">
            </div>

            <!-- Feature Button -->
            <button id="toggle" aria-label="toggle-button" style="transition: color .4s;"
                @click="store.commit('toggleTheme')" :class="`fa-${dark ? 'sun' : 'moon'}`"
                class="fa-solid relative feature sun top-[calc(5vh+1rem)] sm:top-[calc(5vh+1.5rem)] right-[calc(20vw+7rem)] sm:right-[calc(20vw+10rem)]">
            </button>
            <button id="info" aria-label="info-button" style="transition: color .4s;" @click="bool.bulb = true"
                class="fa-solid fa-lightbulb feature bulb top-[calc(5vh+9.5rem)] sm:top-[calc(5vh+11.5rem)] right-[calc(20vw-1.5rem)] sm:right-[calc(20vw-2rem)]">
                <Spinner is="ping" :core="dark ? 'bg-indigo-700 border-indigo-100' : 'bg-sky-800 border-sky-100'"
                    :layer="dark ? 'bg-indigo-600' : 'bg-sky-700'" :width=".45"
                    class="absolute notif top-[.5rem] right-[.8rem] sm:top-[.675rem] sm:right-[.95rem]" />
            </button>
        </div>

        <!-- Main Feature -->
        <div class="w-full z-[1] flex flex-col gap-12 px-[6vw] py-[calc(1rem+4vw)]">
            <div class="w-full min-h-[calc(50vh-4vw-1rem)] pt-[calc(2rem+4vw)] flex flex-col justify-end gap-6">
                <h1 class="text-center font-black text-4xl sm:text-5xl leading-[1px] sm:leading-[1px]"
                    :class="dark ? 'text-sky-200' : 'text-blue-500'">Uni<span
                        :class="dark ? 'text-amber-200' : 'text-teal-500'">FACT</span>
                </h1>
                <p class="font-bold text-sm text-center sm:mb-4" :class="dark ? 'text-sky-200' : 'text-blue-500'">
                    deep learning based app for
                    <span class="whitespace-nowrap" :class="dark ? 'text-amber-200' : 'text-teal-500'">
                        Indonesian hoax classification</span>
                </p>
                <IcoText v-model="model" :autofocus="bool.focus" :loading="bool.load" @on-prepend="getPrediction"
                    @on-enter="getPrediction" @after-recognize="getPrediction"
                    title="Untuk pengalaman terbaik, ketikkan narasi berita minimal 20 kata jika ada." />
            </div>
            <div :class="dark ? '[&_span]:text-white' : '[&_span]:text-blue-500'"
                class="w-full min-h-[calc(40vh-8vw-1rem)] flex flex-col lg:flex-row justify-end gap-8 lg:gap-0 lg:justify-around lg:items-end [&>div]:font-bold [&>div]:flex [&>div]:flex-col [&>div]:items-center [&>div]:gap-1.5 [&_span]:text-center">
                <div>
                    <span>Situs cek fakta pilihan</span>
                    <div class="flex gap-3 flex-wrap justify-center">
                        <a v-for="media, i in medias" :key="i" :href="media.to" target="_blank"
                            :aria-label="`Go to ${media.src.split('.')[0]}`"
                            :title="`Ke halaman ${media.src.split('.')[0]}`" style="transition: .4s;"
                            :class="dark ? 'border-blue-400 hover:border-white' : 'border-sky-300 hover:border-sky-100'"
                            class="w-10 h-10 bg-white border-2 rounded-md p-1.5 grid place-items-center cursor-pointer">
                            <img :src="getAssets(media.src)" rel="preload" loading="lazy" width="28" height="28"
                                :alt="`logo ${media.src.split('.')[0]}`" />
                        </a>
                    </div>
                </div>
                <div>
                    <span>Sudah coba aplikasinya ?</span>
                    <a href="'https://forms.gle/TFs7Dy5Raf7m2Gjk8'" target="_blank" style="transition: .4s;"
                        aria-label="Go to form"
                        :class="dark ? 'border-blue-400 hover:border-white text-blue-400 bg-white' : 'border-blue-200 hover:border-blue-500 text-white bg-blue-500'"
                        class="flex justify-center items-center border-2 gap-3 py-2 text-sm sm:text-base lg:py-0 lg:h-10 px-3.5 rounded-md">
                        <i class="fa-solid fa-paper-plane"></i>
                        <p>Bagikan pendapatmu tentang UniFACT</p>
                    </a>
                </div>
            </div>
        </div>

        <!-- Blade -->
        <div style="transition: transform .5s;"
            :class="[dark ? 'bg-slate-800 shadow-slate-900' : 'bg-teal-50 shadow-teal-400', bool.open || bool.bulb ? 'translate-y-0' : 'translate-y-[100%]']"
            class="absolute pb-16 [&_p]:text-sm [&_p]:font-medium [&_li]:text-sm [&_b]:text-sm [&_em]:text-sm [&_h2]:text-lg [&_h4]:text-sm [&_h5]:text-xs w-full h-[80vh] left-0 bottom-0 z-[3] rounded-t-3xl shadow-[0_5px_20px_1px]">
            <div class="relative w-full h-10">
                <span style="transition: .3s" @click="bool.open = false; bool.bulb = false; model = ''; bool.focus = true"
                    :class="dark ? 'bg-sky-300 hover:bg-sky-200 text-slate-800' : 'bg-teal-500 hover:bg-teal-600 text-teal-50'"
                    class="group absolute top-0 left-[calc(50vw-1.5rem)] h-5 w-12 rounded-b-full grid place-items-center cursor-pointer">
                    <i style="transition: .3s"
                        class="fa-solid fa-chevron-down -translate-y-[.15rem] group-hover:translate-y-0"></i>
                </span>
            </div>
            <div v-if="bool.open" class="w-full h-full pt-2">
                <!-- Alert -->
                <div v-if="prediction?.withoutStopword === ''" class="h-full grid place-items-center w-full mb-5">
                    <div :class="dark ? '[&>*]:text-amber-300' : '[&>*]:text-amber-600'"
                        class="flex flex-col items-center gap-3 font-bold [&>*]:text-center p-[calc(2rem+2vw)]">
                        <i class="fa-solid fa-triangle-exclamation text-[calc(4rem+4vw)] mb-[1vw]"></i>
                        <p>Oopss... Narasi yang kamu masukkan hanya memuat stopword (kata yang tidak begitu penting
                            untuk diprediksi), sehingga prediksi tidak dapat dilakukan.<br />
                            Silakan coba lagi dengan narasi yang berbeda.</p>
                        <em style="transition: .4s" class="cursor-pointer"
                            :class="dark ? 'text-amber-300 hover:text-amber-100 active:text-amber-300' : '!text-teal-500 hover:!text-teal-700 active:!text-teal-500'">
                            Lihat daftar stopword >></em>
                    </div>
                </div>
                <!-- prediction -->
                <div v-else :class="dark ? 'dark' : 'light'" class="w-full h-full overflow-y-auto px-[calc(.5rem+2.5vw)]">
                    <div v-if="few[0].every((i: string) => prediction?.existence[i] == 0) || prediction?.withoutStopword?.split(' ').length < 4"
                        :class="dark ? 'bg-amber-300 text-amber-900 border-amber-400' : 'bg-amber-200 text-amber-800 border-amber-800'"
                        class="w-full border-[.15rem] border-solid py-[0.375rem] px-3 rounded-md flex justify-between items-center gap-6 mb-5">
                        <div>
                            <b class="mb-[calc(1rem+1vw)] !text-base">Perhatian!</b><br />
                            <p>{{
                                prediction?.withoutStopword?.split(' ').length < 4
                                ? 'Narasi bersih (tanpa stopword) terlalu singkat'
                                : 'Corpus tidak memuat satupun kata pada narasi' }}. Prediksi mungkin tidak akurat.</p>
                        </div>
                    </div>
                    <div :class="dark ? 'text-sky-300' : 'text-teal-900'">
                        <div
                            class="grid grid-cols-1 gap-[calc(1.5rem+2vw)] sm:grid-cols-2 [&>div]:w-full [&>div]:h-full [&>div>h2]:w-full [&>div>h2]:mb-2 [&>div>h2]:text-center [&>div>h2]:font-bold">
                            <div>
                                <h2>Narasi Asli</h2>
                                <p class="text-center">{{ model }}</p>
                            </div>
                            <div>
                                <h2>Narasi Normal</h2>
                                <p class="text-center">{{ prediction?.normalNaration }}</p>
                            </div>
                            <div class="flex flex-col items-center">
                                <h2>Rincian Probabilitas</h2>
                                <div>
                                    <div v-for="(prob, index) in prediction?.probability" :key="index" :class="detail(prob)"
                                        class="flex mb-1 items-center [&>*]:font-bold">
                                        <h3 class="min-w-[calc(3.5rem+3.5vw)]">{{ prob.probs }}</h3>
                                        <h4>{{ prob.class }}</h4>
                                    </div>
                                </div>
                            </div>
                            <div>
                                <h2>Prediksi Akhir</h2>
                                <div class="w-full flex justify-center items-center my-3">
                                    <i :class="[prediction?.ico, color]" class="text-[3.5rem]"></i>
                                </div>
                                <p :class="color" class="text-center !font-bold">{{
                                    prediction?.prediction
                                }}</p>
                            </div>
                        </div>
                        <div class="[&>h2]:mb-2 [&>h2]:text-center [&>h2]:font-bold mt-[calc(1.5rem+2vw)]">
                            <h5 class="bg-emerald-300 bg-rose-600 bg-rose-300 bg-emerald-600 bg-amber-600 text-teal-50">
                            </h5>
                            <h2>Penjelasan</h2>
                            <p>Berdasarkan dominasi kata pada data train yang digunakan, diperoleh fakta bahwa frekuensi
                                tiap kata dari narasi pada tiap kelas dataset adalah sebagai berikut :</p>
                            <div v-for="fe, f in few[0]">
                                <h4 class="font-bold mt-4 mb-1" :class="explanation(f).text">
                                    {{ few[1][f] }}</h4>
                                <div
                                    class="flex gap-2 flex-wrap [&>h5]:rounded-md [&>h5]:py-1 [&>h5]:px-3 [&>h5]:font-bold">
                                    <h5 v-for="(record, index) in prediction?.record[fe]" :key="index"
                                        :class="explanation(f).other">
                                        {{ record.word }}: {{ record.num }}x</h5>
                                </div>
                            </div>
                            <div class="[&>p]:mb-2 [&_span]:font-bold">
                                <p class="mt-4">Dari data di atas, dominasi kata pada kelas <span
                                        :class="dark ? 'text-amber-300' : 'text-amber-600'">Fabricated
                                        Content/Imposter Content</span> adalah sebanyak <span
                                        :class="dark ? 'text-amber-300' : 'text-amber-600'">
                                        {{ prediction?.domination?.imposter }} kali</span>, pada kelas <span
                                        :class="dark ? 'text-rose-300' : 'text-rose-600'">
                                        Misleading Content/False Context/Manipulated Content</span> adalah <span
                                        :class="dark ? 'text-rose-300' : 'text-rose-600'">
                                        {{ prediction?.domination?.false }} kali</span>, dan pada kelas
                                    <span :class="dark ? 'text-emerald-300' : 'text-emerald-600'">Valid</span> adalah <span
                                        :class="dark ? 'text-emerald-300' : 'text-emerald-600'">
                                        {{ prediction?.domination?.valid }} kali</span>.
                                </p>
                                <p>Sedangkan berdasarkan eksistensi katanya, sebanyak <span
                                        :class="dark ? 'text-amber-300' : 'text-amber-600'">
                                        {{ prediction?.existence?.imposter }} kata </span>
                                    pada narasi ada pada corpus kelas <span
                                        :class="dark ? 'text-amber-300' : 'text-amber-600'">
                                        Fabricated Content/Imposter Content</span>, <span
                                        :class="dark ? 'text-rose-300' : 'text-rose-600'">
                                        {{ prediction?.existence?.false }} kata </span>ada pada corpus kelas <span
                                        :class="dark ? 'text-rose-300' : 'text-rose-600'">
                                        Misleading Content/False Context/Manipulated Content</span>, dan <span
                                        :class="dark ? 'text-emerald-300' : 'text-emerald-600'">
                                        {{ prediction?.existence?.valid }} kata </span>ada pada corpus kelas <span
                                        :class="dark ? 'text-emerald-300' : 'text-emerald-600'">Valid</span>.
                                </p>
                                <p>Mempertimbangkan banyaknya dominasi kata, eksistensi kata, dan urutan
                                    bobot nilai linguistik yang diberikan oleh jaringan saraf, model
                                    memprediksi bahwa narasi tersebut masuk pada kelas
                                    <span class="font-bold" :class="color"> {{ prediction?.prediction }}</span>.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div v-if="bool.bulb" :class="dark ? 'text-sky-300 dark' : 'text-teal-900 light'"
                class="w-full h-full py-5 overflow-y-auto p-[calc(.5rem+2.5vw)]">
                <h2 class="w-full text-center font-bold mb-6">Tahukah Kamu ?</h2>
                <p class="mb-3">Berdasarkan analisis dari <a target="_blank" aria-label="FirstDraft"
                        href="https://firstdraftnews.org/articles/fake-news-complicated/"
                        class="underline font-bold">FirstDraft (2017)</a>,
                    sebuah koalisi non profit internasional pada bidang etika jurnalistik, misinformasi dan
                    disinformasi memiliki sebanyak tujuh klasifikasi yaitu:</p>
                <div v-for="hoax, index in hoaxes" :key="index" class="flex">
                    <b class="min-w-[1.5rem]">{{ index + 1 }}.</b>
                    <p><b>{{ hoax.title }}</b>, yaitu {{ hoax.desc }}.</p>
                </div>
                <p class="my-3">Masalah klasifikasi ini dapat diselesaikan secara otomatis menggunakan model Deep
                    Learning. Secara singkat, model Deep Learning terutama untuk masalah klasifikasi teks dapat
                    dikatakan sebagai persamaan kurva yang dapat mengelompokkan data masukan ke dalam kelompok kelas
                    tertentu berdasarkan hasil pemberian makna linguistik terhadap setiap kata pada dataset.</p>
                <p>Untuk itu, sebagai syarat penyelesaian skripsi, pengembang mencoba membangun aplikasi dengan
                    model Deep Learning berarsitektur <b>Bidirectional Temporal Convolutional Network</b>
                    yang mana berdasarkan uji coba, dapat menghasilkan model yang lebih baik dari arsitektur lainnya
                    seperti CNN, LSTM, dan GRU. Model yang terpasang pada aplikasi ini dapat mengklasifikasikan
                    narasi ke dalam tiga klasifikasi, yaitu Valid, Misleading Content/False Context/Manipulated
                    Content, dan Fabricated Content/Imposter Content. Model belum dapat mengklasifikasikan secara
                    lengkap dikarenakan masih kurangnya data pada beberapa kelas. Sedangkan penggabungan beberapa
                    kelas dilakukan berdasarkan adanya kemiripan dari kelas yang digabung.</p>
                <h2 class="w-full text-center font-bold mb-6 mt-12">Cara Penggunaan Aplikasi</h2>
                <div class="mb-4 flex flex-col">
                    <h3 class="font-bold mb-2 mt-4">Dengan cara mengetik atau salin tempel</h3>
                    <div v-for="temp, index in tempel" :key="index"
                        class="mb-2 flex flex-col lg:flex-row gap-[calc(.5rem+.5vw)] justify-center items-center">
                        <p class="w-full lg:w-[50%]">{{ temp.text }} <a style="transition: .3s" class="underline font-bold"
                                :class="dark ? 'text-indigo-300 hover:text-indigo-200 active:text-indigo-300' : 'text-blue-500 hover:text-blue-600 active:text-blue-500'"
                                :href="temp.link" target="_blank" :aria-label="`paste-${index}`">{{ temp.suffix }}</a>.</p>
                        <img :src="getAssets(temp.img)" :alt="`paste${index}`" class="w-full lg:w-[50%] mb-3" />
                    </div>
                </div>
                <div class="mb-4 flex flex-col">
                    <h3 class="font-bold mb-2 mt-4">Dengan menggunakan fitur Speech-to-Text (Speech Recognition)</h3>
                    <div v-for="temp, index in speech" :key="index"
                        class="mb-2 flex flex-col lg:flex-row gap-[calc(.5rem+.5vw)] justify-center items-center">
                        <p class="w-full lg:w-[50%]">{{ temp.text }}</p>
                        <img :src="getAssets(temp.img)" :alt="`speech-to-text-${index}`" class="w-full lg:w-[50%] mb-3" />
                    </div>
                </div>
            </div>
        </div>
        <Toast is="error" v-model="bool.toast" :text="error" />
    </div>
</template>

<style scoped>
.overflow-y-auto::-webkit-scrollbar-thumb {
    border-radius: 5px 0 0 5px;
}

.dark::-webkit-scrollbar-thumb {
    background-color: #7dd3fc;
}

.dark::-webkit-scrollbar-thumb:hover {
    background-color: #bae6fd;
}

.light::-webkit-scrollbar-thumb {
    background-color: #14b8a6;
}

.light::-webkit-scrollbar-thumb:hover {
    background-color: #0d9488;
}

@media screen and (max-height: 720px) {
    .moon {
        display: none;
    }

    .feature {
        top: calc(1rem + .5vw) !important;
    }

    .bulb {
        right: calc(1rem + .5vw) !important;
    }
}

@media screen and (max-height: 720px) and (min-width: 40rem) {
    .feature {
        width: 2rem !important;
        height: 2rem !important;
        font-size: 1rem !important;
    }

    .sun {
        right: calc(3.5rem + .5vw) !important;
    }

    .notif {
        top: .25rem !important;
        right: .6rem !important;
    }
}

@media screen and (max-height: 720px) and (max-width: 39.995rem) {
    .feature {
        width: 1.5rem !important;
        height: 1.5rem !important;
        font-size: .825rem !important;
    }

    .sun {
        right: calc(3rem + .5vw) !important;
    }

    .notif {
        top: .1rem !important;
        right: .375rem !important;
    }
}

.stars {
    animation: stars ease-in-out infinite;
}

@keyframes stars {
    0% {
        box-shadow: none;
    }

    25% {
        box-shadow: 0 0 3px 1px #3b82f6;
    }

    50% {
        box-shadow: 0 0 6px 2px #3b82f6;
    }

    75% {
        box-shadow: 0 0 3px 1px #3b82f6;
    }

    100% {
        box-shadow: none;
    }
}
</style>
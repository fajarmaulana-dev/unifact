<script setup lang="ts">
import { computed, ref, watch } from 'vue';
import { usePredict } from './__index';
import NotFound from '@/components/tools/NotFound.vue';
import IcoText from '@/components/tools/IcoText.vue';
import Alert from '@/components/tools/Alert.vue';
import cnn from '@/assets/cnn.webp';
import detik from '@/assets/detik.webp';
import kominfo from '@/assets/kominfo.webp';
import kompas from '@/assets/kompas.webp';
import liputan from '@/assets/liputan6.webp';
import mafindo from '@/assets/mafindo.webp';
import medcom from '@/assets/medcom.webp';
import tempo from '@/assets/tempo.webp';
const open = ref(false);
const bulb = ref(false)
const { loading, predict, prediction } = usePredict();

const textModel = ref('')
const enter = () => {
    if (textModel.value !== '') {
        predict({ text: textModel.value });
    }
}

const normal = ref('')
watch(prediction, () => {
    if (prediction) normal.value = prediction.value?.normalNaration
})

watch(normal, () => {
    if (normal.value !== '') open.value = true
})

const color = computed(() => {
    if (prediction.value?.prediction?.split(' ')[0] === 'Misleading') return 'text-amber-700 dark:text-amber-300';
    if (prediction.value?.prediction?.split(' ')[0] === 'Fabricated') return 'text-rose-700 dark:text-rose-300';
    if (prediction.value?.prediction?.split(' ')[0] === 'Valid') return 'text-emerald-700 dark:text-emerald-300'
})

const assign = (url: string) => location.assign(url);

const sosmed = [
    { class: 'fa-github', title: 'fajarmaulana-dev', act: 'https://github.com/fajarmaulana-dev' },
    { class: 'fa-linkedin', title: 'Fajar Maulana', act: 'https://www.linkedin.com/in/fajar-maulana-16b98b152' },
    { class: 'fa-facebook', title: 'Fajar Maulana', act: 'https://www.facebook.com/people/Fajar-Maulana/100010712022613' },
]

const news = [
    { img: mafindo, title: 'turnbackhoax', act: 'http://turnbackhoax.id/' },
    { img: kominfo, title: 'kominfo', act: 'https://www.kominfo.go.id/content/all/laporan_isu_hoaks' },
    { img: medcom, title: 'medcom', act: 'https://www.medcom.id/cekfakta/' },
    { img: kompas, title: 'kompas', act: 'https://www.kompas.com/cekfakta' },
    { img: liputan, title: 'liputan6', act: 'https://www.liputan6.com/cek-fakta' },
    { img: cnn, title: 'cnnindonesia', act: 'https://www.cnnindonesia.com/tag/cek-fakta' },
    { img: tempo, title: 'tempo', act: 'https://cekfakta.tempo.co/' },
    { img: detik, title: 'detik', act: 'https://hoaxornot.detik.com/' }
]
</script>

<template>
    <NotFound message="" code="" class="overflow-hidden">
        <section class="absolute w-full h-full top-0">
            <div class="relative w-full h-full flex flex-col items-center justify-center p-[calc(.75rem+5vw)]">
                <div @click="bulb = true"
                    class="group md:w-12 md:h-12 w-10 h-10 gr hidden place-items-center cursor-pointer rounded-full dark:bg-amber-200 bg-sky-100 absolute md:top-[calc(20vh+7rem)] top-4 right-4 md:right-[calc(20vw-2rem)] shadow-[inset_0_0_15px_3px] dark:shadow-amber-400 shadow-blue-600">
                    <i style="transition: .2s"
                        class="fa-solid fa-lightbulb text-xl group-hover:text-2xl group-active:text-xl dark:text-amber-700 text-blue-600"></i>
                </div>
                <div class="absolute top-4 left-4 w-fit h-fit">
                    <div
                        class="bl hidden items-center justify-center gap-3 [&>i]:text-2xl [&>i]:cursor-pointer [&>i]:w-10 [&>i]:h-10 [&>i]:dark:bg-white [&>i]:dark:text-blue-400 [&>i]:bg-sky-700 [&>i]:text-sky-100 hover:[&>i]:text-white hover:[&>i]:dark:text-blue-600 active:[&>i]:text-sky-100 active:[&>i]:dark:text-blue-400 [&>i]:rounded-full [&>i]:grid [&>i]:place-items-center [&>i]:transition [&>i]:duration-500">
                        <i v-for="media, index in sosmed" :key="index" :class="`fa-brands ${media.class}`"
                            :title="media.title" @click="assign(media.act)"></i>
                    </div>
                </div>
                <div
                    class="px-4 absolute bottom-4 lg:bottom-[10%] w-full h-fit flex lg:flex-row flex-col items-center justify-center lg:justify-around gap-3 [&>div]:flex-col [&>div]:items-center [&>div]:justify-center [&>div]:gap-1 [&>div>p]:font-bold [&>div>p]:text-sky-700 [&>div>p]:dark:text-white">
                    <div class="inf hidden">
                        <p style="font-size: var(--larger-icon) !important;">Situs cek fakta pilihan</p>
                        <div
                            class="flex flex-wrap items-center justify-center gap-3 [&>div]:text-2xl [&>div]:cursor-pointer [&>div]:w-10 [&>div]:h-10 [&>div]:bg-white [&>div]:border-2 [&>div]:border-solid [&>div]:border-blue-400 hover:[&>div]:border-blue-700 hover:[&>div]:dark:border-white active:[&>div]:border-blue-400 [&>div]:rounded-md [&>div]:grid [&>div]:place-items-center [&>div]:transition [&>div]:duration-500 [&>div]:p-1">
                            <div v-for="media, index in news" :key="index" :title="media.title"
                                @click="assign(media.act)">
                                <img :src="media.img" :alt="media.title">
                            </div>
                        </div>
                    </div>
                    <div class="fin hidden">
                        <p style="font-size: var(--larger-icon) !important;">Sudah coba aplikasinya ?</p>
                        <div class="text-center">
                            <div style="font-size: var(--logo) !important; cursor: pointer !important;"
                                @click="assign('https://forms.gle/TFs7Dy5Raf7m2Gjk8')"
                                class="flex items-center justify-center gap-3 dark:bg-white dark:text-blue-400 bg-sky-700 text-sky-100 hover:text-white hover:dark:text-blue-600 active:text-sky-100 active:dark:text-blue-400 rounded-md transition duration-500 h-10 sm:w-[calc(14rem+20vw)] w-[calc(14rem+14vw)] max-w-[25rem] font-bold">
                                <i class="fa-solid fa-paper-plane"></i>
                                <span>Bagikan pendapatmu tentang UniFACT</span>
                            </div>
                        </div>
                    </div>
                </div>
                <h1 style="font-size: var(--big-title) !important;"
                    class="text-sky-500 dark:text-sky-200 font-black leading-[calc(1.25rem+1.25vw)]">
                    Uni<span class="text-amber-500 dark:text-amber-200">FACT</span>
                </h1>
                <h4 style="font-size: var(--small-title) !important;"
                    class="w-full text-center mb-[calc(1rem+1vw)] text-sky-500 dark:text-sky-200 font-bold">
                    deep learning based app
                    <span class="text-amber-500 dark:text-amber-200">
                        for Indonesian hoax classification</span>
                </h4>
                <IcoText is="search" v-model="textModel" :loading="loading" prepend-cursor="cursor-pointer"
                    @on-prepend="enter()" @on-enter="enter()" @after-recognize="enter()" />
            </div>
        </section>
        <section style="transition: .5s; z-index: 51;" :class="bulb ? 'translate-y-0' : 'translate-y-[100%]'"
            class="absolute cont p-[calc(1.25rem+1.25vw)] pr-[calc(.25rem+.25vw)] bg-sky-100 dark:bg-slate-800 w-full h-[60%] bottom-0 rounded-t-2xl">
            <div class="relative w-full h-full">
                <span class="absolute w-full h-8 -top-[calc(1.25rem+1.25vw)] flex justify-center items-start">
                    <span @click="bulb = false"
                        class="group h-5 w-12 rounded-b-full bg-sky-600 dark:bg-sky-300 text-slate-50 dark:text-slate-800 grid place-items-center cursor-pointer">
                        <i style="transition: .25s"
                            class="fa-solid fa-angle-down -translate-y-[.1rem] group-hover:translate-y-[.05rem]"></i>
                    </span>
                </span>
                <div class="w-full h-full pr-[calc(1.25rem+1.25vw)] overflow-y-auto [&>div]:flex">
                    <h2 class="w-full text-center font-bold mb-6">Tahukah Kamu ?</h2>
                    <p class="mb-3">Berdasarkan analisis dari <a
                            href="https://firstdraftnews.org/articles/fake-news-complicated/"
                            class="underline font-bold">FirstDraft (2017)</a>,
                        sebuah koalisi non profit internasional pada bidang etika jurnalistik, misinformasi dan
                        disinformasi memiliki sebanyak tujuh klasifikasi yaitu:</p>
                    <div>
                        <strong class="min-w-[1.5rem]">1.</strong>
                        <p><strong>Satire atau Parody</strong>, yaitu konten tidak memiliki niat untuk merugikan, akan
                            tetapi konten tersebut memiliki potensi untuk mengelabuhi</p>
                    </div>
                    <div>
                        <strong class="min-w-[1.5rem]">2.</strong>
                        <p><strong>Misleading Content</strong>, yaitu digunakannya informasi yang menyesatkan pada suatu
                            konten untuk membingkai sebuah isu atau individu tertentu.</p>
                    </div>
                    <div>
                        <strong class="min-w-[1.5rem]">3.</strong>
                        <p><strong>Imposter Content</strong>, yaitu konten palsu yang dibuat dengan meniru sumber
                            aslinya.</p>
                    </div>
                    <div>
                        <strong class="min-w-[1.5rem]">4.</strong>
                        <p><strong>Fabricated Content</strong>, yaitu konten yang 100% salah dan dibuat untuk merugikan
                            serta menipu pengaksesnya.</p>
                    </div>
                    <div>
                        <strong class="min-w-[1.5rem]">5.</strong>
                        <p><strong>False Connection</strong>, yaitu ketika judul, gambar, atau keterangannya tidak
                            mendukung konten yang dipublikasikan.</p>
                    </div>
                    <div>
                        <strong class="min-w-[1.5rem]">6.</strong>
                        <p><strong>False Context</strong>, yaitu ketika konten yang asli dipadankan dengan konteks
                            informasi yang salah.</p>
                    </div>
                    <div>
                        <strong class="min-w-[1.5rem]">7.</strong>
                        <p><strong>Manipulated Content</strong>, yaitu ketika informasi atau gambar yang asli
                            dimanipulasi oleh penipu untuk mengelabuhi.</p>
                    </div>
                    <p class="my-3">Masalah klasifikasi ini dapat diselesaikan secara otomatis menggunakan model Deep
                        Learning. Secara singkat, model Deep Learning terutama untuk masalah klasifikasi teks dapat
                        dikatakan sebagai persamaan kurva yang dapat mengelompokkan data masukan ke dalam kelompok kelas
                        tertentu berdasarkan hasil pemberian makna linguistik terhadap setiap kata pada dataset.</p>
                    <p>Untuk itu, sebagai syarat penyelesaian skripsi, pengembang mencoba membangun aplikasi dengan
                        model Deep Learning berarsitektur <strong>Bidirectional Temporal Convolutional Neural
                            Network</strong> yang mana berdasarkan uji coba, dapat menghasilkan model yang lebih baik
                        dari arsitektur lainnya seperti CNN, LSTM, dan GRU. Model yang terpasang pada aplikasi ini dapat
                        mengklasifikasikan narasi ke dalam tiga klasifikasi, yaitu Valid, Misleading Content/False
                        Context/Manipulated Content, dan Fabricated Content/Imposter Content. Model belum dapat
                        mengklasifikasikan secara lengkap dikarenakan masih kurangnya data pada beberapa kelas.
                        Sedangkan penggabungan beberapa kelas dilakukan berdasarkan adanya kemiripan dari kelas yang
                        digabung.</p>
                </div>

            </div>
        </section>
        <section style="transition: .5s;  z-index: 51;" :class="open ? 'translate-y-0' : 'translate-y-[100%]'"
            class="absolute cont bg-sky-100 dark:bg-slate-800 w-full h-[80%] bottom-0 rounded-t-2xl">
            <div class="relative w-full h-full">
                <span class="absolute w-full h-8 -top-8 flex justify-center items-start">
                    <span @click="textModel = ''; open = false; normal = ''"
                        class="group h-5 w-12 rounded-b-full bg-sky-600 dark:bg-sky-300 text-slate-50 dark:text-slate-800 grid place-items-center cursor-pointer">
                        <i style="transition: .25s"
                            class="fa-solid fa-angle-down -translate-y-[.1rem] group-hover:translate-y-[.05rem]"></i>
                    </span>
                </span>
                <div v-if="prediction?.withoutStopword === ''"
                    class="h-full grid place-items-center w-full p-[calc(.5rem+2.5vw)] pt-0 mt-8 !pb-12">
                    <div
                        class="flex flex-col items-center gap-3 font-bold [&>*]:text-center [&>*]:text-amber-700 [&>*]:dark:text-amber-300 p-[calc(2rem+2vw)]">
                        <i class="fa-solid fa-triangle-exclamation text-[5rem] mb-[2vw]"></i>
                        <p>Oopss... Narasi yang kamu masukkan hanya memuat stopword (kata yang tidak begitu penting
                            untuk diprediksi), sehingga prediksi tidak dapat dilakukan.<br />
                            Silakan coba lagi dengan narasi yang berbeda.</p>
                        <em style="transition: .5s"
                            @click="assign('https://drive.google.com/file/d/1dNRiXb9fy3fzeypcYukzeexk7M8RNNLB/view?usp=sharing')"
                            class="hover:!text-amber-500 active:!text-amber-700 active:dark:!text-amber-300 cursor-pointer">
                            Lihat daftar stopword >></em>
                    </div>
                </div>
                <div v-else class="w-full h-full overflow-y-auto p-[calc(.5rem+2.5vw)] pt-0 mt-8 !pb-12">
                    <Alert class="mb-[calc(1rem+1.5vw)]" is="warning"
                        v-if="prediction?.existence?.false === 0 && prediction?.existence?.imposter === 0 && prediction?.existence?.valid === 0 || prediction?.withoutStopword?.split(' ').length < 4">
                        <strong class="mb-[calc(1rem+1vw)]">Perhatian!</strong><br />
                        <p>{{ prediction?.withoutStopword?.split(' ').length < 4
                                ? 'Narasi bersih (tanpa stopword) terlalu singkat'
                                : 'Corpus tidak memuat satupun kata pada narasi'
                        }}. Prediksi mungkin tidak akurat.</p>
                    </Alert>
                    <div
                        class="grid grid-cols-1 gap-[calc(1.5rem+2vw)] sm:grid-cols-2 [&>div]:w-full [&>div]:h-full [&>div>h2]:w-full [&>div>h2]:mb-2 [&>div>h2]:text-center [&>div>h2]:font-bold">
                        <div>
                            <h2>Narasi Asli</h2>
                            <p class="text-center">{{ textModel }}</p>
                        </div>
                        <div>
                            <h2>Narasi Normal</h2>
                            <p class="text-center">{{ prediction?.normalNaration }}</p>
                        </div>
                        <div class="flex flex-col items-center">
                            <h2>Rincian Probabilitas</h2>
                            <div>
                                <div v-for="(prob, index) in prediction?.probability" :key="index"
                                    :class="prob?.class.split(' ')[0] === 'Misleading' ? 'text-amber-700 dark:text-amber-300' : prob?.class.split(' ')[0] === 'Fabricated' ? 'text-rose-700 dark:text-rose-300' : 'text-emerald-700 dark:text-emerald-300'"
                                    class="flex mb-1 items-center [&>*]:font-bold">
                                    <h3 class="min-w-[calc(3.5rem+3.5vw)]">{{ prob.probs }}</h3>
                                    <h4>{{ prob.class }}</h4>
                                </div>
                            </div>
                        </div>
                        <div>
                            <h2>Prediksi Akhir</h2>
                            <div class="w-full flex justify-center items-center my-3">
                                <i :class="[prediction?.ico, color]" class="text-[4rem]"></i>
                            </div>
                            <p :class="color" class="text-center font-bold">{{
                                    prediction?.prediction
                            }}</p>
                        </div>
                    </div>
                    <div class="[&>h2]:mb-2 [&>h2]:text-center [&>h2]:font-bold mt-[calc(1.5rem+2vw)]">
                        <h2>Penjelasan</h2>
                        <p>Berdasarkan dominasi kata pada data train yang digunakan, diperoleh fakta bahwa frekuensi
                            tiap kata dari narasi pada tiap kelas dataset adalah sebagai berikut :</p>
                        <h4 class="font-bold mt-4 mb-1 text-rose-700 dark:text-rose-300">
                            Fabricated Content/Imposter Content</h4>
                        <div
                            class="flex gap-2 flex-wrap [&>h5]:bg-rose-700 [&>h5]:dark:bg-rose-300 [&>h5]:text-sky-100 [&>h5]:dark:text-slate-800 [&>h5]:rounded-md [&>h5]:py-1 [&>h5]:px-3 [&>h5]:font-bold">
                            <h5 v-for="(record, index) in prediction?.record?.imposter" :key="index">
                                {{ record.word }}: {{ record.num }}x</h5>
                        </div>
                        <h4 class="font-bold mt-4 mb-1 text-amber-700 dark:text-amber-300">Misleading Content/False
                            Context/Manipulated Content</h4>
                        <div
                            class="flex gap-2 flex-wrap [&>h5]:bg-amber-700 [&>h5]:dark:bg-amber-300 [&>h5]:text-sky-100 [&>h5]:dark:text-slate-800 [&>h5]:rounded-md [&>h5]:py-1 [&>h5]:px-3 [&>h5]:font-bold">
                            <h5 v-for="(record, index) in prediction?.record?.false" :key="index">
                                {{ record.word }}: {{ record.num }}x</h5>
                        </div>
                        <h4 class="font-bold mt-4 mb-1 text-emerald-700 dark:text-emerald-300">Valid</h4>
                        <div
                            class="flex gap-2 flex-wrap [&>h5]:bg-emerald-700 [&>h5]:dark:bg-emerald-300 [&>h5]:text-sky-100 [&>h5]:dark:text-slate-800 [&>h5]:rounded-md [&>h5]:py-1 [&>h5]:px-3 [&>h5]:font-bold">
                            <h5 v-for="(record, index) in prediction?.record?.valid" :key="index">
                                {{ record.word }}: {{ record.num }}x</h5>
                        </div>
                        <div class="[&>h4]:mb-2">
                            <h4 class="mt-4">Dari data di atas, dominasi kata pada kelas <span
                                    class="text-rose-700 dark:text-rose-300 font-bold">Fabricated Content/Imposter
                                    Content</span> adalah sebanyak <span
                                    class="text-rose-700 dark:text-rose-300 font-bold">
                                    {{ prediction?.domination?.imposter }} kali</span>, pada kelas <span
                                    class="text-amber-700 dark:text-amber-300 font-bold">
                                    Misleading Content/False Context/Manipulated Content</span> adalah <span
                                    class="text-amber-700 dark:text-amber-300 font-bold">
                                    {{ prediction?.domination?.false }} kali</span>, dan pada kelas
                                <span class="text-emerald-700 dark:text-emerald-300 font-bold">Valid</span> adalah <span
                                    class="text-emerald-700 dark:text-emerald-300 font-bold">
                                    {{ prediction?.domination?.valid }} kali</span>.
                            </h4>
                            <h4>Sedangkan berdasarkan eksistensi katanya, sebanyak <span
                                    class="text-rose-700 dark:text-rose-300 font-bold">
                                    {{ prediction?.existence?.imposter }} kata </span>
                                pada narasi ada pada corpus kelas <span
                                    class="text-rose-700 dark:text-rose-300 font-bold">
                                    Fabricated Content/Imposter Content</span>, <span
                                    class="text-amber-700 dark:text-amber-300 font-bold">
                                    {{ prediction?.existence?.false }} kata </span>ada pada corpus kelas <span
                                    class="text-amber-700 dark:text-amber-300 font-bold">
                                    Misleading Content/False Context/Manipulated Content</span>, dan <span
                                    class="text-emerald-700 dark:text-emerald-300 font-bold">
                                    {{ prediction?.existence?.valid }} kata </span>ada pada corpus kelas <span
                                    class="text-emerald-700 dark:text-emerald-300 font-bold">Valid</span>.
                            </h4>
                            <h4>Mempertimbangkan banyaknya dominasi kata, eksistensi kata, dan urutan
                                bobot nilai linguistik yang diberikan oleh jaringan saraf, model
                                memprediksi bahwa narasi tersebut masuk pada kelas
                                <span class="font-bold" :class="color"> {{ prediction?.prediction }}</span>.
                            </h4>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </NotFound>
</template>

<style scoped>
.cont h2 {
    font-size: var(--largest-icon) !important;
}

.cont h3 {
    font-size: var(--larger-icon) !important;
}

.cont p,
.cont li,
.cont strong,
.cont em {
    font-size: var(--icon) !important;
}

.cont h4 {
    font-size: var(--smaller-icon) !important;
}

.cont h5 {
    font-size: var(--smallest-icon) !important;
}

@media all and (min-height: 540px) {
    .inf {
        display: flex;
    }
}

@media all and (min-height: 360px) {
    .fin {
        display: flex;
    }
}

@media all and (min-height: 280px) {
    .gr {
        display: grid;
    }

    .bl {
        display: flex;
    }
}
</style>
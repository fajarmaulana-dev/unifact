import {createApp} from '@vue/runtime-dom';
import App from './App.vue';
import router from './router';
import store from './global';
import './style.css';
import '@fontsource/be-vietnam-pro/100.css';
import '@fontsource/be-vietnam-pro/200.css';
import '@fontsource/be-vietnam-pro/300.css';
import '@fontsource/be-vietnam-pro/300.css';
import '@fontsource/be-vietnam-pro/500.css';
import '@fontsource/be-vietnam-pro/600.css';
import '@fontsource/be-vietnam-pro/700.css';
import '@fontsource/be-vietnam-pro/800.css';
import '@fontsource/be-vietnam-pro/900.css';
import {useRegisterSW} from 'virtual:pwa-register/vue';
useRegisterSW({immediate: true});

const app = createApp(App);

app.use(router);
app.use(store);

app.mount('#app');

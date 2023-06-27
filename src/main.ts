import {createApp} from '@vue/runtime-dom';
import App from './App.vue';
import router from './router';
import store from './global';
import './style.css';
import './awesome.css';
import '@fontsource/be-vietnam-pro';

const app = createApp(App);

app.use(router);
app.use(store);

app.mount('#app');

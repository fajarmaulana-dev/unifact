import {createStore} from 'vuex';
import Local from '@/api/local';

const store = createStore({
  state() {
    return {
      isDark: !Local.getLocalData('theme')
        ? true
        : Local.getLocalData('theme') === true
        ? true
        : false,
    };
  },
  mutations: {
    toggleTheme(state: any) {
      Local.setLocalData('theme', !state.isDark);
      state.isDark = !state.isDark;
    },
  },
  actions: {},
  getters: {},
});

export default store;

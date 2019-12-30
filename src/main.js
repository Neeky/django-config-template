import Vue from 'vue';
import App from './App.vue';

let app = document.getElementById('app');
let vm = new Vue({
    render: (h) => h(App)
}).$mount(app);
import { createApp } from 'vue'
import { createPinia } from "pinia";

import App from './App.vue'
import router from "./router";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";

createApp(App).use(router).use(createPinia()).mount("#app");
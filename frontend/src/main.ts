import { createApp, defineAsyncComponent } from 'vue'
import { createPinia } from "pinia";
import router from "./router";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";

const App = defineAsyncComponent(() => import("./App.vue"));

createApp(App).use(router).use(createPinia()).mount("#app");
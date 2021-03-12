import "bootstrap/dist/css/bootstrap.min.css";
import $ from "jquery";
import Popper from "popper.js";
import "bootstrap/dist/js/bootstrap.bundle.min";
import Vue from "vue";
import App from "./App.vue";

new Vue({
    el: "#app",
    components: {
        App,
    },
}).mount("#app");

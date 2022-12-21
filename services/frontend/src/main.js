import { createApp } from 'vue'
import App from './App.vue'

import axios from 'axios';

import './assets/styles/loader.css';

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/';  // the FastAPI backend

createApp(App).mount('#app')

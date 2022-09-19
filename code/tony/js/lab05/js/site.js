const App = new Vue({
    el: '#app',
    data: {
        message: 'Hello, world!',
    },
})

const app = Vue.createApp(App)
app.mount('#app')
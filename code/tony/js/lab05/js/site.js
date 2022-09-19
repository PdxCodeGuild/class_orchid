const App = {
    el: '#app',
    data: () => {
        return { message: 'Hello, world!' }
    },
}

const app = Vue.createApp(App)
app.mount('#app')
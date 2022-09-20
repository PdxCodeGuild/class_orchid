
console.log('hello')
const App = ({
    el: '#app',
    data: ()=> {
        return{
            todo:'',
            
        }
    }
})

const app = Vue.createApp(App)
app.mount('#app')
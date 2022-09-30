const App = {
    el: '#app',
    data: () => {
        return {
            keyword:'',
            quotes:'',
        }
    },

    mounted () {
        axios
            .get('https://favqs.com/api/quotes',{headers:{'Authorization':'Token token="855df50978dc9afd6bf86579913c9f8b"'}})
            .then(response => {
                console.log(response)
                this.quotes = response.data.quotes})
            
    }
    // methods: {
    //     getQuotes() {
    //         axios.get('https://favqs.com/api/', {params:{filter:''}})
            
//         }

//     }

// }
}


const app = Vue.createApp(App)
app.mount('#app')
const App = {
    el: '#app',
    data: () => {
        return {
            input:'',
            quotes:[],
            data:1,
            tag:''
        }
    },

    mounted () {
        axios
            .get('https://favqs.com/api/quotes',{headers:{'Authorization':'Token token="855df50978dc9afd6bf86579913c9f8b"'}})
            .then(response => {
                console.log(response)
                this.quotes = response.data.quotes})
        
    },
methods:{  
    keyWord() {
        console.log(this.input)
        axios
        .get('https://favqs.com/api/quotes',{headers:{'Authorization':'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params:{'filter':this.input, 'page':this.data, 'type':this.tag}})
        .then(response => {
            console.log(response)
            this.quotes = response.data.quotes})
    },
    nextPage() {
        this.data += 1
        axios
        .get('https://favqs.com/api/quotes',{headers:{'Authorization':'Token token="855df50978dc9afd6bf86579913c9f8b"'}, 
        params:{'filter':this.input, 'page':this.data}})
        .then(response => {
            console.log(response)
            this.quotes = response.data.quotes})
    },
    prevPage() {
        this.data -= 1
        axios
        .get('https://favqs.com/api/quotes',{headers:{'Authorization':'Token token="855df50978dc9afd6bf86579913c9f8b"'}, 
        params:{'filter':this.input, 'page':this.data}})
        .then(response => {
            console.log(response)
            this.quotes = response.data.quotes})
    },

    
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
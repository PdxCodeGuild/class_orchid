const App = {
    el: '#app',
    data:()=> {
        return {
            outputs: [],
            current_page: 1,
            filterInput: '',
            keywordInput: '',
            key: api()
        }
    },
    mounted() {
        axios({
            method: "GET",
            url: 'https://favqs.com/api/quotes/',
            headers: {
                "Authorization": 'Token token="' + this.key + '"' 
            }
        })
        .then(response => {
            console.log(response)
            for(let i = 0; i < response.data.quotes.length; i++){
                this.outputs.push(response.data.quotes[i])
            }
        })
    },
    methods: {
        getKeywords() {
            this.outputs = []
            this.current_page = 1
            this.getNewPage()
        },
        getNewPage() {
            this.outputs = []
            axios({
                method: "GET",
                url: 'https://favqs.com/api/quotes/',
                params: {
                    page: this.current_page,
                    type: this.filterInput,
                    filter: this.keywordInput,
                },
                headers: {
                    "Authorization": 'Token token="' + this.key + '"' 
                }
            })
            .then(response => {
                console.log(response)
                for(let i = 0; i < response.data.quotes.length; i++){
                    this.outputs.push(response.data.quotes[i])
                }
            })
        },
        pageDownBuilder() {
            this.current_page--
            this.getNewPage()
        },
        pageUpBuilder() {
            this.current_page++
            this.getNewPage()
        },
    }
}


const app = Vue.createApp(App)
app.mount('#app')
let key = api()
let count = 9

const App = {
    el: '#app',
    data:()=> {
        return {
            output: [],
            history: {},
            startSearch: '',
            endSearch: '',
        }
    },
    mounted() {
        axios.get(`https://api.nasa.gov/planetary/apod?api_key=${key}&count=${count}`)
            .then(response => {

                for(let i = 0; i < count; i++) {
                    if(i >= 0 || i <= response.data.length) {
                        this.output.push(response.data[i])
                    }
                }
            })  
            .catch(err => console.error(err))
    },

    methods: {
        getURL() {
            console.log(this.startSearch)
            console.log(this.endSearch)
            axios.get(`https://api.nasa.gov/planetary/apod?api_key=${key}&start_date=${this.startSearch}&end_date=${this.endSearch}`)
            .then(response => {
                // let temp = this.temp.push(response.data)
                this.output = []
                for(let i = 0; i < response.data.length; i++){
                    if(i >= 0 || i <= response.data.length){
                        this.output.push(response.data[i])
                    }
                }

                historyName = this.startSearch + ' => ' + this.endSearch

                this.history[historyName] = `https://api.nasa.gov/planetary/apod?api_key=${key}&start_date=${this.startSearch}&end_date=${this.endSearch}`

                // 2022-09012,2022-09-28


            })  
            .catch(err => console.error(err))
        },
        historyURL(historyCall) {
            axios.get(historyCall).then(response => {
                this.output = []
                for(let i = 0; i < response.data.length; i++){
                    if(i >= 0 || i <= response.data.length){
                        this.output.push(response.data[i])
                    }
                }
            }

            )
        }
    }
}

const app = Vue.createApp(App)
app.mount("#app")



const App = {

    el: '#app',
    data() {
        return {
            output: null,
            search: null,
            objectItems: [],
            page: 1

        }

    },


    mounted() {
        axios
            .get('https://favqs.com/api/quotes', {
                headers: { 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"' },
                params: {
                    'page': this.page,
                }

            })
            .then(response => {
                (this.objectItems = response.data.quotes)

            })


    },
    methods: {

        nextPage() {
            this.page++
            axios
                .get('https://favqs.com/api/quotes', {
                    headers: { 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"' },
                    params: {
                        'filter': this.search,
                        'page': this.page,
                    }
                })
                .then(response => {
                    (this.objectItems = response.data.quotes)

                })

        },

        prevPage() {
            this.page--
            axios
                .get('https://favqs.com/api/quotes', {
                    headers: { 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"' },
                    params: {
                        'filter': this.filter,
                        'page': this.page,


                    }
                })
                .then(response => {
                    (this.objectItems = response.data.quotes)

                })
        },



        getQotd() {

            console.log('GET Request');
            axios.get('https://favqs.com/api/qotd')
                .then(res => {
                    console.log(res)
                    this.output = res.data.quote.body
                    this.objectItems = null

                })
                .catch(err => console.error(err))

        },

        getQuote(search) {
            console.log(search)
            axios.get(`https://favqs.com/api/quotes/`,
                {
                    headers: { 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"' },
                    params: {
                        "filter": this.search,
                        "page": this.page,
                    }
                })

                .then(res => {
                    console.log(res)
                    this.objectItems = res.data.quotes;
                    this.output = null

                })
                .catch(err => console.error(err))
        },

        computed: {
            pageCount() {
                let l = this.objectItems.length,
                    s = this.size;
                return Math.ceil(l / s);
            },

            paginatedData() {
                const start = this.page * this.size,
                    end = start + this.size; return this.objectItems.slice(start, end);
            },

        },



    },
}


const app = Vue.createApp(App);
app.mount('#app');









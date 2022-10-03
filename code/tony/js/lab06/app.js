const App = {
    el: '#app',
    data() {
        return {
            data: { page: 0, quotes: [] }, search: { query: '' }
        }
    },
    async mounted() {
        this.data = await this.getQuotes()
        this.data.quotes = this.data.quotes.slice(0,5)
        console.log(this.data.quotes)
    },
    components: {
        quoteitem: {
            props: ['body','author'],
            template: `<div class="quote col-4 my-2"><div class="quotebody">{{body}}</div><div class="quoteauthor"><em>– {{author}}</em></div></div>`
        },
    },
    methods: {

        async getQuotes(pg=1) {
            opts = {headers:{'Authorization':'Token token="649e4ae55c1d9543452f9d0e72f4075d"'}}
            opts.params = {'page': this.data.page + pg}
            if (this.search.type != 'keyword') { opts.params.type = this.search.type }
            if (this.search.query) { opts.params.filter = this.search.query }
            console.table(this.data.page)
            const res = await axios
                .get('https://favqs.com/api/quotes', opts)
                .then(res => res)
                .catch(err => console.error(err))
            this.url = res.request.responseURL
            console.table(res.data.page)
            console.table(this.data.page)
            this.data = res.data
            return res.data
        },

        async doSearch(e) {
            this.data.page = 0
            this.search.type = e.path[0].id
            this.search.query = e.path[0].value
            e.path[0].value = ''
            this.data = await this.getQuotes()
        }

    },
    computed: {
        less() {
            return this.data.quotes.length && this.data.page > 1 && this.search.query != ''
        },
        more() {
            return this.data.quotes.length && !this.data.last_page && this.search.query != ''
        }
    }
}
const app = Vue.createApp(App)
app.mount('#app')
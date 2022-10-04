import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'
import AUTH_KEY  from '../hide.js'

createApp({
    data() {
        return {
          quotesList: [],
          qotd: '',
          search: '',
          prevSearch: '',
          key: '',
          data: {page: 1}
        }
      },
      components: {
        quote: {
            props: {
                body: '',
                author: '',
            },
            template: `<div class="quote"><div class="q_author">{{author}}</div><div class="q_body">{{body}}</div></div><br>`,
        }
      },
      methods: {
        async testAPI(){
            const params = {headers:{'Authorization':`Token token=${AUTH_KEY}`}}
            const res = await axios.get('https://favqs.com/api/qotd', params).then((res) => {
                console.log(res)
                this.qotd = res.data.quote.body
            }).catch(error => {
                console.log(error)
                return error
            })
        },
        async getRandomQuotes(){
            const params = {headers:{'Authorization':`Token token=${AUTH_KEY}`}}
            params.params = this.data
            const quotesFromApi = await axios.get('https://favqs.com/api/quotes/', params)
            .then((res) => {
                console.log(res)
                this.quotesList = res.data.quotes
            }).catch((error) => {
                console.log(error)
            })
        },
        async getSearchQuotes(){
            const params = {headers:{'Authorization':`Token token=${AUTH_KEY}`}}
            params.params = this.data
            console.log(this.key)
            if(this.key == 'key'){
                console.log('here key')
                const quotesFromApi = await axios.get(`https://favqs.com/api/quotes/?filter=${this.search}`, params)
                    .then((res) => {
                        console.log(res)
                        this.quotesList = res.data.quotes
                    }).catch((error) => {
                        console.log(error)
                    })
            }else{
                console.log('here else')
                const quotesFromApi = await axios.get(`https://favqs.com/api/quotes/?filter=${this.search}&type=${this.key}`, params)
                    .then((res) => {
                        console.log(res)
                        this.quotesList = res.data.quotes
                    }).catch((error) => {
                        console.log(error)
                    })
            }
            
            this.prevSearch = this.search
            this.search = ''
        },
        async getSearchAttrQuotes(){
            console.log(this.key)
        },
        async getNextPageSearch(page){
            const params = {headers:{'Authorization':`Token token=${AUTH_KEY}`}}
            if(this.data.page == 0){
                this.data.page += 1
            }
            if((this.data.page) >= 1){
                this.data.page += page
            }
            console.log(this.data.page, this.prevSearch)
            params.params = this.data
            const quotesFromApi = await axios.get(`https://favqs.com/api/quotes/?filter=${this.prevSearch}`, params)
            .then((res) => {
                console.log(res)
                this.quotesList = res.data.quotes
            }).catch((error) => {
                console.log(error)
            })
        },
      },
      computed: {

      },
      async mounted(){
        await this.testAPI()
        await this.getRandomQuotes()
      }
}).mount('#app')

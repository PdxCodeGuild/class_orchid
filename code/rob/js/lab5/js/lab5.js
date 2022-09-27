import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'
import {AUTH_KEY} from '../hide.js'

createApp({
    data() {
        return {
          message: 'Hello Vue!',
          apiTest: this.testAPI(),
          quotesList: [],
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
                console.log
                this.apiTest = res.data.quote.body
                this.quotesList = res.data.quotes
            }).catch(error => {
                console.log(error)
                return error
            })
        },
        async getQuotes(){
            const params = {headers:{'Authorization':`Token token=${AUTH_KEY}`}}
            params.params = this.data
            const quotesFromApi = await axios.get('https://favqs.com/api/quotes/', params)
            .then((res) => {
                console.log(res)
                this.quotesList = res.data.quotes
            }).catch((error) => {
                console.log(error)
            })
        }
      },
      computed: {
        
      },
      async mounted(){
        await this.getQuotes(1)
      }
}).mount('#app')

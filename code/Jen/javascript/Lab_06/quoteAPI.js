

const App = {

    el: '#app',
    data() {
        return {
            output: {},
            search: {},

        }

    },

    methods: {

        getQotd() {



            console.log('GET Request');
            axios.get('https://favqs.com/api/qotd')
                .then(res => {
                    console.log(res)
                    this.output = res.data.quote.body

                })
                .catch(err => console.error(err))

        },

        getQuote(search) {
            console.log(search)
            axios.get(`https://favqs.com/api/quotes/`,
                { headers: { "Authorization": "Token token = '855df50978dc9afd6bf86579913c9f8b'" }, params: { "filter": search } })

                .then(res => {
                    console.log(res)
                    this.output = res.data.quote.body;
                })
        }
        //  .catch(err => console.error(err))

    }


}


const app = Vue.createApp(App);
app.mount('#app');










/*

{

}

*/
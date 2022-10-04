const App = {
    el: '#app',
    data: () => {
        return { data : [] , searchKey : "", page : 1 , searchType : ""}
    },
    mounted () {
        axios
        .get('https://favqs.com/api/quotes/', {headers : {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}})
        .then(response => (this.data = response.data.quotes))
    },
    methods :{
        filter(s) {
            axios
        .get('https://favqs.com/api/quotes/', {headers : {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params : {"filter" : this.searchKey, "page" : this.page, "type": this.searchType}})
        .then(response => (this.data = response.data.quotes))
        },
        pagination() {
            this.page += 1
            axios
        .get('https://favqs.com/api/quotes/', {headers : {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params : {"filter" : this.searchKey, "page" : this.page }})
        .then(response => (this.data = response.data.quotes))
        },
        flip() {
            this.page -= 1
            axios
            .get('https://favqs.com/api/quotes/', {headers : {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params : {"filter" : this.searchKey, "page" : this.page }})
            .then(response => (this.data = response.data.quotes))
        }
    },
    
}

const app = Vue.createApp(App)
app.mount('#app')

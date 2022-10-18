new Vue({
    el: '#app',
    data: () => {
        return {
            page: 1,
            type: '',
            output: null,
            searchTerm: '',
        }
    },
    mounted (){
        axios
            .get('https://favqs.com/api/quotes', {
                headers: {'Authorization':'Token token="855df50978dc9afd6bf86579913c9f8b"'}, 
            })
            .then(response => { 
                (this.output = (this.output = response.data.quotes))
            })
            console.log(this.output)
    },
    methods: {
        search(e) {
            this.searchTerm = e.target.value
            axios
                .get('https://favqs.com/api/quotes', {
                    headers: {'Authorization':'Token token="855df50978dc9afd6bf86579913c9f8b"'}, 
                    // params for filtering 
                    params: {'filter': this.searchTerm,
                              'page': this.page,
                              'type': this.type
                }
                })
                .then(response => { 
                    (this.output = response.data.quotes)
                })
        },
        next(){
            this.page += 1
            axios
            .get('https://favqs.com/api/quotes', {
                headers: {'Authorization':'Token token="855df50978dc9afd6bf86579913c9f8b"'}, 
                params: {'filter': this.searchTerm,
                        'page': this.page,
            }
        })
            .then(response => { 
                (this.output = response.data.quotes)
        })
    },
}
})

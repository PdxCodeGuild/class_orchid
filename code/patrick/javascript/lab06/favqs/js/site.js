




new Vue({
    el: '#app',
    data: () => {
        return {
            info: null,
            searchItem: '',
            page: 1,
            type: '',

            
        }
    },
    methods: {
        userInput(e) {
            
            this.searchItem = e.target.value
            
            
            
            
            axios
                .get('https://favqs.com/api/quotes', {
                    headers: {'Authorization':'Token token="855df50978dc9afd6bf86579913c9f8b"'}, 
                    params: {'filter': this.searchItem,
                              'page': this.page,
                              'type': this.type
                }
                })
                .then(response => { 
                    (this.info = response.data.quotes)
                    
                    
                })
            
            console.log(this.info)
            console.log(this.page)
            console.log(this.type)
            
        },
        nextPage(){
            this.page += 1
            axios
            .get('https://favqs.com/api/quotes', {
                headers: {'Authorization':'Token token="855df50978dc9afd6bf86579913c9f8b"'}, 
                params: {'filter': this.searchItem,
                        'page': this.page,
            }
        })
            .then(response => { 
                (this.info = response.data.quotes)
            
            
        })
    },
        
    },
    mounted (){
        axios
            .get('https://favqs.com/api/quotes', {
                headers: {'Authorization':'Token token="855df50978dc9afd6bf86579913c9f8b"'}, 
                
            })
            .then(response => { 
                (this.info = (this.info = response.data.quotes))
                
            })
            
            
    },
    

})
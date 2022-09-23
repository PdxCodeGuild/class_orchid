new Vue({
    el: '#app',
    data: () => {
        return {
            info: null,
            searchItem: ''
        }
    },
    methods: {
        userInput(e) {
            console.log(e)
            this.searchItem = e.target.value
            
            console.log(this.searchItem)
            axios
                .get('https://favqs.com/api/quotes', {
                    headers: {'Authorization':'Token token="855df50978dc9afd6bf86579913c9f8b"'}, 
                    params: {'filter': this.searchItem}
                })
                .then(response => { 
                    (this.info = (this.info = response.data.quotes))
                    console.log(response.data)
                })
            
            console.log(this.info)

        }
    },
    mounted (){
        axios
            .get('https://favqs.com/api/quotes', {
                headers: {'Authorization':'Token token="855df50978dc9afd6bf86579913c9f8b"'}, 
                
            })
            .then(response => { 
                (this.info = (this.info = response.data.quotes))
                console.log(response.data)
            })
            
            console.log(this.info)
    },
    

})
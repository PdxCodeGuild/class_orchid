
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
                .get('https://api.edamam.com/api/recipes/v2', {
                
                headers: {
                    'accept' : 'application/json',
                },
                params: {
                    'type': 'public',
                    'app_key' : '60b438b2284a5c3d5ae7d03e81caac11',
                    'q': this.searchItem,
                    'app_id': '1cdc9597'
                        }
                    })
                    .then(response => { 
                        (this.info = (this.info = response.data.hits))
                        
                    })
                }},
            })

                            
                
            



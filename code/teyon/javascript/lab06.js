new Vue({

    el: '#app',
    data: () => {
        return{
            info: null,
            pages: 1,
            find: '',
            type: '',

        }
        
    },
    methods: {
        typedInput(input) {
            this.find = input.target.value

        axios
        .get('http://favqs.com/api/quotes', {
            headers: {'Authorization': 'Token token="b739c98330b6c5c4d8d49a60dd6543e4"'},
            params: {'filter': this.find, 'pages': this.pages, 'type': this.type}
        })
        .then(response => {
            (this.info = response.data.quotes)
        })
        console.log(this.info)
        console.log(this.page)
        console.log(this.type)
    },
    next(){
        this.pages += 1
        axios
        .get('https://favqs.com/api/quotes', {
            headers: {'Authorization': 'Token token="b739c98330b6c5c4d8d49a60dd6543e4"'},
            params: {'filter': this.find, 'pages': this.pages}
        })
        .then(response => {
            (this.info = response.data.quotes)
        })
    }

    },

    mounted (){

        axios
            .get('http//favqs.com/api/quotes', {
                headers:{'Authorization': 'Token token="b739c98330b6c5c4d8d49a60dd6543e4"'}
            })
            .then(response => {
                (this.info = (this.info = response.data.quotes))
        })
    }
})
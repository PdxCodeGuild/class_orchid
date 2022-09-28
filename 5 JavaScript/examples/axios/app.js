// https://jsonplaceholder.typicode.com/

const App = {
    el: '#app',
    data() {
        return {
            output: {}
        }
    },
    mounted() {
        console.log('this happens when the page mounts');
        this.getUsers()
    },
    methods: {
        getUsers() {
            // GET REQUEST
            console.log('GET Request');
            // axios({
            //     method: 'get',
            //     url: 'https://jsonplaceholder.typicode.com/users',
            //     params: {
            //         id: 4
            //     }
            // })
            axios.get('https://jsonplaceholder.typicode.com/users', { params: { id: 3 } })
                .then(res => this.output = res)
                .catch(err => console.error(err))
        },
        addUser() {
            // POST REQUEST
            console.log('POST Request');
            axios.post('https://jsonplaceholder.typicode.com/users', {
                name: 'Fake Person',
                email: 'fake@person'
            })
                .then(res => this.output = res)
                .catch(err => console.error(err))

        },
        updateUser() {
            // PUT/PATCH REQUEST
            // PUT replaced the entire record
            // PATCH only changes the specified keys on the record
            axios.put('https://jsonplaceholder.typicode.com/users/3', {
                name: 'Fake Person',
                email: 'fake@person'
            })
                .then(res => this.output = res)
                .catch(err => console.error(err))
        },
        removeUser() {
            // DELETE REQUEST
            console.log('DELETE Request');
            axios.delete('https://jsonplaceholder.typicode.com/users/3')
                .then(res => this.output = res)
                .catch(err => console.error(err))
        }
    }
}
const app = Vue.createApp(App)
app.mount('#app')
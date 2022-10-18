const App = {
    el: '#app',
    data:()=> {
        return {
            items: {},
            todoName: '',
            counter: 0
        }
    },
    methods: {
        addItem() {
            let addNew = {
                id: this.counter,
                name: this.todoName,
                isComplete: false,
            }
            this.items[this.counter] = addNew
            this.counter++
        },
        remItem(event, passed) {
            console.log(passed)

            delete this.items[passed.id]
        },
        toggle: function(event, passed) {
            this.items[passed.id].isComplete = !passed.isComplete
        }
    }
}
const app = Vue.createApp(App)
app.mount("#app")
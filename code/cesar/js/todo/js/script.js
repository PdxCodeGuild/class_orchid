const App = {
    el: '#app',
    data: () => {
        return {
            incompleteTodo: [],
            completeTodo: [],
            inputField: "",
        }
    },
    methods: {
        add(e) {
            this.incompleteTodo.push(e.target.value)
        },
        remove: function (i) {
            this.incompleteTodo.splice(this.incompleteTodo.indexOf(i), 1)
        },
        done: function (i) {
            this.completeTodo.push(i)
            this.incompleteTodo.splice(this.incompleteTodo.indexOf(i), 1)
        },
        undo: function (i) {
            this.incompleteTodo.push(i)
            this.completeTodo.splice(this.completeTodo.indexOf(i), 1)
        },
        removeForever: function (i) {
            this.completeTodo.splice(this.completeTodo.indexOf(i), 1)
        }
    }
}

const app = Vue.createApp(App)
app.mount('#app')
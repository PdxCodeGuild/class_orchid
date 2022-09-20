const App = {
    el: '#app',
    data: () => {
        return { todos: [] }
    },
    methods: {
        addTodo(e) {
            this.todos.push({task:e.target.value,complete:false})
            localStorage.todos = JSON.stringify(this.todos)
        },
        completeTodo(index) {
            this.todos[index].complete = this.todos[index].complete ? false : true
            localStorage.todos = JSON.stringify(this.todos)
        },
        deleteTodo(index) {
            this.todos.splice(index, 1)
            localStorage.todos = JSON.stringify(this.todos)
        },
    },
    mounted() {
        if (localStorage.todos) {
            this.todos = JSON.parse(localStorage.todos)
        }
    },
}

const app = Vue.createApp(App)
app.mount('#app')
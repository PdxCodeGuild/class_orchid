const App = {
    el: '#app',
    data: () => {
        return { todos: [
            { task: 'Example one', complete: false, },
            { task: 'Example two', complete: false, },
            { task: 'Example three', complete: true, },
            { task: 'Example four', complete: false, },
            { task: 'Example five', complete: true, },
            { task: 'Example six', complete: false, },
            { task: 'Example seven', complete: false, },
        ] }
    },
    methods: {
        addTodo(e) {
            this.todos.push({
                task: e.target.value,
                complete:false,
            })
            localStorage.todos = JSON.stringify(this.todos)
        },
        completeTodo(index) {
            this.todos[index].complete = !this.todos[index].complete
            localStorage.todos = JSON.stringify(this.todos)
        },
        deleteTodo(index) {
            this.todos.splice(index, 1)
            localStorage.todos = JSON.stringify(this.todos)
        },
        clearTodos() {
            localStorage.clear()
            this.todos = []
        },
    },
    mounted() {
        if (localStorage.todos) {
            this.todos = JSON.parse(localStorage.todos)
        }
    },
    updated() {
            this.todos.sort((a,b) => a.complete < b.complete ? -1 : 1 )
    },
    computed: {}
}

const app = Vue.createApp(App)
app.mount('#app')
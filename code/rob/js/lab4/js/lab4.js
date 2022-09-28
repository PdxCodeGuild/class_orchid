const App = {
    el: '#app',
    data: () => {
        return{
            start_id: 0,
            newTodo: "",
            todos: [],
            removedTodos: [],
        }
    },
    methods: {
        addTodo(){
            let todo = {id: this.start_id += 1, todo: this.newTodo, completed: false,}
            this.todos.push(todo)
        },
        deleteTodo(id){
            let todoToDelete = {}
            let todo_index 
            this.todos.forEach((e, index) => {
                if(e.id == id){
                    todoToDelete = e
                    todo_index = index
                }
            });
            this.todos.splice(todo_index, 1)
        },
        completedTodo(id){
            let removedTodo
            let todoIndex
            this.todos.forEach((e, index) => {
                if(e.id == id){
                    todoIndex = index
                }
            })
            removedTodo = this.todos.splice(todoIndex, 1)
            this.removedTodos.push(removedTodo[0])
        },
        deleteCompletedTodo(id){
            let removedTodo
            let todoIndex
            this.removedTodos.forEach((e, index) => {
                if(e.id == id){
                    todoIndex = index
                }
            })
            this.removedTodos.splice(todoIndex, 1)
        },
        undoCompletedTodo(id){
            let undoTodo
            let todoIndex
            this.removedTodos.forEach((e, index) => {
                if(e.id == id){
                    todoIndex = index
                }
            })
            undoTodo = this.removedTodos.splice(todoIndex, 1)
            this.todos.push(undoTodo[0])
        }
    },
    computed:{
        sortedTodos(){
            return this.todos.sort((a, b) => a.id - b.id)
        }
    }
}

const app = Vue.createApp(App)
app.mount('#app')
const App = ({
    el: '#app',
    data: ()=> {
        return{
            todo: [],
            complete: [],
        }
    },
    methods: {
        addTodo: function () {
            this.todo.push(this.todo.item)
            this.todo.item = ''
        },
        deleteTodo: function (item) {
            this.todo.splice(this.todo.indexOf(item),1)
            // this.complete.splice(this.todo.indexOf(item),1)
        },
        completeTodo: function(item) {
            this.complete.push(item)
            this.todo.splice(this.todo.indexOf(item),1)
        },
        undoTodo: function(item) {
            this.todo.push(item)
            this.complete.splice(this.complete.indexOf(item),1)

        },
        deleteComplete: function (item) {
            this.complete.splice(this.complete.indexOf(item),1)
        }
        }
})

const app = Vue.createApp(App)
app.mount('#app')
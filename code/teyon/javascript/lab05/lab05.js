const App = ({
    el: '#app',
    data: ()=> {
        return{
            completed: [],
            todoList: [],
        }
    },
    methods: {
        addTask: function() {
            this.todoList.push(this.todoList.task)
            this.todoList.task = ''
        },
        undoTask: function(task) {
            this.todoList.push(task)
            this.completed.splice(this.completed.indexOf(task),1)
        },
        completedTask: function(task) {
            this.completed.push(task)
            this.todoList.splice(this.todoList.indexOf(task),1)
        },
        deleteTask: function(task) {
            this.todoList.splice(this.todoList.indexOf(task),1)

        }
    }
})
const app = Vue.createApp(App)
app.mount("#app")
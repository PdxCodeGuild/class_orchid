const App = {
    el: '#app',
    data: () => {
        return { toDo : [], inputField : "", completed : []}
    },
    methods: {
        addTodo(e) {
            this.toDo.push(e.target.value)
        },
        removeItem(t) {
            this.toDo.splice(this.toDo.indexOf(t), 1)
        },
        completedItem(i) {
            this.completed.push(i)
            this.toDo.splice(this.toDo.indexOf(i), 1)
        },
        undoTodo(a) {
            this.toDo.push(a)
            this.completed.splice(this.completed.indexOf(a), 1)
        },
        deleteItem(m){
            this.completed.splice(this.completed.indexOf(m), 1)
        }
    }
}

const app = Vue.createApp(App)
app.mount('#app')
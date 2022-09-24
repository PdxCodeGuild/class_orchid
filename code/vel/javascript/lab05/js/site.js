

const App = {
    el: '#app',
    data: () => {
        return { 
            incomplete : [], 
            inputField : "" , 
            complete : []
        }
    },
    methods: {
        userInput(e) {
            this.incomplete.push(e.target.value)
        },
        deleted: function(i) {
            this.incomplete.splice(this.incomplete.indexOf(i), 1)
        },
        completed: function(i) {
            this.complete.push(i)
            this.incomplete.splice(this.incomplete.indexOf(i), 1)
        },
        undo: function(i){
            this.incomplete.push(i)
            this.complete.splice(this.complete.indexOf(i), 1)
        },
        remove: function(i){
            this.complete.splice(this.complete.indexOf(i), 1)
        }
    }
}

const app = Vue.createApp(App)
app.mount('#app')

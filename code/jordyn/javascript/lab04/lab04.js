const App = {
    el: '#app',
    data:()=> {
        return {
            items: {},
            todoName: '',
            counter: 0
        }
    },
    // mounted() {
    //     let addNew = {
    //         id: this.id,
    //         name: 'test',
    //         isComplete: true,
    //     }
    //     this.items[this.id] = addNew
    //     this.id++
    // },
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
            // for(var i = 0; i < this.items.length; i++){
            //     if(this.items[i].id === passed.id){
            //     }
            // }
            delete this.items[passed.id]
        },
        toggle: function(event, passed) {
            this.items[passed.id].isComplete = !passed.isComplete
        }
    }
}

const app = Vue.createApp(App)
app.mount("#app")
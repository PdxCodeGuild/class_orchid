
const App = {

    el: '#app',
    data: () => {
        return {
            todos: [],
            done: [],
            grocery_item: ''
        }

    },

    methods: {

        addListitems() {
            console.log("addlistitems")
            this.todos.push(grocery_item.value)



        },

        removecompleteListitems(i) {
            console.log("removeitem")
            this.done.splice(this.done.indexOf(i), 1)


            /*reference this from the remove button. Delete item */

        },

        removenotcompleteListitems(i) {
            console.log("removeitem")
            this.todos.splice(this.todos.indexOf(i), 1)


            /*reference this from the remove button. Delete item */

        },

        completeItem(i) {
            console.log("completeItem")
            this.done.push(i)
            this.todos.splice(this.todos.indexOf(i), 1)

            /* reference this from the complete button. Add it to Done. 
            Add remove and replace buttons*/
        },

        returnItem(i) {

            console.log("returnItem")
            this.todos.push(i)
            this.done.splice(this.done.indexOf(i), 1)
        }
    }
}


const app = Vue.createApp(App);
app.mount('#app');


Vue.component('todo', {
    template: '<span> <button v-on:click="line= !line" v-bind:class="styling" > complete </button> {{todoname}} </span>',
    data: () => {
        return {
            line: false,
        }
    },
    props: ['todoname'],
    methods: {
        makeline: function () {
            this.line = true
        },
    },
    computed: {
        styling() {
            return {
                line: this.line
            }
        }
    }
})

Vue.component('deleted', {
    template: `<span> <button v-on:click="$emit('deletetodo', todelete )"> delete </button>  </span>`,
    data: () => {
        return {
            toDoList: [],
            toDoItem: [],

        }
    },
    props: ['todelete'],
})


new Vue({
    el: '#app',
    data: () => {
        return {
            toDoItem: [],
            toDoList: [],
        }
    },
    methods: {
        logInput(e) {
            this.toDoItem = e.target.value
            this.toDoList.push(e.target.value)
        },
        deletetodo(toDoItem) {
            this.toDoList.splice(this.toDoList.indexOf(toDoItem), 1)
        }
    },
})


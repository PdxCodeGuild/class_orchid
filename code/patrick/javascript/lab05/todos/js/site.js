
Vue.component('todo', {
    template: '<span> <button v-on:click="line= !line" v-bind:class="styling" > {{todoname}} </button> {{todoname}} </span>',
   
    data: () => {
        
        return {
            line: false,
             



        }
    },
    props:['todoname'],
    methods: {
        makeline: function(){
            this.line = true
        },
        
    

    },
    
    computed: {    
        styling(){
            return {
                line: this.line
            }
        }
    }
    
    
}, 
)

Vue.component('deleted', {
    template: `<span> <button v-on:click="$emit('deletetodo', todelete )">{{todelete}}  </button>  </span>`,
    data: () => {
        
        return {
            toDoList: [],
            toDoItem: [],
            
        }
    },
    props:['todelete'],
    
}


)




new Vue ( {
    
    
    el: '#app',
    data: () => {
        
        return { 
            message: 'Hello, world!' ,
            toDoItem: [],
            toDoList: [],
            line: false,
        }
    },
    methods: {
        logInput(e) {
            this.toDoItem = e.target.value
            this.toDoList.push(e.target.value)
        },
        deletetodo: (toDoItem) => {
            console.log("hello")
            console.log(toDoItem)
            console.log(this.toDoList)
            //console.log(this.toDoList.indexOf(toDoItem))
            this.toDoList.splice(this.toDoList.indexOf(toDoItem),1)
            

        }
        
        
        
        
        
    },
    
           
    

}
)




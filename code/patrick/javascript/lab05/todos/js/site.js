
const toDo = Vue.component('toDo', {
    template: '<button @click="line = !line" > {{toDoName}} </button>',
   
    data: () => {
        
        return {
            line: false, 



        }
    },
    props: ['toDoName']
} 
)



new Vue ( {
    
    components:{
        'toDo': toDo
    },
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
            this.toDoList.push(this.toDoItem)
        },
        styling(){
            return {
                line: this.line
            }
        }
           
            
    
        
    },
    

}
)




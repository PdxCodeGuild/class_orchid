
const App = {
    el: '#app',
    data: () => {
        return { 
            input:'',
            word:[],
            favWordList:[]
        }
    
    },
methods: {
    addWord (input) {
        
        const options = {
            method: 'GET',
            url: `https://wordsapiv1.p.rapidapi.com/words/${input.target.value}/definitions`,
            headers: {
              'X-RapidAPI-Key': '8baca12e90msh0a64a9a369d0a3bp1a615ejsnd390803ad46a',
              'X-RapidAPI-Host': 'wordsapiv1.p.rapidapi.com'
            }
          };
          
          axios.request(options).then((response)=> {
              console.log(response.data);
              this.word = []
              this.word.push(response.data)
          }).catch(function (error) {
              console.error(error);
          });
        },
    favWord : function (item){
        this.favWordList.push(item)
        this.word.splice(this.word.indexOf(item),1)
        },
    deleteWord : function (item) {
        this.favWordList.splice(this.favWordList.indexOf(item),1)
    },
    },
}

const app = Vue.createApp(App)
app.mount('#app')
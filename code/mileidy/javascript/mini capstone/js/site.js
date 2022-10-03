const App = {
    el: '#app',
    data: () => {
        return {dogBreeds : [], favoritesList : []}
    },
    methods :{
        addDogbreeds(e) {
            const options = {
                method: 'GET',
                url: 'https://dogbreeddb.p.rapidapi.com/',
                params: { search: e.target.value },
                headers: {
                    'X-RapidAPI-Key': '7a409cff14msh272a65bad987f00p12b11cjsn0fadf631cd07',
                    'X-RapidAPI-Host': 'dogbreeddb.p.rapidapi.com'
                }
            };
        
            axios.request(options).then((response) => {
                this.dogBreeds = response.data
                console.log(response.data)
            }).catch(function (error) {
                console.error(error);
            });
            console.log(e.target.value)
            },
            favoriteDog(i) {
                this.favoritesList.push(i)
            }, 
            deleteDog(m){
                this.favoritesList.splice(this.favoritesList.indexOf(m), 1)
            },
        }
}      

const app = Vue.createApp(App)
app.mount('#app')
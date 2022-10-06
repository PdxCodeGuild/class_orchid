const app = Vue.createApp({
    data() {
        return {
            info: '',
            searchCity: '',
            returnCity: [],
        }
    },
    methods: {
        search(e) {
            this.searchCity = e.target.value
            console.log(this.searchCity)
            axios
            .get('https://api.openweathermap.org/data/2.5/weather/', {
                headers: {
                    'accept': 'application/json',
                },
                params: {
                  'q': this.searchCity,
                  'appid': '4e865cbc120af5106cdb531655675627',
                  'units': 'imperial',
                }
            })
            .then(res => (this.returnCity = res.data))
            this.returnCity = ''
            }

        }
    
    }
);

app.mount('#weather');
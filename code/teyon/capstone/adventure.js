import airportData from "./airports.js"

new Vue({
    el: '#app',
    data () {
        return {
            info: null,
            incoming: null, 
            outgoing: null,
            date: null,
            airports: airportData,
            outgoingIata: null,
            incomingIata: null,
            favFlight: [],
            incLat: null,
            incLon: null,
            outLat: null,
            outLon: null,
            price: null,
            map: null,
            information: null
        }
    },

    methods: {

        getIata(){
            let departure = this.outgoing

            for(let key in this.airports){
                if(this.airports[key]["location"] == departure){
                    this.outgoingIata = this.airports[key]["airport"]
                }
                
            }
            let arrival = this.incoming

            for(let key in this.airports){
                if(this.airports[key]["location"] == arrival){
                    this.incomingIata = this.airports[key]["airport"]

                }
            }

            this.flightData()
            
        },

        flightData(){
            axios
            .get('https://priceline-com-provider.p.rapidapi.com/v1/flights/search',{
            params: {"itinerary_type":"ONE_WAY","class_type":"ECO","location_arrival":this.incomingIata,"date_departure":this.date,"location_departure":this.outgoingIata,"sort_order":"PRICE","number_of_stops":"1","price_max":"20000","number_of_passengers":"1","duration_max":"2051","price_min":"100"},
            headers: {
                'X-RapidAPI-Key': '71c7cd9e87msh636c8b829338161p16fe2djsnac414d19ae23',
                'X-RapidAPI-Host': 'priceline-com-provider.p.rapidapi.com'
            }
        }
            )
            .then(response => { 
                for (let index = 0; index < response.data.totalTripSummary.airport.length; index++){
                    if(response.data.totalTripSummary.airport[index].lowestTotalFare.amount == response.data.totalTripSummary.minTotalFareWithTaxesAndFees){
                        this.price = response.data.totalTripSummary.airport[index]
                        console.log(this.price)
                        }
                    }
                })
        
                    

            this.iataLatLong()
            

            },

        savedFlights(item){

            this.favFlight.push(item)
            


        },

        iataLatLong(){
            let arriving = this.incomingIata
            
            // axios
            // .get ('https://priceline-com-provider.p.rapidapi.com/v1/flights/locations',{
            // params: {name: arriving},
            // headers: {
            //     'X-RapidAPI-Key': '71c7cd9e87msh636c8b829338161p16fe2djsnac414d19ae23',
            //     'X-RapidAPI-Host': 'priceline-com-provider.p.rapidapi.com'
            // }
            // }
            // )
            // .then(response => {
            //     this.incLatLon = response.data[id]
            //     console.log(this.incLatLon)})

            // let depart = this.outgoingIata
            
            // axios
            // .get ('https://priceline-com-provider.p.rapidapi.com/v1/flights/locations',{
            // params: {name: depart},
            // headers: {
            //     'X-RapidAPI-Key': '71c7cd9e87msh636c8b829338161p16fe2djsnac414d19ae23',
            //     'X-RapidAPI-Host': 'priceline-com-provider.p.rapidapi.com'
            // }
            // }
            // )
            // .then(response => {
            //     this.outLatLon = response.data
            //     console.log(this.outLatLon)
            // })
            axios
            .get(`https://travel-hacking-tool.p.rapidapi.com/api/airports/${arriving}/`,{headers: {
                'X-RapidAPI-Key': '71c7cd9e87msh636c8b829338161p16fe2djsnac414d19ae23',
                'X-RapidAPI-Host': 'travel-hacking-tool.p.rapidapi.com'
            }
            })
            .then(response => {
                this.incLat = response.data.latitude
                this.incLon = response.data.longitude
                console.log(this.information)
                console.log(this.incLat, "incLat")
                console.log(this.incLon, "incLon")})
                
                let depart = this.outgoingIata

                axios
                .get(`https://travel-hacking-tool.p.rapidapi.com/api/airports/${depart}/`,{headers: {
                    'X-RapidAPI-Key': '71c7cd9e87msh636c8b829338161p16fe2djsnac414d19ae23',
                    'X-RapidAPI-Host': 'travel-hacking-tool.p.rapidapi.com'
                }
                })
                .then(response => {
                    this.outLat = response.data.latitude
                    this.outLon = response.data.longitude
                    this.information = response.data
                    console.log(this.information)
                    console.log(this.outLat, "outlat")
                    console.log(this.outLon, "outlon")
                    this.googleMap()    
                    })
                    
                
                },

            googleMap(){

                const outLatLon = { lat: this.outLat, lng: this.outLon };
                const incLatLon = { lat:this.incLat, lng: this.incLon }
                console.log(outLatLon)
                console.log(this.outLat)
                
                
                const map = new google.maps.Map(document.getElementById("map"), {
                    center: { lat: 0, lng: 0 },
                    zoom: 2,
                });
                new google.maps.Marker({
                    position: outLatLon,
                    map,
                    title: "Hello World!",
            });   
                new google.maps.Marker({
                    position: incLatLon,
                    map,
                    title: "Hello World!",
            })  

            },

        },



    computed: {
        filteredInfo(){
            if(this.price){
                console.log(this.price)


                return this.price
                
                

            }
        return null


        }

    },

    mounted() {

        const map = new google.maps.Map(document.getElementById("map"), {
            center: { lat: 0, lng: 0 },
            zoom: 2,
        });

    
    }
})



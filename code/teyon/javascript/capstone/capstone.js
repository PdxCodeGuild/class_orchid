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
            .then(response => (this.info = response))

            },

        savedFlights(item){

            this.favFlight.push(item)
            


        }

    },



    computed: {
        filteredInfo(){
            if(this.info){


                return this.info.data.totalTripSummary.airport

            }
        return null


        }

    }
})
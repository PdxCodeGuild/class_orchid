import axios from "axios"

new Vue({
    el: '#app',
    data () {
        return {
            info: null
        }
    },
    methods: {
        flightdata(){
            
            
            axios
            .get('https://priceline-com-provider.p.rapidapi.com/v1/flights/search',
            params = {"itinerary_type":"ONE_WAY","class_type":"ECO","location_arrival":arrival_iata,"date_departure":date,"location_departure":outgoing_iata,"sort_order":"PRICE","number_of_stops":"1","price_max":"20000","number_of_passengers":"1","duration_max":"2051","price_min":"100"},
            headers = {
                'X-RapidAPI-Key': '71c7cd9e87msh636c8b829338161p16fe2djsnac414d19ae23',
                'X-RapidAPI-Host': 'priceline-com-provider.p.rapidapi.com'
            }
            )
            .then(response => (this.info = response.data.flights))

            }
    }
})
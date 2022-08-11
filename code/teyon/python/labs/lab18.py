import requests
import json
import pprint

print("Welcome to Cheapest Flight Finder!")

#csv info

#created a variable called file path which is the data we want to read
filepath = '../data/airports.csv'

#make the data in the file readable
with open(filepath, 'r') as f:
    contents = f.read()


#creates a list of the lines
lines = contents.split('\n')

#creates headers as the first line
header = lines[0]
#created an individual list of the header
header = header.split(',')

#blank list which will hold the list of airports without the header
list_of_airports = []

#the final list that will hold the dictionaries we will create later
list_of_dicts = []

#took the lines in contents and removed the header line so it is only the names and attributes
airports = lines[1:]

#for loop to appened each airport and city to a list
for airport in airports:
    airport = airport.split(",")
    list_of_airports.append(airport)


#for loop that iterates through every new list we created and appended to the list of airports   
for list in list_of_airports:
    #empty dictionary that will hold each airport with header
    dict = {}
    #enumerate creates a tuple which is index and item together inside the list, 
    for i,info_iata in enumerate(list):
        dict[header[i]] = info_iata

    #list of dicts appends with every newly created dictionary callec dict
    list_of_dicts.append(dict)


#flight code

date = input("What date are you looking to leave(Year-Month-Day(2022-12-20)): ")
outgoing_location = input("What is your outgoing city: ")


for dictionary in list_of_dicts:
    if dictionary['Location'] == outgoing_location:
        print(dictionary)
        outgoing_iata = dictionary['Airport']
        break


fantasy_destination_1 = input("What is your arrival destination: ")


for iata in list_of_dicts:
    if iata['Location'] == fantasy_destination_1:
        arrival_iata = iata['Airport']
        break



url = "https://priceline-com-provider.p.rapidapi.com/v1/flights/search"

querystring = {"itinerary_type":"ONE_WAY","class_type":"ECO","location_arrival":arrival_iata,"date_departure":date,"location_departure":outgoing_iata,"sort_order":"PRICE","number_of_stops":"1","price_max":"20000","number_of_passengers":"1","duration_max":"2051","price_min":"100"}

headers = {
	"X-RapidAPI-Key": "71c7cd9e87msh636c8b829338161p16fe2djsnac414d19ae23",
	"X-RapidAPI-Host": "priceline-com-provider.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

# pprint.pprint(response.text)

data = json.loads(response.text)
price = data["totalTripSummary"]["minTotalFareWithTaxesAndFees"]
print(price)

for carrier in data["filteredTripSummary"]["carrier"]:
    for airport in carrier["airport"]:
        for stop in airport["stops"]:
            if price == stop["lowestTotalFare"]:
                print(f"""
                There are currently {stop['numberOfItineraries']} tickets available
                {carrier['code']} 
                is offering flights from {airport['origAirport']} to {airport['destAirport']} 
                for {stop['lowestTotalFare']} 
                on {date} 
                """)
                
    


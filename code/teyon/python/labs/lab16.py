#Dad jokes part 1
import requests
import json
from time import sleep
#welcome the user to the generator
print("Welcome to the Dad Joke Generator\n")

#request access to the dad jokes api
response = requests.get('https://icanhazdadjoke.com/', headers={'accept':'application/json'})
#taking the results of the request and placing them in a json 
response = response.json()

#variable that extracts a joke from the json file
joke = response['joke']
#print the joke
print(f"The first joke is on us :)\n {joke}\n")   




#Dad jokes part 2

#part to welcome statement
print("Now its your turn to Generate some Dad jokes\n")
#while loop that will continually ask the user to input a word to generate jokes until done is typed
while True:
    #user import to search for jokes
    search = input("Type a word to find a corresponding dad joke or type done to exit dad joke generator: \n")

    #parameters set for the api returned results
    params = {
        'page': '1',
        'limit': '20',
        'term': search

    }
    #request access to dad jokes api
    searched_response = requests.get('https://icanhazdadjoke.com/search',params=params, headers={'accept':'application/json'})
    #variable created the takes the results of the api request and puts them in a json format
    searched_response = searched_response.json()
    #if statements that will either break the while loop or continue asking for user input
    if search == 'done':
        break
    else:
    #for loop that iterates through the searched response for each result in the json
        for results in searched_response['results']:
            #3 seconds before each iteration and joke is printed
            sleep(3)

            #creating a variable that goes into each result and pulls out the value for the joke key
            final_results = results['joke']
            #print the value for each joke key
            print(final_results)

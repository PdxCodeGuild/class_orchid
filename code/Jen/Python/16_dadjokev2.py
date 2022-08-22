'''Jen Williams
PDX Code Guild Bootcamp - Orchid
lab 16: Dad Joke'''

import requests
from time import sleep

while True:
    print("Would you like a random joke or would you like to search for a specific topic? ")
    choice = input("Please type random or search. \nIf you would like to exit, type exit. " )

    if choice == 'random':

        response = requests.get('https://icanhazdadjoke.com', headers={'accept': 'application/json'})
        data = response.json()

        print(data.get('joke'), '\n')

    elif choice == 'search':
        search_term = input("What jokes would you like to search? ")
        response = requests.get('https://icanhazdadjoke.com/search', headers={'accept': 'application/json'}, params={'term': search_term})
    

        data = response.json()

        data=data.get('results')
    
        for i in range(len(data)):
            print(data[i].get('joke'), '\n')
            sleep(2)
        else:
            print("Sorry, we're all out of jokes of that type.\n")

    elif choice == 'exit':
        break

    else: 
        choice = input("Please choose either random or search. If you are done, type exit. ")



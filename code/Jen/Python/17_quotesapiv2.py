'''Jen Williams
PDX Code Guild Bootcamp - Orchid
lab 17: Quotes'''

import requests

while True:
    print("Would you like the quote of the day or to search for a specific topic? ")
    choice = input("Please type qotd or search. \nIf you would like to exit, type exit. ")

    if choice == 'qotd':

        response = requests.get('https://favqs.com/api/qotd', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
        data = response.json()
        quote=data.get('quote').get('body')
        info=data.get('quote').get('author')
        print(f"{quote} Author - {info}"'\n')

    elif choice == 'search':
        
        search = input("What term would you like to search? ")
        response = requests.get('https://favqs.com/api/quotes', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'} , params={'filter': search})
        data = response.json()
        #print(data)
        peel=data.get('quotes')
        for i, info in enumerate(peel):
            print(peel[i].get('body'), '\n')
    elif choice == 'exit':
        print("Goodbye")
        break

    else:
        choice = input("Please choose either qotd or search. If you are done, type exit. ")



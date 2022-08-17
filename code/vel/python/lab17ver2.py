"""
Lab 17 version 2
"""

"""
use the keyword they input and match that to a key to print the value
print the number of quotes then print the quotes

"""



import requests
import json

# response = requests.get(f'https://icanhazdadjoke.com/search?term={name}', params = params, headers = {'accept': 'application/json'})





while True:
    keyword = input('Enter a keyword to search for quotes: ')

    response = requests.get(
        'https://favqs.com/api/quotes/', 
        params = {'filter':keyword}, 
        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
        )

    response = response.json()
    # response = json.dumps(response, indent=4)

    #would this be how i get the number of quotes containing my keyword/user input?
    number_of_quotes = len(response['quotes'])
    print(f'\n{number_of_quotes} quotes associated with nature')
    for quote in response['quotes']:
        print(quote['body'])
        print(quote['author'])

    
    play_again = input("Do you want another quote? y/n: ")
    if play_again == 'n':
        print('Glad we could help!')
        break




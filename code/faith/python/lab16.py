
import requests
import json


search_term = input('please enter search term: ')
params = {
    'page':'1',
    'limit':'20',
    'term': search_term
}



response = requests.get('https://icanhazdadjoke.com/search',params=params, headers={'accept': 'application/json'})
# print(response.text)
joke_dict = response.json()
joke = joke_dict['results']

for x in joke:
    print(x['joke'])

# final_joke =joke[0]
# print(final_joke['joke'])
# print(joke)


   
import requests
import json
from pprint import pprint
params = {
    "current_page": 1,
    "limit": 20,
    "next_page": 2,
    "previous_page": 1,
}

name = input(f'what is the name of what you are searching for? : ')

response = requests.get(f'https://icanhazdadjoke.com/search?term={name}',params = params, headers={'accept': 'application/json'})
dictionary = response.json()
# print(dictionary['results'])        


for result in dictionary['results']:
    print(result['joke'])
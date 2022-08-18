import requests
from pprint import pprint

keyword = input('What would you like to search for:')

params = {
    'filter' : keyword
}

response = requests.get('https://favqs.com/api/quotes/', params=params, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
# pprint(response.text)
data = response.json()
for quote in data['quotes']:
    print(quote['author'] + '\n' + quote['body'] + '\n')





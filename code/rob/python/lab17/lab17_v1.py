import requests

req = requests.get('https://favqs.com/api/qotd')

data = req.json()

print('Author: ' + data['quote']['author'])
print('Quote: ', data['quote']['body'])

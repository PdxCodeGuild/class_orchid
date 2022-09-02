import requests

url = 'https://icanhazdadjoke.com/'

response = requests.request('GET', url, headers={'accept': 'application/json'})
response = response.json()

print(response.get('joke'))
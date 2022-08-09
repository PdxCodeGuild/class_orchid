import requests
import json
import time

print('Hello and welcome to Dad Jokes Gallore!')

name = input('What is your name? ')

print(f'Thank you for coming {name}!') 
response = input('Would you like to hear a joke? (yes/no): ')
while True:
    if response == 'yes':
        end_point = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
        end_point = end_point.json()
        time.sleep(3)
        print(end_point['joke'])
        
        break
    else:
        print('goodbye')

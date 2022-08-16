"""
Lab 16: Dad jokes api
"""
import requests
import json
import time


print("Welcome to dads stand up!")

response = input(f"Are you ready for some dad jokes? yes or no?: ").lower()

while True:
    if response == 'yes':
        end_point = requests.get('https://icanhazdadjoke.com/', headers ={'accept': 'application/json'})
        end_point = end_point.json()
        time.sleep(2)
        print(end_point['joke'])
        break
    else:
        print('Maybe nest time hahaha! (Did you get the joke? "Nest time" hahaha)')
        break

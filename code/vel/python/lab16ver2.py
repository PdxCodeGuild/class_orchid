"""
Lab 16 version 2
"""

from urllib import response
import requests
import json
import time
from pprint import pprint

params = {
    "current_page": 1,
    "limit": 20,
    "next_page": 2,
    "previous_page": 1,

}

name = input("What is the name of what you're looking for?: ")

response = requests.get(f'https://icanhazdadjoke.com/search?term={name}',params = params, headers={'accept': 'application/json'})

dict = response.json()

for result in dict['results']:
    print(result['joke'])
"""
Lab 16: Dad Jokes API
Cesar Rebolledo
"""
import requests
import pprint
import json

response = requests.get('https://icanhazdadjoke.com/', headers={'accept' : 'application/json'})
response = json.loads(response.text)

print(response['joke'])





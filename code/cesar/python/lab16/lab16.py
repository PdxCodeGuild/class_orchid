"""
Lab 16: Dad Jokes API 
Cesar Rebolledo

Part 1
Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ with the accept header as application/json. 
This will return a dad joke in JSON format. You can then use the .json() method on the response to get a dictionary. 
Get the joke out of the dictionary and show it to the user.
"""
import requests
from pprint import pprint
import json


response = requests.get('https://icanhazdadjoke.com/', headers={'accept' : 'application/json'})
response = json.loads(response.text)

print(f'''

Hello there!

        Here is a dad joke for you:

"{response['joke']}"
''')


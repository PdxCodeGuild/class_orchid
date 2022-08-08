import requests 
import json

response = requests.get('https://icanhazdadjoke.com/', headers={})

response = json.loads(response.text)


import requests

base_url = 'https://www.strava.com/oauth/authorize'

res = requests.get(base_url) 

print(res.json())
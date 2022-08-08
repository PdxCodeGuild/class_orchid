# LAB 18: Mini Capstone # 



import requests
import json
from base64 import b64encode


"""  #Make a Test Call
curl -X POST \
  'https://api.kroger.com/v1/connect/oauth2/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Authorization: Basic {{base64(cakeeaters-2b6711aa71841b8c080f4db876a49089597637486573096327:yzmxG_3kVdrai9C7WyZj_J4AxDB9swR_RIpcPI88)}}' \
  -d 'grant_type=client_credentials'

"""
#.addHeader("Authorization", "Basic {{base64(“CLIENT_ID:CLIENT_SECRET”)}}")


client_id = 'cakeeaters-2b6711aa71841b8c080f4db876a49089597637486573096327'
client_secret = 'yzmxG_3kVdrai9C7WyZj_J4AxDB9swR_RIpcPI88'


clientid_secret = client_id +':'+ client_secret
headers = f'Authorization: Basic {clientid_secret}'

grocery_list = [
    'spinach', 
    'strawberries',
    'mandarin orange',
    'almond milk',
    'carrots',
    'watermelon',
    'lemon',
    'sweet potato',
    'kale',
    'cucumber',
]

#response = requests.get(f'https://api-ce.kroger.com/v1/connect/oauth2/authorize?{headers}')
response = requests.get('https://api-ce.kroger.com/v1/connect/oauth2/authorize',auth=(client_id, client_secret))

print(response)



#path 
# https://api-ce.kroger.com/v1/


#https://api.kroger.com/v1/connect/oauth2/authorize?scope={{SCOPES}}&response_type=code&client_id={{CLIENT_ID}}&redirect_uri={{REDIRECT_URI}}




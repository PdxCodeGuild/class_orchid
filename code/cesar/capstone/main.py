import requests
from pprint import pprint 
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# activities_url = "https://www.strava.com/api/v3/athlete/activities"


# header = {'Authorization': 'Bearer ' + 'e3d03388c3d23863868a5eca6bce8534b1eb3012'}
# param = {'per_page':200, 'page':1}

# response = requests.get(activities_url, headers=header, params=param).json()


# pprint(response) 


auth_url = "https://www.strava.com/oauth/token"

payload = {
    'client_id': '95093',
    'client_secret': 'cd5c86fe0a0a72e91064e06b6cc83c048a90bf3f',
    'refresh_token': 'b31d26a77c81b482620171e7aec26cd08c121b83',
    'grant_type': 'refresh_token',
}

print("requesting token \n")

res = requests.post(auth_url,data=payload, verify=False)
# pprint(res.json())


access_token = res.json()['access_token']

print("Access Token: {}".format(access_token))

activities_url = "https://www.strava.com/api/v3/athlete/activities"


header = {'Authorization': 'Bearer ' + 'e3d03388c3d23863868a5eca6bce8534b1eb3012'}
param = {'per_page':200, 'page':1}

response = requests.get(activities_url, headers=header, params=param).json()


pprint(response) 




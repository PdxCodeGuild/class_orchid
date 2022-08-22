import requests
import json


params = {
    "inc" : 'author,body',
    "results" : "1",

}



response = requests.get("https://favqs.com/api/qotd", params=params, headers = {'accept' : 'application/json'})
response = json.loads(response.text)
print(response['quote']['author'])
print(response['quote']['body'])
      


    
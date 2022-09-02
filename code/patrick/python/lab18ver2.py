import pprint
import re
import requests
import json

params = {
    "type" :"public",
     "app_id" : "1cdc9597", 
    "app_key" : "60b438b2284a5c3d5ae7d03e81caac11",
    "q" : "type of food",

}


def test():
    type_of_food_requested = input(f"Please enter the type of food you want to search for: ")
    params.update({"q": [type_of_food_requested]})
    #print(params)

    response = requests.get("https://api.edamam.com/api/recipes/v2", params=params, headers = {'accept' : 'application/json'})
    response = json.loads(response.text)

    hits = response["hits"]



    w1 = hits[1]
    #print(w1["recipe"].keys())



    print(f"Here is the ingrediant list:", w1["recipe"]["ingredientLines"])
    print(f'Here is the link for the instructions:', w1["recipe"] ["url"])


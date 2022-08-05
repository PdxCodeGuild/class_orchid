

import requests
import json


params = {
    "keyword": "keyword"

}


import pprint

while True:
    keyword = input(f"enter the keyword or 'done' to quit: ")
    params.update({"keyword" : keyword })
    
    if keyword != "done":
        response = requests.get("https://favqs.com/api/quotes", params=params, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'} )
        
        response = response.json()
        #pprint.pprint(response.keys())
        
        quotes = response['quotes']
        #print(quotes)
        #print("!" *20)
        #print(quotes[1]['body'])
        #print(quotes[1]['author'])
        for i, item in enumerate(quotes):
            print(quotes[i]['body'])
            print(quotes[i]['author'])    
    if keyword == "done":
        print(f"Thanks for laughing with us!") 
        break



   

    
    
    
   


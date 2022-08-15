

import requests
import json




import pprint

while True:
    params = {
        "keyword": "keyword"

        }
    keyword = input(f"enter the keyword or 'done' to quit: ")
    params.update({"keyword" : keyword })
    
    if keyword != "done":
        #response = requests.get("https://favqs.com/api/quotes", params=params, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'} )
        response = requests.get("https://favqs.com/api/quotes?filter=<keyword>", params=params, headers = {'Content-Type: application/json''Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'} )
        response = response.json()
        #pprint.pprint(response.keys())
        
        quotes = response['quotes']
        print(quotes)
        #print(quotes)
        #print("!" *20)
        #print(quotes[1]['body'])
        #print(quotes[1]['author'])
        for i, item in enumerate(quotes):
            print(quotes[i]['body'])
            #print(quotes[i]['author'])    
    if keyword == "done":
        print(f"Thanks for laughing with us!") 
        break



   

    
    
    
   


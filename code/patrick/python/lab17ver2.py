

import requests
import json




import pprint

while True:
    params = {
        
        "inc" : "author, body",
        "results": "25"

        }
   
    
    keyword = input(f"enter the keyword or 'done' to quit: ")
    
    headers = {
    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
     'accept' : 'application/json',
     }
    
    
    
    if keyword != "done":
        response = requests.get("https://favqs.com/api/quotes?filter=<keyword>", params=params, headers = headers )
        #response = requests.get("https://favqs.com/api/quotes', params=params , headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'} )
        #response = requests.get("https://favqs.com/api/quotes?filter=keyword", params=params,  headers = {'accept' : 'application/json'} )
        print(response)
        #response = json(response.text)
        response = response.json()
        #pprint.pprint(response.keys())
        print(response)
        
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



   

    
    
    
   


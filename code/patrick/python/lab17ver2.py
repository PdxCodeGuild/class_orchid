

import requests
import json




import pprint

while True:
    params = {
        
        "inc" : "author, body",
        "results": "25",
        

        }
   
    
    keyword = input(f"enter the keyword or 'done' to quit: ")
   
    headers = {
    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"',
     'accept' : 'application/json',
     }
    
    
    
    if keyword != "done":
        response = requests.get(f"https://favqs.com/api/quotes?filter={keyword}", params=params, headers = headers )
        
        response = response.json()
        
        
        quotes = response['quotes']
        
        for i, item in enumerate(quotes):
            print(quotes[i]['body'])
                
    if keyword == "done":
        print(f"Thanks for laughing with us!") 
        break



   

    
    
    
   


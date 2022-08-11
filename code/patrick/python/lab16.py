
import requests
import json








    
params = {
    'results' : '20',
    'term' : 'search_term',
    'inc' : 'joke',

    }
term = input("please enter your search term or quit: ")
results = int(input(f"Please enter the number of results wanted: "))
params.update({'term': term})
params.update({'results': results})
print(params)
options = '''
    1. show me jokes
    2. changer search term
    3. quit
'''
import time
while True:
    jokes = []
    user_input = input(options)    
    if user_input == "1":
        while len(jokes) <= int(results):
            response = requests.get("https://icanhazdadjoke.com/search", params=params, headers = {'accept' : 'application/json'})
            response = json.loads(response.text)
            #print(response["joke"])
            result = response["results"]
            for i, item in enumerate(result):
                w1 = result[i]
                w2 = (w1['joke'])
                
                print(w2)
            
                    




            time.sleep(2)
            jokes.append(w2)

    if user_input == "3":
        print(f"Game over, Thanks for laughing with us!")
        break
    
    if user_input == "2":
        search_term = input("please enter your search term or quit: ")
        params.update({'search_term': search_term})
        if search_term == "quit":
                    print(f"Game over!")
                    break













        




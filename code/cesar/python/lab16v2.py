"""
Lab 16: Dad Jokes API
Cesar Rebolledo

Part 2
Add the ability to "search" for jokes using another endpoint. Create a REPL that allows one to enter a search term 
for dad jokes on different subjects. You can show all (up to 20) jokes at once, or use time.sleep to keep them coming
at a steady pace. As a bonus, you can ask the user if they want to see the next 20 jokes.
"""
import requests
from pprint import pprint
import json
import time
# function to take in the term from the nested if loop. 
# will return list called results_jokes. 
def search_jokes(term):
        
        response = requests.get(f'https://icanhazdadjoke.com/search?term={term}', 
        headers={'accept' : 'application/json'})
        results = json.loads(response.text)
        result_jokes = results['results']
        return result_jokes
# function to help with spacing. takes in two params. 
def pauser(i, j):
        print(i,j.get("joke"),"--","\n")
        time.sleep(1)

options = f"""
        Welcome!
        (1) Search 
        (2) End 
      Enter options: """
# start of my REPL 
while True:
        input_options = input(options)
        print(input_options)
        if input_options == '2':
                print('Goodbye!')
                break
        
        elif input_options == '1':
                # Calling function. 
                jokes = search_jokes(input('term: '))
                # Trying my luck with list comprehension. 
                term_jokes = [pauser(i,j) for i,j in enumerate(jokes)]
        else:
                print("Not a valid options, try again.")
        

        


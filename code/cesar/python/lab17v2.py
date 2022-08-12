"""
Lab 17 Version 2: 
+++++++++++++++++
Cesar Rebolledo
+++++++++++++++++
The Favqs Quote API also supports getting a list of quotes associated with a 
given keyword https://favqs.com/api/quotes?filter=<keyword>. 
Prompt the user for a keyword, list the quotes you get in response, and prompt the user to enter a new keyword.

> enter a keyword to search for quotes: nature
25 quotes associated with nature 
<list of quotes>
> enter a keyword to search for quotes:
This API endpoint requires an API key be included in a request header. You can find documentation of
 specifying request headers here and documentation on authorization with the Favqs API here under "Authorization".

headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
"""

import requests, json, time
from pprint import pprint

# Def a function to take in one parameter: in the while loop to take in a search term.
def term_finder(term):
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    response = requests.get(f'https://favqs.com/api/quotes?filter={term}',headers=headers)
    response = json.loads(response.text) # type dict 
    results_list = response['quotes'] # this will result in a type: list 
    return results_list

choice = f'''
Chose from one of the follow:
1 - Search a quote by a keyword
2 - End/Quit 

Option: '''

while True:
    user_input = input(choice)
    if user_input == "2":
        print("Goodbye!")
        break
    elif user_input == "1":
        keyword_search = input("Search quote by keyword: ")
        for i, quote in enumerate(term_finder(keyword_search),1):
            print(f'{i} - {quote["body"]} \n quote by: {quote["author"]} \n')
            time.sleep(1)

    



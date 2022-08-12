"""
Lab 17 Version 2: 
+++++++++++++++++
Cesar Rebolledo
+++++++++++++++++
Version 3: Pagination (Optional)
You can continue showing quotes after the first 25 by specifying a page query parameter. 
For example page 2 will display quotes 26-50. https://favqs.com/api/quotes?page=<page>&filter=<keyword>. 
Prompt the user for a keyword, list the first page of quotes you get in response, and prompt the user to 
either show the next page or enter a new keyword. You can use string concatenation to build the URL.

> enter a keyword to search for quotes: nature
25 quotes associated with nature - page 1
<list of quotes>
> enter 'next page' or 'done': next page
25 quotes associated with nature - page 2
<list of quotes>
> enter 'next page' or 'done': done
> enter a keyword to search for quotes:
"""

import requests, json, time
from pprint import pprint

# # Def a function to take in one parameter: in the while loop to take in a search term.
# def term_finder(term):
#     headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
#     response = requests.get(f'https://favqs.com/api/quotes?filter=nature',headers=headers)
#     response = json.loads(response.text) # type dict 
#     results_list = response['quotes'] # this will result in a type: list 
#     return results_list

# def next_page():
#     headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
#     response = requests.get(f'https://favqs.com/api/quotes?filter=nature',headers=headers)
#     response = json.loads(response.text) # type dict
#     print(type(response['next_page']))

    

# choice = f'''
# Chose from one of the follow:
# 1 - Search a quote by a keyword
# 2 - End/Quit 

# Option: '''

# while True:
#     user_input = input(choice)
#     if user_input == "2":
#         print("Goodbye!")
#         break
#     elif user_input == "1":
#         keyword_search = input("Search quote by keyword: ")
#         for i, quote in enumerate(term_finder(keyword_search),1):
#             print(f'{i} - {quote["body"]} \n quote by: {quote["author"]} \n')
#             time.sleep(1)



# def last_page(count):
#     headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
#     response = requests.get(f'https://favqs.com/api/quotes?page={count}?filter=camp',headers=headers)
#     response = json.loads(response.text) # type dict 
#     response = response['quotes'][0]['body']
    
#     return response



# print(last_page(1))

headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
response = requests.get(f'https://favqs.com/api/quotes?page=1?filter=nature',headers=headers)
response = json.loads(response.text) # type dict 


parse_quote = response["quotes"][0]['body']

# print(parse_quote)
page_count = 1


def next_p(page):
    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    response = requests.get(f'https://favqs.com/api/quotes?page={page}?filter=nature',headers=headers)
    response = json.loads(response.text) # type dict 
    return response

pprint(next_p(2))


# while parse_quote != "No quotes found":
#     page_count += 1
#     print('No more')
#     print(page_count)





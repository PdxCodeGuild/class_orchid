import requests
import json
import sys
import time

header = {
    'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
}

def main():
    '''Initializes'''
    term = search_query()
    page = 1
    response = response_fetch(term, page)
    joke_print(response, term, page)
    

def search_query():
    '''returns term and joke limit based on input'''
    term = input('What kind of Quote\'s are you looking for?\n> ')
    return term

def response_fetch(term, page=1):
    '''fetches quotes based on query'''
    response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={term}', headers=header)
    return response.json()

def joke_print(response, term, page):
    quote_count = len(response['quotes'])
    x = 0
    while x < quote_count:
        print('\n' + response['quotes'][x]['body'])
        print(f"-{response['quotes'][x]['author']}")
        x += 1        

    if response['last_page'] == False:
        print(f'\nWould you like to see another {quote_count} Quote\'s?')
        next_step = int(input('1. Yes\n2. Search for more jokes\n3. Exit\n> '))
    else:
        print("There are no more quote's to display, what would you like to do?")
        next_step = int(input('1. End of search results\n2. Search for more quote\'s\n3. Exit\n> '))

    if next_step == 1:
        if response['last_page'] == True:
            main()
        page += 1
        response = response_fetch(term, page)
        joke_print(response, term, page)
    elif next_step == 2:
        main()
    else:
        sys.exit()
    

print('\nSearch for Quote\'s from FaveQ')
main() 
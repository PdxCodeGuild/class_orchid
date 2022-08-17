import requests
import json
import sys
import time

url = 'https://icanhazdadjoke.com'
header = {
    'accept':'application/json'
}

def main():
    '''Initializes'''
    term, limitcount = search_query()
    page = 1
    response = response_fetch(term, page, limitcount)
    joke_print(response, term, page, limitcount)
    

def search_query():
    '''returns term and joke limit based on input'''
    term = input('What kind of dad jokes are you looking for?\n> ')
    limitcount = int(input('How many jokes would you like to see?\n> '))

    return term, limitcount

def response_fetch(term, page=1, limitcount=20):
    '''fetches dad jokes based on query'''
    response = requests.get(f'https://icanhazdadjoke.com/search?term={term}&page={page}&limit={limitcount}', headers=header)
    return response.json()

def joke_print(response, term, page, limitcount):
    joke_count = len(response['results'])
    x = 0
    while x < joke_count:
        print('\n' + response['results'][x]['joke'])
        x += 1
        time.sleep(1)
    
    print('\nNo more jokes to display!')
    
    print(f'\nWould you like to see another {joke_count} jokes?')
    next_step = int(input('1. Yes\n2. Search for more jokes\n3. Exit\n> '))

    if next_step == 1:
        page += 1
        response = response_fetch(term, page, limitcount)
        joke_print(response, term, page, limitcount)
    elif next_step == 2:
        main()
    else:
        sys.exit()
    

print('\nSearch for Dad Jokes using the icanhazdadjoke.com API')
main()
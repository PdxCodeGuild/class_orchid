import requests
from decouple import config

key = config('KEY')

auth = {'Authorization': f'Token token="{key}"'}


page_num = 1
next_page = 'done'
while True:
    if next_page == 'done':
        search = input('\nEnter a keyword to search for quotes ("enter" to leave): ')
    if search == '':
        break
    parm = {'page': page_num, 'filter': f'{search}'}
    req_prompt = requests.get('https://favqs.com/api/quotes', params=parm, headers=auth)
    data_len = len(req_prompt.json()['quotes'])
    data_quotes = req_prompt.json()['quotes']
    
    print(f'{data_len} quotes associated with nature - page {page_num}\n')
    
    num = 1
    for quote in data_quotes:
        print(f"{num}. {quote['body']}")
        num += 1

    next_page = input('\nEnter \'next page\' or \'done\':')
    if next_page != 'done':
        page_num += 1

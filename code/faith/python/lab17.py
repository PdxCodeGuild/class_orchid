import requests
import json





while True:
    keyword = input('Enter a keyword: ')
    page = 1
    quote = requests.get('https://favqs.com/api/quotes',params={'page': '1','filter':keyword}, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    quote_dict = quote.json()
    quotes = quote_dict['quotes']

    for x in quotes:
       main = x['body']
       author = x['author']
       print(f"{author} : {main}")
      
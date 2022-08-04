import requests

api_token = '649e4ae55c1d9543452f9d0e72f4075d'
api_url_base = 'https://favqs.com/api'

class Quote:
    def get_quotes(self, keyword:str='', page:int=1):
        if keyword:
            self.search = keyword
        headers = {'Authorization': f'Token token="{api_token}"'}
        params = {'page': page, 'filter': self.search}
        response = requests.request('GET', f'{api_url_base}/quotes', params=params, headers=headers)
        response = response.json()
        self.quotes = response.get('quotes')
        self.page = response.get('page')
        self.last_page = response.get('last_page')

q = Quote()
q.get_quotes(keyword=input('Search term: '))

while not q.last_page:
    for quote in q.quotes:
        author, body = quote.get('author'), quote.get('body')
        print(f'\n\n{body}\n\n  ~ {author}\n\n')
    user_input = None
    while not user_input in ['q','s','']:
        user_input = input('Next page [Enter] - Quit [q] - New search [s]')
    if user_input == 'q':
        break
    if user_input == 's':
        q.get_quotes(keyword=input('Search term: '))
    else:
        q.get_quotes(page=q.page+1)


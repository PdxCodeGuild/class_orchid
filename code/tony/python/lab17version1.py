import requests

response = requests.request('GET', 'https://favqs.com/api/qotd')
author, body = response.json().get('quote').get('author'), response.json().get('quote').get('body')
print(f'\n\n{body}\n\n  ~ {author}\n\n')

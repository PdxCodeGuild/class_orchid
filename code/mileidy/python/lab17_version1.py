
import requests
from pprint import pprint
#i referenced request.md

response = requests.get('https://favqs.com/api/qotd/')
# pprint(response.text)
data = response.json()
# pprint(data)


print(data['quote']['author'] + '\n' + data['quote']['body'])


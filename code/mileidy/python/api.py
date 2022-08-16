import requests
import json
from pprint import pprint


dictionary = {'key'}
end_point = requests.get('https://favqs.com/api/qotd', headers={'accept': 'application/json'})
end_point.json()
print(end_point.json())
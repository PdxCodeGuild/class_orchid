"""
Lab 17: Quotes API Version 1
"""

# you used something similiar in your capstone. to grab the quote, not so much the author

import requests
import json
url = 'https://favqs.com/api/qotd'

response = requests.get(url)

response = response.json()

author = response["quote"]['author']

quote = response["quote"]['body']

print('\n' + author + '\n' + quote)

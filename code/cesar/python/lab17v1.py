import requests, json
from pprint import pprint

# api_key = '1073ce4606cd8c09f89ca186d81ab75f'

"""
Version 1: Get a Random Quote
The URL to get a random quote is https://favqs.com/api/qotd, send a request here, parse the JSON 
in the response into a python dictionary, and show the quote and the author.

Cesar Rebolledo 
"""


response = requests.get(f'https://favqs.com/api/qotd')
response = json.loads(response.text)
print(f"""
{"*"*40}
Random quote generated just for you: 

    "{response['quote']['body']}"

Quote by: {response['quote']['author']}
{"*"*40}
""")

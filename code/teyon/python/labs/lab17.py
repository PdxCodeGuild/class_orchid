import requests

print("Welcome to the Quote of The Day generator")

#calling on API
response = requests.get('https://favqs.com/api/qotd', headers={'Content-Type': 'application/json'})

#taking the results of the request and placing them in a json 
response = response.json()
#extracting the quote from the json
quote = response['quote']['body']
#extracting author from json
author = response['quote']['author_permalink']
#print out the final result
print(f"QOTD by {author}: {quote}")

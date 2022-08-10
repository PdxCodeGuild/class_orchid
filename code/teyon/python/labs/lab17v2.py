import requests

print("Welcome to the Quote of The Day generator")

user_keyword = input("Type a keyword to help generate a quote: ")
#calling on API
response = requests.get('https://favqs.com/api/quotes?filter=<keyword>', headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

#taking the results of the request and placing them in a json 
response = response.json()
print(response)

#extracting the quote from the json
# quote = response['quote']['body']
# author = response['quote']['author_permalink']

# print(f"QOTD by {author}: {quote}")
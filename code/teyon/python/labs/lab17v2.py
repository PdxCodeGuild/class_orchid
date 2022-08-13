import requests
import pprint
#welcome 
print("Welcome to the Quote of The Day generator\n")
#creat a function that calls on the api and converts it into a string
def get_quotes(input):
    #calling quotes API
    response = requests.get(f'https://favqs.com/api/quotes?filter={input}', headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    
    #extracting the quote from the json
    response = response.json()
    return response
#user input
keyword = input("Type a keyword to help generate a quote type exit to end: ")


while True:
    #if statement that breaks the loop 
    if keyword == "exit":
        break
    #else call get_quotes function to print quotes
    else:
        response = get_quotes(keyword)

        quotes = response['quotes']
        for quote in quotes:
            print(f'-{quote["body"]}\n')
        #ask user for new keyword after printing
        keyword = input("Type a keyword to help generate a quote type exit to end: ")
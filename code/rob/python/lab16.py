import requests
import time

HEADERS = {'Accept': 'application/json'}

req = requests.get(r'https://icanhazdadjoke.com/', headers=HEADERS)

joke = req.json()['joke']

checks = {
    1: '. ',
    2: ', ',
    3: '? ',
    4: '! ',
}

split_joke = []

for key, check in checks.items():
    if check in joke:
        split_joke = joke.split(f'{check}')

print('\n', split_joke[0])

time.sleep(2)

print(split_joke[1], '\n')


#part 2
term = input('Enter a term for joke search ("exit" to leave): ')


while True:
    if term == 'exit':
        break
    number = int(input('How many do you want?: '))
    parms = { 'page': 1, 'limit': number, 'term': term,}
    req_search = requests.get(r'https://icanhazdadjoke.com/search', params=parms, headers=HEADERS)

    joke_search = req_search.json()['results']
    num = 1
    for joke in joke_search:
        print(f"{num}. {joke['joke']}", '\n')
        num += 1

    term = input('Enter a term for joke search ("exit" to leave): ')

import requests, time, re

search_term = input('Enter a search term: ')

response = requests.request('GET', 'https://icanhazdadjoke.com/search', params={'term': search_term}, headers={'accept': 'application/json'})
response = response.json()

# list of strings
jokes = [str(result.get('joke')) for result in response.get('results')]

# show throbber while sleeping
def do_sleep(d,c):
    [[print(''.join(['.' for i in range(i+1)])),time.sleep(d)] for i in range(c)]

for joke in jokes:

    # split into question + answer
    match = re.findall('^([^,.!?…]+)\s*(\W)\s*(.*)$', joke)[0]
    question = match[0] + match[1]
    answer = match[2]

    print(f'\n\n\n{question}')
    
    if match[2].strip():
        do_sleep(1,3)
        print(answer)
    print('\n\n')

    user_input = ''
    while user_input not in ['y','n']:
        user_input = input('Would you like to hear another [y/n]? ')
    if user_input == 'n': break

city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}



print(f'''

{'*'*80}
Lets take a road trip! In the line below, please enter one of the following
cities:
        Boston
        New York
        Albany
        Portland
        Philadelphia
{'*'*80}

''')

user_city_input = input('Enter a city you would like to visit: ').title()

print(user_city_input)


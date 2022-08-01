city_to_accessible_cities = {
    'Boston': {'New York', 'Albany', 'Portland'},
    'New York': {'Boston', 'Albany', 'Philadelphia'},
    'Albany': {'Boston', 'New York', 'Portland'},
    'Portland': {'Boston', 'Albany'},
    'Philadelphia': {'New York'}
}

for city in enumerate(city_to_accessible_cities):
    print(f'{city[0]+1}: {city[1]}')

user_input = ''
acceptable_input = [str(s) for s in list(range(1,len(city_to_accessible_cities)+1))]

while not user_input in acceptable_input:
    user_input = input(f'Choose a city [1-{len(city_to_accessible_cities)}]: ')

user_city = list(enumerate(city_to_accessible_cities))[int(user_input)-1][1]

connected_cities = city_to_accessible_cities[user_city]
print('Connections: ' + ', '.join([s for s in connected_cities]))

hops = set().union(*[city_to_accessible_cities.get(city) for city in connected_cities])
try: [hops.remove(city) for city in [user_city] + list(connected_cities)]
except KeyError: None
print('Hops: ' + f', '.join([s for s in hops]))

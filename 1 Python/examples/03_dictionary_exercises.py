miles_morales = {
    'superhero': 'Spider-Man',
    'age': 17,
    'home': 'New York City',
    'family': ['Jefferson Davis', 'Rio Morales'],
    'occupation': 'student',
}

"""
Access: dict[key] or dict.get(key)
Access the 'superhero' key to print Miles' superhero name
"""
# print(miles_morales['superhero'])
# print(miles_morales.get('superhero'))
# # print(miles_morales['villain']) # KeyError: 'villain'
# print(miles_morales.get('villain'))

# dict.get will not raise a KeyError if the value is not in the dictionary
# it can also be used to conditionally do different things
# based on whether it is None or an actual value

superhero = miles_morales.get('superhero')
if superhero is not None: # you can use is when comparing to None because there is only one None in memory
    print(f'{superhero} is the superhero name')
else:
    print('no superhero name')

villain = miles_morales.get('villain')
if villain is not None:
    print(f'{villain} is the villain name')
else:
    print('no villain name')

"""
Update: dict[key] = value
Happy Birthday Miles 🎂
Increase Miles' age by 1
"""
miles_morales['age'] = miles_morales['age'] + 1
# miles_morales['age'] += 1 # shorthand for the above line
print(miles_morales)

"""
Add Miles' uncle, Aaron Davis, to the 'family' list value
"""
miles_morales['family'].append('Aaron Davis')
# miles_morales['family'] evaluates down to the list with family members
# you can .append to the end of it

# alternatively, you could extract the family list out
# and the append to that
# family = miles_morales['family']
# family.append('Aaron Davis')
print(miles_morales)


"""
Add key/value pair: dict[key] = value
Add more info to the miles_morales dictionary
"""
miles_morales['voice_actor'] = 'Shameik Moore'
miles_morales['high school'] = 'Brooklyn Visions Academy'
miles_morales['superpowers'] = ['spidey sense', 'web slingin', 'invisibility', 'venom beam'] 
miles_morales['superpowers'].append('lifting 10 tons!')
miles_morales['first_appearance'] = 'Ultimate Comics Fallout #4'
print(miles_morales)

print(miles_morales)

"""dict.update()"""
miles_morales.update({'languages': ['english', 'spanish']})

print(miles_morales)

print('\n\n\n')
"""dict.keys()"""
print(miles_morales.keys())
for key in miles_morales.keys():
    print(key)


"""dict.values()"""
print(miles_morales.values())


"""dict.items()"""
print(miles_morales.items())

print()
print('Miles Morales info:')
for key, value in miles_morales.items():
    print(f'🕷 {key}: {value}')

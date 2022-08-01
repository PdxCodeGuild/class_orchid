


numbers = []
for x in range(10):
    numbers.append(x ** 2)




numbers = [x ** 2 for x in range(10)]







numbers = [1, 2, 3, 4, 5]

evens = []
for number in numbers:
    if number % 2 == 0: # for any integer where number % 2 == 0, that number is even
        evens.append(number)




evens = [number for number in numbers if number % 2 == 0]





"""
EXERCISE 1
Translate for loop to list comprehension
"""
hats = ['baseball cap', 'fedora', 'derby', 'panama']

for hat in hats:
	print(hat)

# list comprehension version...
print_returns = [print(hat) for hat in hats]
# print returns None
print(print_returns) # [None, None, None, None]


"""
EXERCISE 2
Translate for loop to list comprehension
"""
dogs = ['pluto', 'fido', 'clifford', 'lassie']
dog_facts = []
for dog in dogs:
	dog_facts.append(f'{dog.capitalize()} is a good boy.')
print(dog_facts)

# list comprehension version...
dog_facts = [f'{dog.capitalize()} is a good boy.' for dog in dogs]
print(dog_facts)

"""
EXERCISE 3
Translate for loop to list comprehension
"""
numbers = [1, 238, 74, 364, 65, 23, 765]
evens = []
odds = []
for number in numbers:
	if number % 2 == 0:
		evens.append(number)
	else:
		odds.append(number)
print(evens, odds)
# list comprehension version
evens = [number for number in numbers if number % 2 == 0]
odds = [number for number in numbers if number % 2 == 1]
print(evens, odds)
# Pete's attempt to do this with just one list comprehension (it didn't work)
# odds = []
# evens = [number for number if number % 2 else odds.append(number) in numbers if number % 2]


"""
EXERCISE 4
Translate for loop to list comprehension
"""
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
fall = ['september', 'october', 'november']
winter = ['december', 'january', 'february']
seasons2d = [spring, summer, fall, winter]





for season in seasons2d:
    for month in season:
        print(month)





[[print(month) for month in season] for season in seasons2d]

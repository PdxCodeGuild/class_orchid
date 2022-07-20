# Booleans
if True:
    print('this line ran')
if False:
    print('this line didn\'t')

print(1 == 1) # True
print(1 == 2) # False

# Boolean operator:
# and: evaluates down to True if all values or True or "truthy"
# evaluates down to False if any value is False or "falsy"
print(True and True) # True
print(True and False and True and True) # False
print(True and True and True and True and True and True and True and True and True and False) # False

# or: evaluate down to True if any value is True
# evaluate down to False if any value is False
print(True or False or True) # True
print(False or False or False) # False
print(False or False or False or False or True or False) # True

# not: 
print(not True) # False
print(not False) # True

plant = {
    'color': 'green',
    'climate': 'temperate',
    'thirsty': True
}

color = plant.get('color')
if color is not None:
    print(f'The plant\'s color is {color}.')

height = plant.get('height')
if height is not None:
    print(f'The plant\'s height is {height}.')
else:
    print('height unknown')


# Comparisons
# value1 == value2 will return True if the values are equivalent, False if not
print(1 == 1) # True
# value1 != value2 will return True if the values are not equivalent, False if they are
print(1 != 2) # True

# Comparison shorthands:
jackalope = 6
if jackalope >= 4 and jackalope <= 8: # evaluates down to if True and True:
    print('let\'s make another one')

# this is  a shorthand version of the above comparisons
if 4 <= jackalope <= 8:
    print('more jackalopes!')

pete_fav_color = 'green'
tony_fav_color = 'green'
christah_fav_color = 'green'

if pete_fav_color == 'green' and tony_fav_color == 'green' and christah_fav_color == 'green':
    print('💚')

# given value1 == value2 == value3 (and so on), will return true if all values are equivalent
if pete_fav_color == 'green' == tony_fav_color == christah_fav_color:
    print('🥬')

# parentheses in conditionals will evaluate before
# the other expressions
print((5 == 5) == 5) # True == 5 # False

# in & not in
# in
# list: if element is in list
colors = ['red', 'green', 'blue']
print('yellow' in colors) # False
print('yellow' not in colors) # True

# string
print('hello' in 'hello world') # True
print('z' in 'pete') # False

# dictionary
# value in dictionary will return True if that value is a key in the dictionary
computer = {
    'owner': 'Pete',
    'brand': 'Apple',
    'model': 'MacBook Pro',
    'year': 2012
}

print('Pete' in computer) # False
print('owner' in computer) # True

# looping over a dictionary will give you the keys
for key in computer:
    print(key, computer[key])

# here is a way to get the key and value
for key, value in computer.items():
    print(key, value)


# is & is not
# is: will see if values are the same object in memory (if they are identical)
print(True is True) # True
print('hello' is 'hello') # True
print([1, 2, 3] is [1, 2, 3]) # False
print([1, 2, 3] == [1, 2, 3]) # True

numbers1 = [1, 2, 3]
numbers2 = [1, 2, 3]
print(numbers1 == numbers2) # True
print(numbers1 is numbers2) # False

numbers3 = numbers1
print(numbers3 is numbers1) # True (the lists are the same object)

numbers1.append(4)
print(numbers1, numbers2, numbers3) # [1, 2, 3, 4] [1, 2, 3] [1, 2, 3, 4]
print(id(numbers1), id(numbers2), id(numbers3))
# numbers1 and numbers2 have the same id

print(id('hello'), id('hello'))
print(id([1, 2, 3]), id([1, 2, 3])) # 🤷‍♂️

temperature = int(input('what is the temperature? '))


if temperature <= 60:
    print('cold')
elif temperature <= 70:
    print('warm')
elif temperature <= 80:
    print('pretty warm')
elif temperature <= 90:
    print('hot')
else: # this will run if none of the previous conditonals were True
    print("wow it's so hot!")

# short-circuited evaluation
# and
# in this case, it doesn't need to look anymore after
# it finds the False
expression = True and True and False and True and True
# in this case, it will have to read every value in the and
# expression chain to make sure nothing is False or falsey
expression = True and True and True and True

# or
# this is looking for the first truthy value, so it will not need
# to evaluate the rest of the line one it hits True
expression = False or False or True or True or False
# this one will have to to go all the way through
expression = False or False or False or False

# oneline conditionals in python
jackalope = 7
mating_age = True if 4 <= jackalope <= 8 else False
# here is the above line done with a plain if/else block
if 4 <= jackalope <= 8:
    mating_age = True
else:
    mating_age = False
print(mating_age)

# truthy and falsey
# a string with any characters is truthy
# the only falsey string is '' or ""
if 'hello':
    print('hello to you')
if '':
    print('will this print?') # doesn't print
if '0':
    print('the string 0 is truthy?')

# any number other than 0 is truthy
# 0 is falsey
if 123:
    print('my favorite number!')
if 0:
    print('I guess this one is falsey!') # doesn't print

# an empty list is falsey
# any list with elements is truthy
if ['red', 'green', 'blue']:
    print('purple')
if []:
    print('is an empty list truthy?')

# Falsey values: False, 0, None, '', [], {}

def validate_input(ten_digits, two_dashes):
    """function to validate phone #"""
    error = ''
    success = ''
    if ten_digits:
        success += 'Ten digits are present. '
    else:
        error += 'Ten digits not present. '
    if two_dashes:
        success += 'Two dashes are present. '
    else:
        error += 'Two dashes not present. '
    return error, success

error, success = validate_input(True, False)

if error: # expecting error to be a string, if the string is truthy (it isn't empty) we need to give the user their error message
    print('requirements for phone number missing: ')
    print(error)

if error == '':
    print('this might be a better way. using truthy/falsey can lead to errors sometimes')
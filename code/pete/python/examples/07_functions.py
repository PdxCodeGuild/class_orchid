# Defining functions
# functions start with the def keyword, then the name of the function,
# then parentheses, and a colon
# if the function takes any parameters, they will go inside
# the parentheses
def add(x, y):
    # docstrings, multiline strings with 3 """, are used in python
    # for documentation.  VS Code will now display this string, when
    # hovering over this add function
    """given numbers x and y, will return their sum"""
    # validating that both x and y are numbers
    if type(x) is not int and type(x) is not float:
        raise ValueError(f'{x} is not a number')
    if type(y) is not int and type(y) is not float:
        raise ValueError(f'{y} is not a number')
    return x + y
# print(add(3, 5))
# print(add('hello', 'goodbye'))

# Parameters
# the variables passed into the function are called parameters
# in this case, first_name and last_name
# they are parameters as long as they are inside the scope of the function
# and they do not exist as variables outside of its scope

# default parameter/optional argument has the parameter=value notation in the function definition
# if that value is not passed in, it will be considered to be the default value
# in this case, if status is not passed in, it will be the string 'cool'
def staff_bio(first_name, last_name, role, status='cool'): # status is an optional argument with a default value of 'cool'
    # first_name and last_name are parameters
    """given a first_name and a last_name, prints information about staff member"""
    print(f'{first_name} {last_name} is a {status} {role} at PDX Code Guild.')

# 'Pete' and 'Jones' are arguments
fn = 'Pete'
ln = 'Jones'
staff_bio(fn, ln, 'instructor', 'lame') # arguments are what are passed into the function
# paremeters inside the function are not declared at the scope
# outside the function
# print(first_name) # NameError: name 'first_name' is not defined

# passing arguments by position: you pass in arguments in the order that the function expects them
staff_bio('Mitch', 'Chapman', 'TA')

# passing keyword arguments: you can pass arguments with parameter_name=argument_value
# they can be passed in any order this way
staff_bio(role='TA', first_name='Matt', last_name='Walsh')

# staff_bio(last_name='Burrow', first_name='Danny', 'instructor') # SyntaxError: positional argument follows keyword argument
# if using both positional and keyword arguments, all positional arguments must come first
staff_bio('Danny', role='instructor', last_name='Burrow')

# Returning
# the return keyword will end a function and "send back" what value, if any
# comes after it
# return 'hello' will return the string 'hello'

def first_sorted(list_of_strings: list):
    """given a list_of_strings, will sort that list and return the first value after sorting"""
    list_of_strings.sort()
    first_in_list = list_of_strings[0]
    return first_in_list

strings = ['hello', 'goodbye', 'awesome', 'whatever', 'sleepy']
first_item_in_list = first_sorted(strings)
print(first_item_in_list)

# Implicit Return
# if a function doesn't return anything, it will still return None
def say_hi():
    print('saying hello from python 🐍')

return_value = say_hi()
print(return_value) # None

# Returning Multiple Values
# comma-separated values after the return keyword
# will result in multiple return values
def get_dimensions():
    return 500, 200

# tuple unpacking
width, height = get_dimensions()
print(width)
print(height)

dimensions = get_dimensions()
print(dimensions) # (500, 200)

# recursion
# here is a function whose only purpose is to call itself
# def crash_python():
#     crash_python()

# crash_python() # RecursionError: maximum recursion depth exceeded

# for loop done with a function
def for_loop(sequence, index=0):
    print(sequence[index])
    index += 1
    if index == len(sequence):
        # returning once we've hit the end of the list
        return
    for_loop(sequence, index)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
for_loop(colors)

# Lambda functions
# lambda functions are a way to write short, sometimes one-off functions that can fit in one line
# function_name = lamba arguments: return value
multiply = lambda x, y: x * y
print(multiply(2, 3))

def multiply(x, y):
    return x * y

# *args
sum([1, 2, 3]) # 6
def sum(*args):
    print(args) # (1, 2, 3, 4, 5)
    total = 0
    for number in args:
        total += number
    return total
print(sum(1, 2, 3, 4, 5))

# define function that adds 2 numbers

# x and y are the parameters
def add(x, y):
    """given numbers x and y, returns their sum"""
    return x + y

# 4 and 7 are the arguments
result = add(4, 7)

print(result)

# function that doesn't take parameters:
def gimme3():
    return 3

result = gimme3()

print(result)

# a function with no return AND an optional agument (role)
def staff_bio(first_name, last_name, role='instructor'):
    message = f'{first_name} {last_name} works at PDX Code Guild as an {role}.'
    print(message)

# passing by postiion
# the arguments are passed in the order in which
# they are expected as parameters
staff_bio('Pete', 'Jones')

# passing keyword arguments
# keyword arguments will look like parameter=value
staff_bio(last_name='Burrow', first_name='Danny')

staff_bio('Mitch', 'Chapman', 'TA')

# Implicit Return
# every function returns something
# if there is no return line, the function will just
# return None
return_from_staff_bio = staff_bio('Matt', role='TA', last_name='Walsh')
print(return_from_staff_bio)

# Returning Multiple Values
def get_dimensions():
    return 500, 200
# tuple unpacking
width, height = get_dimensions()
print(width)
print(height)

dimensions = get_dimensions()
print(dimensions)
print(dimensions[0], dimensions[1])

# Recursion
i = 0
def crash_python():
    # you can use the global keyword
    # to indicate that you are refering
    # to a variable outside the scope
    # of the function
    global i
    print(i)
    i += 1
    crash_python()

# crash_python() # RecursionError: maximum recursion depth exceeded while calling a Python object

# lambda functions
# lambda functions are one-line functions with a special syntax

# function_name = lambda parameters: return value

def multiply(x, y):
    return x * y

multiply = lambda x, y: x * y

result = multiply(3, 7)
print(result)

# *args
# *args as function parameters let you pass in 0, 1 or any number of additional arguments
def sum(*args):
    # print(args) # (1, 2, 3)
    total = 0
    for arg in args:
        total += arg
        # print(arg)
    return total


total = sum(1, 2, 3, 4, 5)
print(total)


# print is an example of a built-in function that takes *args
# print(1, 2, 3, 4, 5, 'hello', 'goodbye', {'key': 'value'})
# x = 6
# print(x)
# # there is a built-in id function which takes in an object
# # and returns the integer id of that objec
# print(id(x))
# print(id(6))

# # Types
# # there i a built-in type funtion, which takes in an object
# # and returns the type of that object
# print(type(x)) # <class 'int'>
# y = '7'
# print(type(y)) # <class 'str'>
# # z = x + y # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# hot_outside = True
# print(type(hot_outside)) # <class 'bool'>
# w = 0.435
# print(type(w)) # <class 'float'>
# z = w + x
# print(z) # 6.435
# print(type(z))

# teacher = {'name': 'Pete', 'role': 'instructor'}
# print(type(teacher)) # <class 'dict'>

# numbers = [5, 4, 3, 2, 1]
# print(type(numbers)) # <class 'list'>

# print(type(print)) # <class 'builtin_function_or_method'>

def add(x, y):
    return x + y

# print(type(add)) # <class 'function'>

# class_name = 'Class Orchid'
# print(type(f'Welcome to {class_name}!')) # <class 'str'>

# # Literals
# message1 = "It's Python Time!"
# message2 = input('What time is it? ')
# print()
# print('message1 is a string literal,\nit was literally typed into the source code,\nand will always be the same as long as the code stays the same')
# print(message1)
# print()
# print('message2 is not a literal,\nit is whatever the user types in,\nand could be different every time the code runs,\neven if the source code stays the same')
# print(message2)

# # Type Conversion
# print(add(2,3))
# x = input('welcome to the adding calculator please enter number 1: ')
# y = input('please enter number 2: ')
# z = x + y

# print(f'the sum of {x} and {y} is {z}') # given x = 5 and y = 7, this one says z is 57 because x and y are both strings (they are concatenated)
# x = int(x) # x is now an integer
# y = int(y) # y is now an integer
# z = x + y
# print(f'the sum of {x} and {y} is {z}') # now we will get 12, because x and y are both integers

# Mutability
# strings are immutable
message = 'hello world'
print(message, id(message))
message += '!' # same thing as message = message + '!'
print(message, id(message))

# lists are mutable
colors = ['red', 'green', 'blue', 'yellow']
print(colors, id(colors))
colors.append('orange')
print(colors, id(colors))

# using the time library to delay output
import time
print('Why does the python live on land?')
time.sleep(3) # the script will wait 3 seconds
print("Because it's above C-level")
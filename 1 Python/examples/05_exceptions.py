"""Compilation Errors"""
"""SyntaxError"""
# print('hello world)
# SyntaxError: EOL while scanning string literal
# EOL: end of line.  It was expecting the string to close off before the line ended

# print('hello world'
# SyntaxError: unexpected EOF while parsing
# EOF: End of file.  The parentheses need to close before the file ends

"""IndentationError"""
# weather = 'pleasant'
# if weather == 'pleasant':
# print('go outside')
# IndentationError: expected an indented block
# if the previous line ends with a :, the next line must be indented

# def say_hello():
# print('say hello')
# IndentationError: expected an indented block

# print('hello')
#     print('goodbye')
# IndentationError: unexpected indent
# If there is no : at the end of the previous line, a line should
# not be indented

"""Runtime Errors"""
"""NameError"""
# A variable you are referencing is not defined
# sentence1 = 'Python is cool 🐍'
# sentence3 = 'JavaScript is pretty cool too ☕️'
# print(sentence1)
# print(sentence2) # NameError: name 'sentence2' is not defined
# print(sentence3)

"""AttributeError"""
# Given an object, you can access that objects attributes and methods with dot notation:
# for example list.append will add an item to a list
# string.capitlize will return a capitalized version of that string
# If that attribute or method is something the object doesn't have, an AttributeError will be raised

# name = 'pete' # name is a string
# tas = ['matt', 'mitch'] # tas is a list
# tas.append('lisa') # lisa joins the class, we can append her string to the list
# print(tas)
# name.append('jones') # AttributeError: 'str' object has no attribute 'append'
# append is a list method.  Strings do not have an append attribute.
# print(name.capitalize())


"""TypeError"""
# a TypeError occurs when the operation you are trying to perform on an object
# is not something that that object can do.  A basic example is adding integers and strings together

# print(1 + '1') # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# numbers = [2, 6, 8, 1, 9]
# for number in numbers:
#     print(number)

# for i in range(len(numbers)):
#     print(i, number[i]) # TypeError: 'int' object is not subscriptable

# x = 45
# print(x[3])# TypeError: 'int' object is not subscriptable

# x = 4.5
# print(x[2]) # TypeError: 'float' object is not subscriptable

# len(123) # TypeError: object of type 'int' has no len()

# for i in range('banana'): # TypeError: 'str' object cannot be interpreted as an integer
#     print(i) 

"""IndexError"""
# an IndexError occurs when an number that is too large (there are not that many elements in the list)
# is put in brackets: [x] after a list
# colors = ['red', 'green', 'yellow']
# # print(colors[-1]) # -1 gives the last item in the list
# for i in range(4):
#     print(f'index: {i}')
#     print(f'color: {colors[i]}') # IndexError: list index out of range (when i was 4)
#     print()


"""KeyError"""
# A KeyError is raised when attempting to access a value from a dictionary with a key that doesn't exist
# plant = {
#     'leaves': 'green',
#     'height(in)': 6,
#     'pot': 'clay'
# }

# print(plant['leaves'])
# print(plant['pot'])
# print(plant.get('latin_name')) # This was None, did not raise an error.  dict.get is not going to cause
# # an error if the key is not in the dictionary
# print(plant['latin_name']) # KeyError: 'latin_name'


"""ValueError"""
# print(int('hotdog')) # ValueError: invalid literal for int() with base 10: 'hotdog'
# import math
# print(math.sqrt(-1)) # ValueError: math domain error


"""raising errors"""
# for i in range(20):
#     if i == 13:
#         raise ValueError('13 is unlucky')
#     print(i)



for i in range(20):
    try: # this is going "try" to run the code in the indented block
        # test = not_variable # NameError: name 'not_variable' is not defined
        if i == 7:
            raise ValueError('number is too lucky')
        if i == 13:
            raise ValueError('unlucky number')
        print(i)
    except ValueError as e: # the indented block in except ValueError: will only run in the case
        # of a ValueError
        # other errors can be handled in their own except blocks, even in a generic one
        # print('unlucky number') # hard coded
        print(e) # modular: says whatever the ValueError message is as definied above
    except:
        print('something went wrong')
    # finally: # you can addd a finally: at the end of a try/except chain, this code will run
    # whether or not any exceptions are raised
    #     print('this runs every single time')

# a try: needs an except:
# the following would cause a SyntaxError
# try:
#     print('something')
        
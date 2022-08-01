# String Literals
# a "literal" is when an object (like a string) is written
# into the source code

message = 'hello world' # a string literal declared

def capitalize(s: str): # this could potentially take in a string
    # not from the source code
    return s.capitalize()

# strings can be defined in multiple ways
# single quotes
sentence = 'Welome to strings in Python!'

# double quotes
sentence = "Welcome to strings in Python!"

# multi-line strings/comments
# these strings can include line breaks
sentence = """
Dear Student,

    You are humbly welcome to learn strings.

With Regards,
––The Instructor

P.S.: Strings, in Python, that is
"""

print(sentence)

# if you need to use quotes inside a string, there a are a couple different ways
print('You can use "double quotes" inside of single quotes')

print("You can use 'single quotes' inside of single quotes")

# you can also use escape characters for quotes (and other things)

# to use single/double quotes without breaking the string,
# you can put a backslash (\) before the quote

print('You can use \'escape characters\' to put single quotes in a string without breaking it')
print("You can use \"escape characters\" to put double quotes in a string without breaking it")

# \n will give a new line
# \t will give a tab
print('\n\tWelcome to String Town\n\nWe have strings for everyone!\n')
#
# 	Welcome to String Town

# We have strings for everyone!
# 

# unicode characters
print('\u0394') # Δ
print('\u3965') # 㥥
print('\u1234') # ሴ
print('\u2700') # ✀
print('\u3542') # 㕂
print('\u0001') # whitespace
print('\u1997') # ᦗ
print('\u1987') # ᦇ
print('\u2002') # whitespace
print('\u12345') # ሴ5
print('\u0000')
print('\u9999') # 香

# raw strings
# prefix a string with r, and it will ignore any escape sequences
print(r'\n\thello\u\\\\\\\\') # \n\thello\u\\\\\\\\


# Ascii Codes:
# ord takes in a one-character string, returns its ascii code
print(ord('A')) # 65

# chr takes in an ascii code as integer, and returns the character for that code
print(chr(66)) # B

for i in range(200):
    print(f'ASCII Code: {i}: {chr(i)}')


# concatenation
# use the + operator to 'add' or combine strings

word1 = 'hello '
word2 = 'world'

message = word1 + ' ' + word2
print(message) # hello world

# due to type restrictions, you can't contcatenate non-string objects to strings
# message = 'my favorite number is ' + 13 # TypeError: can only concatenate str (not "int") to str

# however, you can use fstrings to do things like puttting a number into a string
message = f'my favorite number is {13}'
print(message)

# multiplication
jacks_manuscript = 'All work and no play makes Jack a dull boy.  ' * 30
print(jacks_manuscript)

# I like to use this if I am debugging, and there is already a lot of text
# and I want someting important to stick out
important_variable = 'THIS IS VERY IMPORTANT'


print('*' * 40)
print(important_variable)
print('*' * 40)

# building up a string

message = ''
words = ['strings', 'are', 'fun', 'to', 'use']
print(words) # ['strings', 'are', 'fun', 'to', 'use']

for word in words:
    message += word + ' '

print(message)

# you can use len for a string just the way you could for a list

print(len(words)) # 5 (5 elements in the list)
print(len(message)) # 23 (23 characters in the string)

# access string[index]
# works similarly to lists, but gives you the character
# instead of the element
print(message[2]) # r (the character at index 2 in the string)

# String Methods

print('message id:', id(message))

# string.find(substring)
# similar to list.index(element)
index = message.find('r')
print(index) # 2

# you can use this on substrings, not just individual characters
index = message.find('fun')
print(index) # 12

# string methods that return new strings
new_message = message.title()
print(message) # strings are fun to use
print(new_message) # Strings Are Fun To Use

new_message = message.upper()
print(message) # strings are fun to use
print(new_message) # STRINGS ARE FUN TO USE

print('message id:', id(message))

# if you want to change the variable that you're using for
# the string method, you'll have to re-assign it:
message = message.upper() # this actually re-assings the variable message
print(message) # STRINGS ARE FUN TO USE

print('message id:', id(message))


# Getting a string out of a list, and vice-versa

# mini lab: Take a sentence and turn it into a slug.

sentence = 'One of my plants needs to be watered.'
# goal is this: 'one-of-my-plants-needs-to-be-watered'

# string.split(delimiter)
print(sentence.split(' ')) # ['One', 'of', 'my', 'plants', 'needs', 'to', 'be', 'watered.']
print(sentence.split('n')) # ['O', 'e of my pla', 'ts ', 'eeds to be watered.']

# string.split(delimiter) will break up the string
# on the delimiter (also a string) passed in as an argument
# it will return a new list, where the elements are the parts
# of the string in between the delimiter

# if you pass no argument, it will split on all whitespace
words = sentence.split()
print(words) # ['One', 'of', 'my', 'plants', 'needs', 'to', 'be', 'watered.']

# for i in range(len(words)):
#     words[i] = words[i].upper()
# print(words)

# for i, word in enumerate(words):
#     words[i] = word.upper() # make sure to change the list, not just the loop variable!

# print(words)


for i, word in enumerate(words):
    # do our string manipulation to word
    word = word.lower() # making word lowercase
    word = word.strip('.') # removing periods from start/end of word

    # change the list
    words[i] = word


slug = '-'.join(words)
print(slug) # one-of-my-plants-needs-to-be-watered

# pete's unnoficial version that doesn't exist/work
# words.join('-') # this is not a thing in python 😭


# string.strip(another_string)
# sting.strip will remove matching characters from the
# beginning and end of a string

message = '-------here is the important part----------------------'
print(message.strip('-')) # here is the important part

# with no arguments, string.strip will trim all leading/trailing whitespace

message = """


    stuff

more stuff
        this thing
the end
        
            
    """

print(message)
print('*'*40)
print(message.strip())

message = ')(*&^%$^%$%^&here is the message*#&#*%(@$%^'

# given multiple characters, will remove all from
# start/end of string in any order
print(message.strip('!@#$%^&*()~_+')) # here is the message

# docstrings
# docstrings are used for notation in python
# they are multiline strings used as documentation
# directly in the source code
# for example, you can include them inside functions

def add(x, y):
    """given numbers, x and y, returns their sum"""
    return x + y

result = add(3, 5)
print(result)

# the string library/module

import string

print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits) # 0123456789
print(string.punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

message = ')(*&^%$^%$%^&here is the message*#&#*%(@$%^'
print(message.strip(string.punctuation)) # here is the message

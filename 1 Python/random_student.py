"""Prints the name of a student to be called on."""

import random

students = [
    'cesar',   # 0
    'christa', # 1
    'jason',   # 2
    'jen',
    'jordyn',
    'luis',
    'mileidy',
    'patrick',
    'rob',
    'teyon',
    'tony',
    'vel',    # 11
] # PEP8 styling guidelines recommend a trailing comma for multiline lists

# print(random.randint(0, len(students) - 1)) # evaluates down a number in the range 0-11
name = students[random.randint(0, len(students) - 1)] # puts that index (0-11) into the list
print(name)

# name = random.choice(students)
# print(name)

# print(random.random()) # random float between 0 and 1
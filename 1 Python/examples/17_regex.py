"""
Regular Expressions, or regex, is a way of searching through a set of text 
for any matching criteria. The regex is how you define the criteria. 

Use https://regexr.com/
to write and validate regex, and for helpful cheat sheets 
and more in-depth documentation 
"""

# the python module for using regex 
import re


# the string we're going to search in
test_str = """
Danny: +1 503-208-1234, instructor
Matt: 987-432-1893, TA
Mitch: +153 9381391937, TA
"""

# the regular expression
expression = r'(\+\d{1,4}\s)?(\d{3}-?\d{3}-?\d{4})'

# Find all: re.findall() searches the string for ALL instances that match the regular expression
match = re.findall(expression, test_str)

# It returns a list of tuples
print(match) #[('+1 ', '503-208-1234'), ('', '987-432-1893'), ('+153 ', '9381391937')]
# One tuple for each "capturing group"
# Capturing groups are defined by () in the expression we wrote

# The first capturing group is for the country codes
# We made this optional with a ?, so sometimes this is an exmpty string
for m in match:
    print(m[0]) 
    ''' 
    +1 

    +153 
    '''

# The second capturing group is for the phone number without country code
for m in match:
    print(m[1])
    '''
    503-208-1234
    987-432-1893
    9381391937
    '''
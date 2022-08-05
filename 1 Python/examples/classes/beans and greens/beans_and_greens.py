# All python files are "modules" and you can import local ones just like you can import anything else
import beans
import greens

# Methods and attributes with __ before and after the names are special
# They are called "dunder" methods (for double underscore) or magic methods

# The __name__ attribute is set by python when a module is called
# When the file is called directly, it's set as __main__
print(f"The beans and greens filename is set to {__name__}")

print("this is the best dish on earth")
# The functions defined in these files are now available here as methods on those modules
beans.dans_opinion()
greens.dans_opinion()


# __str__ is a common example of a dunder attribute
# Everything has a __str__ attribute that defines what happens if that thing
# needs to be represented as a string (even if it's not a string)
# These ones are the default ones set by python

print(beans) # <module 'beans' from '/home/dan/code-guild/class_orchid/1 Python/examples/classes/beans and greens/beans.py'>
print(beans.dans_opinion) # <function dans_opinion at 0x7f83b7c86440>


# When the _io module was written, the authors overwrote the __str__ attribute of the object
# to give users more specific information than the default
filepath = '1 Python/examples/data/cities.csv'
with open(filepath, 'r') as f:
    print(f) # <_io.TextIOWrapper name='1 Python/examples/data/cities.csv' mode='r' encoding='UTF-8'>

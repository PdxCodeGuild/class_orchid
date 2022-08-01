"""Tuples"""
# tuples are similar to lists but are immutable
# they cannot be changed after they are first defined

list_of_numbers = [1, 2, 3, 4, 5]
print(list_of_numbers)

list_of_numbers.append(6)
print(list_of_numbers)

# tuples use () instead of []
tuple_of_numbers = (1, 2, 3, 4, 5)
tuple_of_numbers = (1, 2, 3, 4, 5, 6)
# tuple_of_numbers.append(6) # AttributeError: 'tuple' object has no attribute 'append'
print(tuple_of_numbers.count(3)) # you can't .apppend to a tuple, but you can .count 

colors = ['red', 'green', 'blue']
# for i, color in enumerate(colors):
for enum_tuple in enumerate(colors):
    print(enum_tuple)
# (0, 'red')
# (1, 'green')
# (2, 'blue')

# tuple unpacking
info = ('Pete', 'instructor', 'fountains')
name, role, decorations = info
print(name, role, decorations)

# tuple literals with only one element
# need a trailing comma to distinguish
# them from just being in parentheses
# for order of operations
float_tuples = (3.14,)
print(float_tuples, type(float_tuples))

# empty tuples just need ()
empty_tup = ()
print(empty_tup)



"""Sets"""
# sets are list-like objects with special properties
# they are filled with values which are unique from one another
# they are unordered (run this program more than once and letters will be
# in different orders)
letters = {'a', 'b', 'c', 'b', 'a', 'd', 'z', 'q', 'f', 'f', 'z', 'x'}
print(letters) # {'c', 'b', 'x', 'z', 'd', 'f', 'q', 'a'}
# sets can only have immutable values: this would cause an error
# error_set = {1, 2, 3, 'hello', 'goodbye', [1, 2, 3], {'a': 1}} # TypeError: unhashable type: 'list'

# sets have some interesting methods

colors1 = {'red', 'blue', 'orange', 'purple'}
colors2 = {'green', 'red', 'orange', 'yellow'}

# set.union(other_set) will return a new set
# with values from boths sets
all_colors = colors1.union(colors2)
print(all_colors) # {'purple', 'orange', 'blue', 'red', 'yellow', 'green'}

colors_difference = colors1.difference(colors2)
print(colors_difference) # {'purple', 'blue'}

colors_intersection = colors1.intersection(colors2)
print(colors_intersection) # {'red', 'orange'}
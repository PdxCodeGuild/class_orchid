###############################
#                             #
#  PART 1:                    #
#  Global vs Local variables  #
#                             #
#  Scope & Parameters         #
#                             #
###############################

""" 
a = 2

def scope_test():
    a = 1

scope_test()
print(a)
 """

# in short, scope is the concept of "as far as Python can tell, where does this variable exist?"
# a GLOBAL variable is "globally" available - it exists everywhere after it has been declared
# a LOCAL variable only exists within a specific section of your code
# functions can see GLOBAL variables, but a variable assigned within a function is LOCAL

""" 
a = 2

def scope_test():
    print(a)
    a = 1

scope_test()
print(a)
 """

# this will trigger an UnboundLocalError exception
# by declaring the variable inside the function (even though it's after the print statement), you have told the function that "a" is a LOCAL variable

""" 
def scope_test():
    a = 1

scope_test()
print(a)
 """

# this will also trigger an UnboundLocalError exception since "a" doesn't exist globally, but it is called globally in the print

""" 
a = 2
b = 1

def add_things():
    a = a + b
    print(a)

add_things()
 """

# UnboundLocalError: local variable 'a' referenced before assignment
#
# variable 'a' is a GLOBAL variable - available to the entire app
# a = tells the function that you want to make a LOCAL variable named 'a'
# the function now sees 'a' as a local variable, and ignores the global variable
# because of this, the 'a' in 'a + b' hasn't been declared yet
#
# both of these would work:
#     c = a + b
#     print(c)
# 
# 
#     print(a + b)
# 
# but there's a better way:
# 
# a = 2
# b = 1
# 
# def add_things(a,b):
#     a = a + b
#     print(a)
# 
# add_things(a,b)
# 
# this is the same thing:
# 
# num1 = 2
# num2 = 1
# 
# def add_things(a,b):
#     a = a + b
#     print(a)
# 
# add_things(num1,num2)

""" 
def list_test(a_list):
    a_list.pop()
    print(a_list)

def string_test(a_string):
    a_string += "!!!"
    print(a_string)

def int_test(an_int):
    an_int += 1
    print(an_int)

def dict_test(a_dict):
    a_dict['test'] = 'Hello world'
    print(a_dict)

test_list = [1,2,3,4]

test_string = "Hello"

test_int = 1

test_dict = {'key_1':'value 1'}

print('\nLists:')
print(f'before: {test_list}')
list_test(test_list)
print(f'after: {test_list}')

print('\nStrings:')
print(f'before: {test_string}')
string_test(test_string)
print(f'after: {test_string}')

print('\nInts:')
print(f'before: {test_int}')
int_test(test_int)
print(f'after: {test_int}')

print('\nDicts:')
print(f'before: {test_dict}')
dict_test(test_dict)
print(f'after: {test_dict}')
 """

# note that functions WILL modify the original variable (even when passed as a parameter) if that variable's type is mutable
# lists, dictionaries, and sets are mutable
# strings, integers, floats, booleans, and tuples are immutable
# 
# there are ways to get around modifying mutable variables, but that's outside the scope of what we're talking about today


###############################
#                             #
#  PART 2:                    #
#  Reusability                #
#                             #
#  Parameters (again)         #
#                             #
###############################

""" 
cc_nums = [
    [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5],
    [5, 7, 5, 6, 7, 3, 2, 4, 9, 8, 1, 0, 9, 5, 2, 6],
    [4, 6, 1, 8, 4, 9, 6, 7, 8, 0, 2, 4, 1, 5, 3, 5],
]

def cc_validate():
    check_digit = cc_num.pop()
    if check_digit == 5:
        print('valid')
    else:
        print('invalid')

cc_validate()
 """

# this is a key for why you pass parameters instead of using GLOBAL variables
# with parameters, you can reuse a function over and over again in similar situations

###############################
#                             #
#  PART 3:                    #
#  Function Output            #
#                             #
#  Return instead of print    #
#                             #
###############################

""" 
cc_num = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]
your_balance = 2000
matt_balance = 0

def cc_validate():
    check_digit = cc_num.pop()
    if check_digit == 5:
        print('valid')
    else:
        print('invalid')

def cc_process():
    if cc_validate() == 'valid':
        your_balance -= 1000
        matt_balance += 1000
        print('You have successfully given Matt $1000. Thank you.')
    else:
        print('Your card could not be processeed.')
        

cc_validate()
cc_process()
# print(matt_balance)
 """

# returning from a function (rather than printing for example) lets you use the data from the function elsewhere
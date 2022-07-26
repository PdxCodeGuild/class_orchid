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
cc_num = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]

def cc_validate():
    check_digit = cc_num.pop()
    if check_digit == 5:
        print('valid')
    else:
        print('invalid')

cc_validate()
print(cc_num)
 """

# because lists are mutable, their methods work without variable assignment (i.e. .append() and .pop() work without variable_name = before them)
# due to mutability, you can modify a GLOBAL variable list inside of a function without triggering an UnboundLocalError exception
# while this may be desired in rare cases, it is usually not what you want to do
# 
cc_num = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]

def cc_validate(cc):
    check_digit = cc.pop()
    if check_digit == 5:
        print('valid')
    else:
        print('invalid')

print(cc_num)
cc_validate(cc_num)
print(cc_num)


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
# print(cc_num)
# print(matt_balance)
 """
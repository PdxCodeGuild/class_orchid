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
    print(a)
    a = 1

scope_test()
print(a)
 """
""" 
num_1 = 2
num_2 = 1

num_3 = 5
num_4 = 7

def add_things(first_num,second_num):
    first_num = first_num + second_num
    print(first_num)

add_things(first_num=num_1,second_num=num_2)
add_things(num_3,num_4)
 """
""" 
a = 2
b = 1

def add_things():
    a = a + b
    print(a)

add_things()
 """
""" 
a = 1

def scope_test():
    a = 2

scope_test()

print(a)
 """
""" 
def string_test(a_string):
    a_string += "!!!"
    print(a_string)

test_string = "Hello"

print('\nStrings:')
print(f'before: {test_string}')
string_test(test_string)
print(f'after: {test_string}')
 """
""" 
def list_test(a_list):
    a_list.pop()
    print(a_list)

test_list = [1,2,3,4]

print('\nLists:')
print(f'before: {test_list}')
list_test(test_list)
print(f'after: {test_list}')
 """





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
# cc_num = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]

def cc_validate(cc):
    check_digit = cc.pop()
    if check_digit == 5:
        print('valid')
    else:
        print('invalid')

for card in cc_nums:
    cc_validate(card)
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

def cc_validate(cc):
    check_digit = cc.pop()
    if check_digit == 5:
        return 'valid'
    else:
        return'invalid'

def cc_process(cc_valid,your_balance,matt_balance):

    if cc_valid == 'valid':
        your_balance -= 1000
        matt_balance += 1000
        print('You have successfully given Matt $1000. Thank you.')
        return your_balance, matt_balance
    else:
        print('Your card could not be processeed.')
        return your_balance, matt_balance
        

is_cc_valid = cc_validate(cc_num)



your_balance, matt_balance = cc_process(is_cc_valid,your_balance,matt_balance)


print(matt_balance)
 """


cc_num = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]
your_balance = 2000
matt_balance = 0

def cc_validate(cc):
    check_digit = cc.pop()
    if check_digit == 5:
        return True
    else:
        return False

def cc_process(cc_valid,from_account,to_account):

    if cc_valid:
        from_account -= 1000
        to_account += 1000
        print('You have successfully given Matt $1000. Thank you.')
        return from_account, to_account
    else:
        print('Your card could not be processeed.')
        return from_account, to_account
        

# is_cc_valid = cc_validate(cc_num)



your_balance, matt_balance = cc_process(cc_validate(cc_num),your_balance,matt_balance)


print(matt_balance)
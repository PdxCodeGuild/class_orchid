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
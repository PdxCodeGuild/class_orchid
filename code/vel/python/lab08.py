"""
Lab 08: Credit Card Validation
"""

"""
write a function that returns wherther a string containing a credit card number is valid as a boolean (Truthy / Falsey?)
    covert the input string into a list of ints (list_of_ints = input("...")) then maybe list_of_ints = int(list_of_ints) for loop that typecast input into int
    
    slice off the last digit, this is the check digit lets do .pop storing that digit into the check_digit variable that i will then put into my function...
    
    reverse the digits reverse(cards_numbers) (im assuming I have to assign the reversed list to a new varible) () .....python list method on w3 school
    
    double every other element in the reversed list ( reversed_list[ :2:] * 2 ) ?

    subtract nine from numbers over 9 (maybe while number in reveresed_list is < 9 - 9 from number?)   maybe if statement works too

    sum all values ( for number in reversed_list, sum = 0, sum += number) ???

    take the second digit of that sum (sum[1] then i put that into my function to check if its true or not, % 10 could be a start.
"""

def validation(check_digit,ones_digit):
    ones_digit = ones_digit % 10
    if check_digit == ones_digit:
        return 'Valid!'
    else:
        return 'Invalid!'

sum_of_input = 0

credit_card = list(input('Enter your credit card number here: '))

for index in range(len(credit_card)): # using the range function to go the length of the users input "credit_card"
    credit_card[index] = int(credit_card[index])

check_digit = credit_card.pop(-1)
credit_card.reverse()

for i, n in enumerate(credit_card): # 
    if i % 2 == 0: # im checking for even numbers to double which is why i % 2 makes sense because there is no remainder with even numbers so it == 0 always
        credit_card[i] = credit_card[i] * 2 # then doubling it at the even indicies 


for index in range(len(credit_card)):
    if credit_card[index] > 9:
        credit_card[index] = credit_card[index] - 9

for num in credit_card: 
    sum_of_input += num

print(validation(check_digit, sum_of_input)) # functions only have access to data that we pass into them



    
    










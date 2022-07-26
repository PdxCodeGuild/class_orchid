import random

card_digits = []

card_number = input('Please enter your your card number: ')

for num in card_number:
    int_card_number = int(num)

    card_digits.append(int_card_number)

check_digit = card_digits.pop()

card_digits.reverse()

for index in range(len(card_digits)):
    print(card_digits[index])
    if index % 2 == 0:
        card_digits[index] *= 2
        if card_digits[index] > 9:
            card_digits[index] -= 9

total = sum(card_digits)

second_digits =  total % 10 

if second_digits == check_digit:
    print('Valid!')

else:
    print('Not valid.')


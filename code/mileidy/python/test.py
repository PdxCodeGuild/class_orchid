
def splice():

    card_digits = []

    card_number = input('Please enter your 15 digit card number: ')

    card_number = int(card_number)

    card_digits.append(card_number)

    return card_digits[0::15]

    print(f'{card_digits}')

splice()
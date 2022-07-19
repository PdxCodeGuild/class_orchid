roman_numerals = {
    '1' : 'I',
    '2' : 'II',
    '3' : 'III',
    '4' : 'IV',
    '5' : 'V',
    '6' : 'VI',
    '7' : 'VII',
    '8' : 'VIII',
    '9' : 'IX',
    '0' : 'X',
    '11-20' : 'X',
    '21-30' : 'XX',
    '31-39' : 'XXX',
    '40-49' : 'XL',
    '50-60' : 'L',
    '60-70' : 'LX',
    '71-80' : 'LXX',
    '80-89' : 'LXXX',
    '90-99' : 'XC',
    '100' : 'C',
}

def get_number():
    number = input('Enter a number 1-100 (or press "enter" to exit): ')
    is_number = False

    while not is_number:
        if number.isnumeric():
            is_number = True
        elif number == '':
            return number
        else:
            print('That was not a number. Try again!')
            number = input('Enter a number 1-100 (or press "enter" to exit): ')
    

    return number

num = get_number()

def numbers_1_to_10(one):
    print(f'{roman_numerals[str(one)]}')

def numbers_11_to_20():
    print(f'{roman_numerals["11-20"]}', end='')

def numbers_21_to_20():
    print(f'{roman_numerals["21-30"]}', end='')

def numbers_31_to_39():
    print(f'{roman_numerals["31-39"]}', end='')

def numbers_40_to_49():
    print(f'{roman_numerals["40-49"]}', end='')

def numbers_50_to_60():
    print(f'{roman_numerals["50-60"]}', end='')

def numbers_60_to_70():
    print(f'{roman_numerals["60-70"]}', end='')

def numbers_71_to_80():
    print(f'{roman_numerals["71-80"]}', end='')

def numbers_80_to_89():
    print(f'{roman_numerals["80-89"]}', end='')

def numbers_90_to_99():
    print(f'{roman_numerals["90-99"]}', end='')



while num != '':
    num = int(num)
    ones = num % 10
    tens = num // 10

    print(f'{num} in roman numerals is : ', end='')

    
    if num > 0 and num < 101:
        if num == 100:
            print(f'{roman_numerals["100"]}')
        elif num > 89 and num <= 99:
            numbers_90_to_99()
        elif num > 80 and num <= 89:
            numbers_80_to_89()
        elif num > 70 and num <= 80:
            numbers_71_to_80()
        elif num > 60 and num <= 70:
            numbers_60_to_70()
        elif num > 49 and num <= 60:
            numbers_50_to_60()
        elif num > 39 and num <= 49:
            numbers_40_to_49()
        elif num > 30 and num <= 39:
            numbers_31_to_39()
        elif num > 20 and num <= 30:
            numbers_21_to_20()
        elif num >= 11 and num <= 20:
            numbers_11_to_20()

        if num != 40 and num != 50 and num != 90 and num != 100:
            numbers_1_to_10(ones)
        
    elif num < 1 or num > 100:
        print('Number was not within 1-100')
    
    num = get_number()

print('bye.')
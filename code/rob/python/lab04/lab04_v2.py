words = {
    '0' : '',
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine',
    '10' : 'ten',
    '11' : 'eleven',
    '12' : 'twelve',
    '13' : 'thirteen',
    '15' : 'fifteen',
    '20' : 'twenty',
    '30' : 'thirty',
    '40' : 'forty',
    '50' : 'fifty',
    '60' : 'sixty',
    '70' : 'seventy',
    '80' : 'eighty',
    '90' : 'ninety',
    't' : 'teen',
    'h' : 'hundred',
}

while True:
    num = int(input('Enter a number 0-99 or Ctrl+C to exit: '))

    hundreds_digit = str(num // 100)
    tens_digit = str((num // 10) % 10)
    ones_digit = str(num % 10)
    
    hundred = ''
    hundred_words = ''
    counter_tens = 1

    #add hundred before tens place if num > 99
    if int(hundreds_digit) >= 1:
        hundred = words['h']
        hundred_words = f'{words[hundreds_digit]} {hundred} '
        if int(tens_digit) == 0 and int(ones_digit) == 0:
            print(f'{num} in words is: ' + hundred_words)
            
    if int(hundreds_digit) == 0:
        hundred_words = ''
    
    #1-9
    if int(tens_digit) == 0 and (int(ones_digit) >= 0 and int(ones_digit) <= 9 and int(ones_digit) != 0):
            print(f'{num} in words is: ' + hundred_words + words[ones_digit])
    
    #10, 11, 12, 13, 15
    if int(tens_digit) == 1 and (int(ones_digit) == 0 or int(ones_digit) == 1 or int(ones_digit) == 2 or int(ones_digit) == 3 or int(ones_digit) == 5):
            print(f'{num} in words is: ' + hundred_words +  words[tens_digit + ones_digit])
    
    #teens
    if int(tens_digit) == 1 and (int(ones_digit) != 0 and int(ones_digit) != 1 and int(ones_digit) != 2 and int(ones_digit) != 3 and int(ones_digit) != 5):
            print(f'{num} in words is: ' + hundred_words +  words[ones_digit] + words['t'])
    
    #20-99
    if int(tens_digit) >= 2:
        while True:
            if int(tens_digit) == counter_tens and (int(ones_digit) >= 0 and int(ones_digit) <= 9):
                if int(ones_digit) == 0:
                     print(f'{num} in words is: ' + hundred_words +  words[tens_digit + '0'])
                else:
                    print(f'{num} in words is: ' + hundred_words +  words[tens_digit + '0'] + '-' + words[ones_digit])
                break
            counter_tens += 1
    
    #0
    elif int(hundreds_digit) == 0 and int(tens_digit) == 0 and int(ones_digit) == 0:
        print(f'{num} in words is: zero')
# Created a dictionary that holds 0-9 along with the word the corresponds to each numbers
worded_ones_digits = {
    0: '',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine'
}

# Created a dictionary that holds 10-19 along with the word the corresponds to each numbers
worded_teens = {
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    14: 'Fourteen',
    15: 'Fifteen',
    16: 'Sixteen',
    17: 'Seventeen',
    18: 'Eighteen',
    19: 'Nineteen'
}

# Created a dictionary that holds 20-90 worded ten digits along with the word the corresponds to each numbers
worded_tens_digits = {
    2: 'Twenty',
    3: 'Thirty',
    4: 'Forty',
    5: 'Fifty',
    6: 'Sixty',
    7: 'Seventy',
    8: 'Eighty',
    9: 'Ninety'
}

# Created a dictionary that holds hundreds words for 100-900 worded ten digits along 
# with the word the corresponds to each numbers
worded_hundreds_digits = {
    1: 'One Hundred',
    2: 'Two Hundred',
    3: 'Three Hundred',
    4: 'Four Hundred',
    5: 'Five Hundred',
    6: 'Six Hundred',
    7: 'Seven Hundred',
    8: 'Eight Hundred',
    9: 'Nine Hundred'
}

# Ask the user to input a number between 0 and 99
digit = input("\nEnter a number between 0-999: ")

# Converts the string input from the variable digit from a string into a integer
digit = int(digit)

hundreds_digit = digit // 100

# Uses modulo to get the remainder of the number that was input
ones_digit = digit % 10

# Uses floor division and modulo to isolate the number in the tens place within a 2 digit number
# to determine the number from the worded_tens dictionary
ten_digit = digit // 10 % 10

# Isolated the number in the tens place withing a 3 digit number to determine the number from the worded_tens
# dictionary
hundreds_ten_digit = digit // 10 % 10

# Isolates the tens and ones place to identify what teen number from the teens dictionary.
teens_modulo = digit % 100

# Create a teens digit to represent any number in the teens that is types in 
teens_digit = digit

# Created an if statements that prints 'zero' when the user type 0
if digit == 0:
    print("zero")

## if statement that determines if a digit is over 100 and the tens place is equal to zero
#  this determines the number in the ones place inside a 3 digit number from the ones_dictionary  
if digit >= 100 and hundreds_ten_digit == 0:
    #created a variable called hundreds_word to indicate which word in the 100's dictionary is to be used
    hundreds_word = worded_hundreds_digits[hundreds_digit]
    #created a variable called ones_word to indicate which word in the ones dictionary is to be used
    ones_word = worded_ones_digits[ones_digit]
    #print the outcome
    print(f"{hundreds_word} {ones_word}")

## if statement that determines if a digit is over 100 and if the tens place is equal to one,
#  this determines the teen number inside a 3 digit number from the teens dictionary.
elif digit >= 100 and hundreds_ten_digit == 1:
    #created a variable called hundreds_word to indicate which word in the 100's dictionary is to be used
    hundreds_word = worded_hundreds_digits[hundreds_digit]
    #created a variable called teens_word to indicate which word in the teens dictionary is to be used
    teens_word = worded_teens[teens_modulo]
    #print outcome
    print(f"{hundreds_word} {teens_word}")
## if statement that determines if a digit is over 100 and the tens place is greater than zero
#  this determines if the number is greater than 19 in the tens place inside a 3 digit number.
elif digit >= 100 and hundreds_ten_digit > 1:
    #created a variable called hundreds_word to indicate which word in the 100's dictionary is to be used
    hundreds_word = worded_hundreds_digits[hundreds_digit]
     #created a variable called tens_word to indicate which word in the tens dictionary is to be used
    ten_word = worded_tens_digits[ten_digit]
     #created a variable called ones_word to indicate which word in the ones dictionary is to be used
    ones_word = worded_ones_digits[ones_digit]
    #print outcome
    print(f"{hundreds_word} {ten_word} {ones_word}")
           
# Elif statement that determines if a digit is under 10 
elif digit < 10:
    # Name value of single digit numbers that are less than 10 from the oens dictionary
    single_digit = worded_ones_digits[ones_digit]
    print(single_digit)
# Prints teen values from the teen dictionary that are greater than 10 and less than 20.
elif digit >= 10 and digit < 20:
    teens = worded_teens[teens_digit]
    print(teens)
# Prints all named values that are less than 100 but more than 20 that the user puts in.
elif digit >= 20 or digit <= 99:
    tens_word = worded_tens_digits[ten_digit]
    ones_word = worded_ones_digits[ones_digit]
    print(f"{tens_word} {ones_word}")

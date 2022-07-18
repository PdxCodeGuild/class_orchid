
# Created a dictionary that holds 0-9 along with the word the corresponds to each numbers
worded_ones_digits = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

# Created a dictionary that holds 10-19 along with the word the corresponds to each numbers
worded_teens = {

    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'

}

# Created a dictionary that holds 20-90 worded ten digits along with the word the corresponds to each numbers
worded_tens_digits = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

# Ask the user to input a number between 0 and 99
digit = input("\nEnter a number between 0-99: ")

# Converts the string input from the variable digit from a string into a integer
digit = int(digit)

# Used modulo to get the remainder of the number that was input
ones_digit = digit % 10

#used floot division to find get the number in the 10s position
ten_digit = digit // 10

# Create a teens digit to represent any number in the teens that is types in 
teens_digit = digit

# Created an if statements that prints 'zero' when the user type 0
if digit == 0:
    print("zero")

# Elif statement that prints the name value of single digit numbers that are less than 10.
elif digit < 10:
    single_digit = worded_ones_digits[ones_digit]
    print(single_digit)
# Prints teen values from the teen dictionary that are greater than 10 and less than 20.
elif digit > 10 and digit < 20:
    teens = worded_teens[teens_digit]
    print(teens)
# Prints all named values that are less than 100 but more than 20 that the user puts in.
elif digit >= 20 or digit <= 99:
    tens_word = worded_tens_digits[ten_digit]
    ones_word = worded_ones_digits[ones_digit]
    print(f"{tens_word}-{ones_word}")
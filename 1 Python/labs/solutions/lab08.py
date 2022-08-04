# Lab 08 Solution - Credit Card Validator

# Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

def credit_validator(card_num_string: str):
    """Returns whether a string containing a credit card number is valid, by returnint 'Valid' or 'Invalid'."""
    # Convert the input string into a list of ints
    card_num_list = [int(num) for num in card_num_string]
    # Slice off the last digit. That is the check digit.
    check_digit = card_num_list.pop()
    # Reverse the digits.
    card_num_list.reverse()
    # Double every other element in the reversed list.
    for index in range(len(card_num_list)):
        if index % 2 == 0:
            card_num_list[index] *= 2
            # Subtract nine from numbers over nine.
            if card_num_list[index] > 9:
                card_num_list[index] -= 9
    # Sum all values.
    # Take the second digit of that sum.
    special_number = int(str(sum(card_num_list))[1])
    # If that matches the check digit, the whole card number is valid.
    if special_number == check_digit:
        return 'Valid'
    else:
        return 'Invalid'
    
    

print(credit_validator("4556737586899855"))

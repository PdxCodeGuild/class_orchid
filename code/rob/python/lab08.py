card_to_check = '4556737586899855'
copy = list(card_to_check)[-2::-1]

last_digit = list(card_to_check).pop()

def card_is_valid():
    for index, num in enumerate(copy):
        copy[index] = int(copy[index])
        if index % 2 == 0:
            copy[index] *= 2
        if copy[index] > 9:
            copy[index] -= 9
        
    copy_sum = str(sum(copy))

    if last_digit == copy_sum[1]:
        return True
    else:
        return False

is_valid = card_is_valid()

print('Card: ', card_to_check, '\nIs Valid: ', is_valid)

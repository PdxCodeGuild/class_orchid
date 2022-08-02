'''Rot13'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alpha_len = len(alphabet)

def rot_start_index(reference, rot_value):
    '''Used to find the current Index in the alphabet'''
    rot_value = rot_value
    rotated = 0
    for index, letter in enumerate(alphabet):
        if letter == reference:
            rotated = rotate(index, rot_value)
    return rotated

def rotate(index, rot_value):
    '''rotates the given index by the given rot rot_value'''
    rot_value = rot_value
    while rot_value > alpha_len:
        rot_value -= alpha_len
    if rot_value > 0: #adds and loops over index if out of index values
        index += rot_value
        if index > alpha_len:
            index -= alpha_len
    elif rot_value < 0: #subtracts and loops back if out of index values
        index -= rot_value
        if index < 0:
            index += alpha_len
    elif rot_value == 0: #does nothing at all
        index += 0
    return index

def main():
    print("\nRot Encryption. (No Capitalization Support)\n")
    encrypt = str(input("What do you need encrypted?\n> ")).lower()
    rot_value = input("What is your ROT?\n> ")
    rot_value = int(rot_value)

    reference_rot = ''

    for reference in encrypt:
        if reference == ' ':
            reference_rot += ' '
        else:
            rot_add = rot_start_index(reference, rot_value)
            reference_rot += alphabet[rot_add]

    print(f"With a ROT of {rot_value}, '{encrypt}' becomes '{reference_rot}'.")

main()
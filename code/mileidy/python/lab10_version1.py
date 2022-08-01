
english_dictionary = {
    ' ' : '',
    'a' : 0,
    'b' : 1,
    'c' : 2,
    'd' : 3,
    'e' : 4,
    'f' : 5,
    'g' : 6,
    'h' : 7,
    'i' : 8,
    'j' : 9,
    'k' : 10,
    'l' : 11,
    'm' : 12,
    'n' : 13,
    'o' : 14,
    'p' : 15,
    'q' : 16,
    'r' : 17,
    's' : 18,
    't' : 19,
    'u' : 20,
    'v' : 21,
    'w' : 22,
    'x' : 23,
    'y' : 24,
    'z' : 25
}
rot_13_dictionary = {
    '' : ' ',
    0 : 'n',
    1 : 'o',
    2 : 'p',
    3 : 'q',
    4 : 'r',
    5 : 's',
    6 : 't',
    7 : 'u',
    8 : 'v',
    9 : 'w',
    10 : 'x',
    11 : 'y',
    12 : 'z',
    13 : 'a',
    14 : 'b',
    15 : 'c',
    16 : 'd',
    17 : 'e',
    18 : 'f',
    19 : 'g',
    20 : 'h',
    21 : 'i',
    22 : 'j',
    23 : 'k',
    24 : 'l',
    25 : 'm',
}

user_input = input('Please enter a word: ')
string = user_input.lower()
result = ""

for letter in string:
    keys = english_dictionary[letter]
    second_value = rot_13_dictionary[keys]
    result += second_value

print(result)

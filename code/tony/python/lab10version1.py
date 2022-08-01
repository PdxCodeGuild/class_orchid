def rot13(s: str):
    return ''.join([chr(ord(s) + (
        (ord(s) in range(97, 110) or ord(s) in range(65, 78)) and 13 or 
        (ord(s) in range(110, 123) or ord(s) in range(78, 91)) and -13
        )) for s in s])

user_input = input('Enter a string to encode: ')

print(rot13(user_input))
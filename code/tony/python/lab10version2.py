def rot13(s: str, o: int):
    return ''.join([chr(
        ord(s) + (
            ord(s) in range(65, 65 + 26 - o) and o
            or ord(s) in range(65 + 26 - o, 65 + 26) and -26 + o
            or ord(s) in range(97, 97 + 26 - o) and o
            or ord(s) in range(97 + 26 - o, 97 + 26) and -26 + o
        )
    ) for s in s])

user_offset = input('Enter offset amount: ')
user_input = input('Enter a string to encode: ')

print(rot13(user_input, int(user_offset)))

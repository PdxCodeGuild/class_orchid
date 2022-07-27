from string import ascii_lowercase, ascii_uppercase

def rot(s,r):
    return ('').join([ascii_lowercase[ascii_lowercase.index(l) + r - 26] if l in ascii_lowercase else ascii_uppercase[ascii_uppercase.index(l) + r - 26] if l in ascii_uppercase else l for l in s])

user_string = input('Please enter a string: ')
rotations = int(input('Please enter a number of rotations: '))

print(rot(user_string,rotations))
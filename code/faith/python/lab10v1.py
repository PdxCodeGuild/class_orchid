rot13={
    'a':'n',
    'b':'o',
    'c':'p',
    'd':'q',
    'e':'r',
    'f':'s',
    'g':'t',
    'h':'u',
    'i':'v',
    'j':'w',
    'k':'x',
    'l':'y',
    'm':'z',
    'n':'a',
    'o':'b',
    'p':'c',
    'q':'d',
    'r':'e',
    's':'f',
    't':'g',
    'u':'h',
    'v':'i',
    'w':'j',
    'x':'k',
    'y':'l',
    'z':'m',
}   


userinput = input('Please enter a word: ')
codedword = []


for character in userinput:
    if character != ' ':
        codedword.append(rot13[character])
    else:
        codedword.append(' ')
print(''.join(codedword))


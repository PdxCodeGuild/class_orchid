# import sys
# input_string = sys.argv[1]

while True:
    try: input_value = int(input('Enter a number [0-4999]: '))
    except ValueError: continue
    except KeyboardInterrupt: print(''); quit()
    if input_value: break

trans = [
    ( 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', ),
    ( 'x', 'xx', 'xxx', 'xl', 'l', 'lx', 'lxx', 'lxxx', 'xc', ),
    ( 'c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dccc', 'cm', ),
    ( 'm', 'mm', 'mmm', 'mmmm' ),
]

i = 0
output_string = ''
for s in str(input_value):
    pos = len(str(input_value)) - i - 1
    i += 1
    output_string += trans[pos][int(s)-1]

print(output_string)
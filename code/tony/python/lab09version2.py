import enum


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9] # test data
greatest = sorted(data)[-1::][0] # greatest value from data
str = '' # initialize a string

for i in range(greatest,0,-1): # decrement through value range
    for val in data: # each value from data
        if val >= i: str += 'X' # plot on the chart
        else: str += ' ' # don't plot
    if i > 1: str += '\n' # new value, new line

print(str)
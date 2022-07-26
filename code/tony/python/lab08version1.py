# accept the user input
cc = input('Please insert your stolen card now: ')

# convert it to a list of ints
cc = list(map(int, cc))
# store the check digit
check = cc[-1::][0]

# reverse the list
cc = cc[:-1:][::-1]

# initialize the sum value
sum = 0

# apply validation rules
for i, value in enumerate(cc):
    if (i+1) % 2: cc[i] = cc[i] * 2
    if cc[i] > 9: cc[i] = cc[i] - 9
    sum += cc[i]

# print the result
if int(str(sum)[1]) == check: print('Valid.')
else: print('Invalid.')

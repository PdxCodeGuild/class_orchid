#data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9,8,7,6,5,4,5,6]

def peaks(values):
    peaks = []
    for x in range(len(values)):
        if x != 0 and x != len(values) - 1:
            if values[x - 1] < values[x] and values[x] > values[x + 1]:
                peaks.append(x)
    return peaks

def valleys(values):
    valleys = []
    for x in range(len(values)):
        if x != 0 and x != len(values) - 1:
            if values[x - 1] > values[x] and values[x] < values[x + 1]:
                valleys.append(x)
    return valleys

peak_list = peaks(data)
valley_list = valleys(data)



def version_2():
    max = data[peak_list[0]] if data[peak_list[0]] > data[peak_list[1]] else data[peak_list[1]]
    while max > 0:
        for x in range(len(data)):
            if data[x] >= max:
                print('X', end=' ')
            else:
                print(' ', end=' ')
            if x == len(data) -1:
                print('')
        max -= 1


def version_3():
    max = data[peak_list[0]] if data[peak_list[0]] > data[peak_list[1]] else data[peak_list[1]]
    prev = 0
    count_x = 0
    count_o = 0
    while max > 0:
        max_numbers = data.count(max)
        for x in range(len(data)):
            index = x + 1
            check_second_max = data[x::] if x != len(data) - 1 else [0]
            #print(check_second_max, max, check_second_max.count(max))
            if check_second_max.count(max) >= 1:
                check_second_max = True
            if data[x] >= max:
                print('X', end=' ')
                count_x += 1
                prev = data[x]
            elif data[x] <= prev and prev != 0 and max_numbers >= 2 and check_second_max == True:
                print('0', end=' ')
                count_o += 1
            else:
                print(' ', end=' ')
            if x == len(data) -1:
                print('')
                prev = 0
        max -= 1
    water = count_x / count_o
    print(f'\nwater: {water}, x\'s: {count_x}, o\'s: {count_o}')

user_input = 1
options = [1,2,3,4]
while user_input in options:
    print('\n1. To see peaks')
    print('2. To see valleys')
    print('3. To see version 2')
    print('4. To see version 3')
    user_input = int(input(f'\nPick a number:'))
    if user_input == 1:
        print('')
        print('Peaks: ', peak_list)
    elif user_input == 2:
        print('')
        print('Valleys: ', valley_list)
    elif user_input == 3:
        print('')
        version_2()
    elif user_input == 4:
        print('')
        version_3()
    else:
        print('invalid option. bye.')
nums = [5, 0, 8, 3, 4, 1, 6]
total = sum(nums)
sum_by_len = total / len(nums)

print(f'\nList total ({total}) divided by numbers in list ({len(nums)}) is {sum_by_len}.\n')


#version 2
nums = []
total = 0
sum_by_len = 0
done = ''

while done != 'done':
    num = input('enter a number, or "done": ')
    if not num.isnumeric():
        done = 'done'
    else:
        nums.append(int(num))

if len(nums) == 0:
    print('no numbers were entered.')
else:    
    total = sum(nums)
    sum_by_len = total / len(nums)

print(f'\nList total ({total}) divided by numbers in list ({len(nums)}) is {sum_by_len}.\n')

nums = []



# print(round(z))
while True:
    user_input = input("enter a number, or 'done: ")
    
    if user_input == 'done':
        sum_nums = sum(nums)
        z = sum_nums / len(nums)
        break
    nums.append(int(user_input))
    print(nums)
# function to get the total and average

print(z)
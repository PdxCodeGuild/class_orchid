## Author: Andrew L Jaquez
## Date updated: 7/18/2022
## Version 1

# nums = [5, 0, 8, 3, 4, 1, 6]
# total = sum(nums)
# total2 = 0
# # loop over the elements
# for num in nums:
#     total2 = total / len(nums)
# print(total2)

#### Verison 2

user_nums = []
while True:
    user_input = input("Enter one number at a time to add to the list: ")
    if user_input == 'done':
        break
    else: 
        user_nums.append(user_input)
for i in range(0, len(user_nums)):
    user_nums[i] = int(user_nums[i])
total_new = sum(user_nums)
for num in user_nums:
    total2_new = total_new / len(user_nums)
print(total2_new)   
print(str(user_nums))

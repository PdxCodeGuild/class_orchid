# nums = [5, 0, 8, 3, 4, 1, 6] # set list 
# sum = 0 # place holder variable to zero 

# # for loop where I am adding the numbers in the list. 

# for num in nums:
    
#     sum = sum + num



# print(f'The sum of the list is {sum}') # Prints out the sum of the list 

# print(f'The length of the list is {len(nums)}') # Prints out length of list

# print(f'The average is {sum / len(nums)}') # Prints out the average 


###################### Version 2 

nums = [] # empty list
sum = 0 # sum set to zero

# start of REPL

while True: 
    add = input('add a number or done: ')
    # print(nums)

    if add == 'done': # done will break the loop
        break

    nums.append(int(add)) # will append and typecast to nums list from the user input variable add
    # print(nums)

for num in nums: # for loop to add the numbers that were added to the list.
    sum = sum + num

print(f'average: {sum / len(nums)}')








    


























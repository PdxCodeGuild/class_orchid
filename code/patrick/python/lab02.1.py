nums = []
total = 0

while True:
    user_responce = input("\nPlease enter a number or 'done' to calcuate")
    if user_responce == "done":
        break
    else:
        nums.append(int(user_responce))
    


    for item in nums:
        total += int(user_responce)


lenght_of_list = len(nums)#part1
total = sum(nums) #part1

final_total = total / lenght_of_list #part1




print(final_total) #part1
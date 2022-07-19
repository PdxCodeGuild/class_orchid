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


lenght_of_list = len(nums)
total = sum(nums) 

final_total = total / lenght_of_list 




print(final_total) 
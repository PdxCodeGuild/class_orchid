nums1 = []
total = 0

while True:
    user_nums = input("\nEnter a number or 'done' to quit: ")
    if user_nums == "done":
            break
    else:
        nums1.append(int(user_nums))

total = sum(nums1)

sum_divided = total / len(nums1)

print(f'\nTotal ({total}) divided by list of numbers ({len(nums1)}) is {sum_divided}.\n')

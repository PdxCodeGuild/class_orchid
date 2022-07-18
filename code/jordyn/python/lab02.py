#Version 1

# nums = [5, 0, 8, 3, 4, 1, 6]
# num_added = 0
# for num in nums:
#     # print(num)
#     num_added += num
#     # print(num_added)

# average = num_added / len(nums)
# average = "{:.3f}".format(average)
# print(f"Average: {average}")

#Version 2

nums = []

while 'done' not in nums:
    x = input("Enter a number, or 'done': ")
    nums.append(x)

# print(nums)

nums.remove('done')
# print(nums)

total = 0
for i in nums:
    total += int(i)

# print(total)
length = len(nums)
# print(length)

average = total / length

print(f'A total of {length} numbers were provided, totaling {total} for an average of: {average}')
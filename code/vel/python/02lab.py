numbers = []
while True:
    nums = input('\nEnter your number here, if done type done: ')
    if nums == "done":
        print(f"Average: {sum(numbers) / len(numbers)}")
        break
    nums = int(nums)
    numbers.append(nums)

# print(numbers) for testing purposes 



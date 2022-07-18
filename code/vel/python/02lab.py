## Version 1 ###


nums = [5, 0, 8, 3, 4, 1, 6] # lets find a way to store the returns and add them for a sum
def sum(list_of_numbers):
    """
    this function accepts a list of numbers and returns the sum
    """
    total = 0
    for num in list_of_numbers: 
        total = num + total
    return total

def average(list_of_numbers):
    """
    this function accepts a list of numbers and returns the average 
    """
    average = sum(list_of_numbers) / len(list_of_numbers)
    return average


print(average(nums))




#### Version 2 ####

numbers = []
while True:
    nums = input('\nEnter your number here, if done type done: ')
    if nums == "done":
        print(f"Average: {sum(numbers) / len(numbers)}")
        break
    nums = int(nums)
    numbers.append(nums)

# print(numbers) for testing purposes 



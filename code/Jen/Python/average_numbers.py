'''Jen Williams
PDX Code Guild Bootcamp - Orchid
lab 2: Average Numbers'''

nums = [5, 0, 8, 3, 4, 1, 6]

x = (len(nums))

mylist = []

for num in nums:
    mylist.append(num)
    z = sum(mylist)
    print(f"number - {num}") 
    print(f"total - {z}")

print(f"The sum of the numbers entered is {z}. The average of the numbers listed is {z / x}.")


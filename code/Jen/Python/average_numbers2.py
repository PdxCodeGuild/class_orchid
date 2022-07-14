'''Jen Williams
PDX Code Guild Bootcamp - Orchid
lab 2: Average Numbers
'''

nums= []
x = input("Please enter a number or 'done' ")

while x.lower() != "done":
    x = int(x)
    nums.append(x)
    #print(nums)
    x = input("Please enter a number or 'done' ")

z = sum(nums)
y = len(nums)
average = (z / y)
average = round(average, 2)

print(f"The average of {nums} is {average}")

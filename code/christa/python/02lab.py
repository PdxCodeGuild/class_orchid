# Version1 lab02
#list of numbers
num = [5, 0, 8, 3, 4, 1, 6]
total_num = 0
# adding each value in the list to the one before it
for val in num:
    total_num = total_num + val

average = total_num/len(num)

print(average)


"""
#Version2
num = []
x = 0
#conditional to build the list for 'num'
while True:
    to_list = input("Enter a number or 'done': ")
    
    if to_list == 'done':
        print("\nThank you")
        break
    else:
        to_list = int(to_list) #identifies the numbers imputed by user are integers
        num.append(to_list) #add integers to the list

for val in num: #adds up the values imputed in the list
    x = x + val
        
avg = x/len(num) #formula for average is the total of num divided by the 'len' (total number of items in the list)

print(avg)

"""
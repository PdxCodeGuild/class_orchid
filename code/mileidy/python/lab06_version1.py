import random

def pick6(k, low = 1, high = 99): #referred back to my 102 notes
    numbers_list = []
    for x in range(6):
        random_number = random.randint(low, high)
        numbers_list.append(random_number)
    return numbers_list

numbers_list = pick6(6, 1, 99) 
# print(numbers_list) succesfully got 6 random numbers in range of 1-99
winning_ticket = pick6()
balance = 0

def num_matches(winning_ticket, ticket):
    for num in winning_ticket == num in ticket:
        return num
    
for x in range(100000):

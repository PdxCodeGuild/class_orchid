import time
import random

def pick6(k, low = 1, high = 99): #referred back to my 102 notes
    numbers_list = []
    for x in range(6):
        random_number = random.randint(low, high)
        numbers_list.append(random_number)
    return numbers_list

numbers_list = pick6(6, 1, 99) 
# print(numbers_list) succesfully got 6 random numbers in range of 1-99
winning_ticket = pick6(6, 1, 99)

winning_amount = {
    0 : 0,
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000
}

def num_matches(winning_ticket, ticket):
    matches = 0 
    for index in range(len(winning_ticket)):
        if winning_ticket[index] == ticket[index]:
            matches += 1

    return matches

winning_ticket = pick6(6, 1, 99)
balance = 0
earnings = 0

for x in range(100000):
    ticket = pick6(6, 1, 99)
    balance -= 2
    matches = num_matches(winning_ticket, ticket)
    earnings+= winning_amount[matches]
    
print('We are currently "crunching" the numbers....')
time.sleep(0)

print('In 3')
time.sleep(0)

print('2')
time.sleep(0)

print("1")
time.sleep(0)

print(balance)
print(earnings)

print(f'The results are in! \nYour final balance is: {earnings + balance }!')

print(f'Your ROI is {(earnings - balance)/ balance}%')
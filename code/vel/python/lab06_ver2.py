"""
Lab 6: Pick6
"""
import random   
# enumerate: can be used to find both the value and index position for each loop/iteration in a for loop

def num_matches(winning_ticket, ticket):
    matches = 0
    for index, number in enumerate(ticket):
        if number == winning_ticket[index]:
            matches += 1
    return matches

earnings = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000,
}

def pick_6():
    pick_6_list = []
    for number in range(0,6):
        num = random.randint(1,99)
        pick_6_list.append(num)
    return pick_6_list

winning_ticket = pick_6()
total = 0
expenses = 0
for x in range(100000):
    ticket = pick_6()
    total -= 2
    expenses += 2
    matches = num_matches(winning_ticket, ticket)
    total += earnings[matches]



ROI = (total)/expenses
print(f'\nYour final balance: ${total}')
print(f'\nYour earnings are ${total} and your expenses are ${expenses}, which makes your ROI is {ROI} %\n')


    





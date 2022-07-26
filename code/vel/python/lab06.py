"""
Lab 6: Pick6
"""

import random

    
def pick_6():
    pick_6_list = []
    for number in range(0,6):
        num = random.randint(1,99)
        pick_6_list.append(num)
    return pick_6_list



winning_ticket = pick_6()


for x in range(100,000):
    ticket = pick_6()
    







"""
first step: create a function that genreates six random numbers that represent the winning ticket

find a way to keep a running sum with a starting balance of $0, -2 every time we 
loop ( total = 0 is a start? -2 from total then add any earnings to total )

next create a function that matches the numbers in both ticket and winning ticket by index position
find a way to make the generator and matching function loop 100,000 times (in range?) 

after the loop, print the final balance 

"""
    


# def num_matches(winning_ticket, ticket):
#     for number in winning_ticket == number in ticket:
#         return number
        




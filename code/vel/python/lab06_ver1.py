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
        
"""
building a function that takes in ticket and winning ticket, 
compares the random numbers looking for matches by index
returns the number of matches which correlates to earnings
"""

def pick_6():
    pick_6_list = []
    for number in range(0,6):
        num = random.randint(1,99)
        pick_6_list.append(num)
    return pick_6_list

winning_ticket = pick_6()
total = 0

for x in range(100000):
    ticket = pick_6()
    total -= 2
    matches = num_matches(winning_ticket, ticket)
    total += earnings[matches]
print(f'\nYour final balance: {total} dollars, will you be taking that in all large bills or all ones?')


"""
first step: create a function that genreates six random numbers that represent the winning ticket

find a way to keep a running sum with a starting balance of $0, -2 every time we 
loop ( total = 0 is a start? -2 from total then add any earnings to total )

next create a function that matches the numbers in both ticket and winning ticket by index position
find a way to make the generator and matching function loop 100,000 times (in range?) 

after the loop, print the final balance 

"""
    





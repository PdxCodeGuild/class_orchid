#PICK 6 V1

#1. Used YouTube tutorial from computing101.net on how to create a lottery game in python
#  I adjusted the suggested use of a for loop to something more simple

#2.Used the example on stackoverflow on how to use random.sample and adjusted it to random.randint

"""
A ticket contains 6 numbers, 1 to 99, and the number of matches between 
the ticket and the winning numbers determines the payoff. Order matters, 
if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. 
If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. 
Calculate your net winnings (the sum of all expenses and earnings).
"""

import random
#lists to store random numbers generated

#generate lottery winning numbers and add to list
#1. Generate a list of 6 random numbers representing a the winning ticket
def pick6():
    six_list=[]
    for _ in range(6):
        random_number = random.randint(1,99) #!!!! change to 99 before submission
        six_list.append(random_number)
    return six_list
#print(pick6())                   

winning_pick6 = pick6()
#print(winning_pick6)
#generate my gas staion random pick 6 ticket and add to list

#compare the numbers in the list by position in the list
def ticket_checker(winning_ticket):
    new_ticket = pick6()      #4. Generate a list of 6 random numbers representing the ticket
    correct_numbers = 0
    for index in range(6):
        if winning_ticket[index] == new_ticket[index]:
            correct_numbers +=1
   # print(winning_ticket)
    #print(new_ticket)
    #print(correct_numbers)
    return correct_numbers               #6 Find how many numbers match
       
#num_matches = ticket_checker(winning_pick6)
#print(num_matches)
num_matches = 0
#2. Start your balance at 0
winnings = 0

#3. Loop 100,000 times, for each loop:
for x in range(100000):
    winnings -= 2                                #5. Subtract 2 from your blance(you bought a ticket)
    num_matches = ticket_checker(winning_pick6) 
    #print('matches', num_matches) 
    #print('dollars expended', winnings)
    if num_matches == 1:
        winnings += 4          #7. Add to your balance the winnings from your matches
    elif num_matches ==2:
        winnings += 7
    elif num_matches == 3:
        winnings += 100
    elif num_matches == 4:
        winnings +=50000
    elif num_matches == 5:
        winnings += 1000000
    elif num_matches == 6:
        winnings += 25000000
print(winnings)       #8. After the loop, print the final balance

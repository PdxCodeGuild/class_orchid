'''Jen Williams
PDX Code Guild Bootcamp
Class Orchid
lab 6: Pick6'''

import random

win_amounts = {
    0 : 0,
    1 : 4.00,
    2 : 7.00,
    3 : 100.00,
    4 : 50_000.00,
    5 : 1_000_000.00,
    6 : 25_000_000.00,
}

ticket = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),]
print(f"Your numbers are {ticket}")
def num_matches(winning_ticket, ticket):
    ticket_wins = 0
    if winning_ticket[0] == ticket[0]:
        ticket_wins = ticket_wins + 1
    if winning_ticket[1] == ticket[1]:
        ticket_wins = ticket_wins + 1
    if winning_ticket[2] == ticket[2]:
        ticket_wins = ticket_wins + 1
    if winning_ticket[3] == ticket[3]:
        ticket_wins = ticket_wins + 1
    if winning_ticket[4] == ticket[4]:
        ticket_wins = ticket_wins + 1    
    if winning_ticket[5] == ticket[5]:
        ticket_wins = ticket_wins + 1    
    winnings = win_amounts.get(ticket_wins)
    return (winnings)

def pick6():
    
    #charge for a ticket
    winning_ticket = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),]
    # create a list of 6 random numbers
    return winning_ticket

running_total = 0
x = 100_000
expense = x * 2.00
while x > 0:
    x = x - 1
    running_total += num_matches(pick6(), ticket)
    
bank = running_total - expense
running_total -= expense
ROI = running_total/expense
if bank > 0:
    print(f"You have played these numbers 100,000 times. Your bank balance is now ${bank}. Your ROI is {ROI} Congratulations!")    
else: print(f"You have played these numbers 100,000 times. Your bank balance is now ${bank}. Your ROI is {ROI} Please try again.")






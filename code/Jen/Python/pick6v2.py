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

ticket = []

var1 = 6
while int(var1) > 0:
    ticket.append(random.randint(1,99))
    var1 -= 1

print(f"Your numbers are {ticket}")


def num_matches(winning_ticket, ticket):
    ticket_wins = 0
    for i, wins in enumerate(winning_ticket):
        for i, ticks in enumerate(ticket):
            if wins == ticks:
                ticket_wins += 1
    return ticket_wins

def pick6():
    
    winning_ticket = []
    var2 = 6
    while int(var2) > 0:
        winning_ticket.append(random.randint(1,99))
        var2 -= 1
    return winning_ticket

running_total = 0
x = 100_000
expense = 0
while x > 0:
    x -= 1
    expense -= 2.00
    running_total += num_matches(pick6(), ticket)
    
bank = running_total + expense
ROI = running_total/expense
if bank > 0:
    print(f"You have played these numbers 100,000 times. Your bank balance is now ${bank}. Your ROI is {ROI} Congratulations!")    
else: print(f"You have played these numbers 100,000 times. Your bank balance is now ${bank}. Your ROI is {ROI} Please try again.")






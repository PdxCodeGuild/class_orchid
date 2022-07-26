#pick6

import random

def pick6(): #Generates Ticket Numbers
    random_list = []
    loop = 1
    while loop <= 6:
        random_list += [random.randint(1,99)]
        # print(random_list) #list creation test
        loop += 1
    else:
        return random_list

def num_matches(winning, ticket): #Matches Tickets to the selected winning ticket
    matches = 0
    index = 0
    while True:
        if winning[index] == ticket[index]:
            matches += 1
            if index <= 4:
                index += 1
            elif index == 5:
                return matches
        elif index <= 4:
            index += 1
        else:
            return matches

def matching_value(matched): #Returns the winning amount for a ticket minus the cost of the ticket itself
    value = 0
    if matched == 0:
        return value
    elif matched == 1:
        value += 4
        return value
    elif matched == 2:
        value += 7
        return value
    elif matched == 3:
        value += 100
        return value
    elif matched == 4:
        value += 50000
        return value
    elif matched == 5:
        value += 1000000
        return value
    elif matched == 6:
        value += 25000000
        return value

loop = 0
winning_ticket = pick6()
expenses = 0
earnings = 0
ticket_count = 100000

while loop != ticket_count:

    ticket = pick6()

    matching = num_matches(winning_ticket, ticket)

    earnings += matching_value(matching)

    expenses -= 2

    loop += 1

print(f"After {ticket_count} tickets, you made a total earnings of ${int(earnings)}. However cost of the tickets was ${int(expenses)}.")
print(f'This has an ROI of {"{:.2f}".format(((earnings - expenses) / expenses) * 100)}%')
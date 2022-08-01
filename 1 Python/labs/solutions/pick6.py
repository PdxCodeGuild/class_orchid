from random import randint, sample
# if you wanted to also import choice from random, you would do this:
# from random import randint, choice

def pick6():
    """
    return a list of 6 random numbers from 1-99
    """
    # this solution can lead to duplicate numbers on a ticket,
    # which can't happen in the lottery
    ticket = []
    for _ in range(6):
        ticket.append(randint(1, 99))
    # return ticket

    # this solution sees that a number does not
    # end up on the ticket more than once
    ticket = []
    while len(ticket) < 6:
        number = randint(1, 99)
        if number not in ticket:
            ticket.append(number)
    # return ticket

    return sample(range(1, 100), 6)

def num_matches(winning_ticket, ticket):
    """
    return the number of matches between the 2 tickets
    """

    # for i in range(len(list)) version
    matches = 0
    for i in range(len(winning_ticket)):
        if winning_ticket[i] == ticket[i]:
            matches += 1
    # return matches

    # for i, element in enumerate(list) version
    matches = 0
    for i, number in enumerate(winning_ticket):
        if number == ticket[i]:
            matches += 1
    # return matches

    matches = 0
    for number1, number2 in zip(winning_ticket, ticket):
        if number1 == number2:
            matches += 1
    return matches

matches_to_winnings = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50_000,
    5: 1_000_000,
    6: 25_000_000,
}


# Generate a list of 6 random numbers representing the winning ticket

# create the winning ticket
winning_ticket = pick6()

# Start your balance at 0
balance = 0
earnings = 0
expenses = 0

# Loop 100,000 times, for each loop:
# you can use underscores in numbers in Python, they will be ignored, but you can use them
# like commas, for instance, to make large numbers easier to read
for _ in range(100_000):

    # Generate a list of 6 random numbers representing the ticket
    ticket = pick6()

    # Subtract 2 from your balance (you bought a ticket)
    balance -= 2
    expenses += 2

    # Find how many numbers match
    matches = num_matches(winning_ticket, ticket)

    # Add to your balance the winnings from your matches
    winnings = matches_to_winnings[matches]
    balance += winnings
    earnings += winnings



# After the loop, print the final balance
print('final balance', balance)
print('expenses', expenses)
print('earnings', earnings)

# calculate roi 
roi = (earnings - expenses) / expenses
print('ROI', roi)
import random

def pick6():
    return [random.randint(1,99) for _ in range(6)]

def num_matches(winning_ticket, ticket):
    matching = 0
    for k,v in enumerate(ticket):
        if winning_ticket[k] == v: matching += 1
    return matching

winning_ticket = pick6()
balance = 0

payouts = [ 0, 4, 7, 100, 50000, 1000000, 25000000 ]

for i in range(100000):
    ticket = pick6()
    balance -= 2
    matching = num_matches(winning_ticket, ticket)
    if matching: balance += payouts[matching]

print(f'Final balance: {balance}')
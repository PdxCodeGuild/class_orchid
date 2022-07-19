#import random module
import random

#defining a function called pick6 that will randomly select 6 number and put them inside of a list
def pick6():

    pick_six_list = []
    for _ in range(6):
        random_selection = random.randint(0,9)
        pick_six_list.append(random_selection)
    return pick_six_list

ticket = [1,0,2]
winning_ticket = [1,0,2]

print(ticket)
print(winning_ticket)

def num_matches(ticket, winning_ticket):
    if ticket[0] == winning_ticket[0]:
        print("1")
num_matches(ticket, winning_ticket)


"""
Lab 6: Pick6

"""

import random

# function that will generate 6 random numbers. created empty list that after for loop is ran will append. 
def pick6(): 
    winning_numbers = []
    for numbers in range(0,6):
         numbers = random.randint(1,99)
         winning_numbers.append(numbers)
        #  print(winning_numbers)
    return winning_numbers

# Where the magic happends. Will take in two parameters. match_sum variable created to then be returned with a number 1-6.
# accomplished by checking the index and I used enumerate for this. 

def num_match(winning_number, ticket): 
    match_sum = 0
    for index, number in enumerate(ticket):
        if ticket[index] == winning_ticket[index]:
            match_sum += 1
    return match_sum

# set a winning ticket outside of the for loop that runs 100,000x so it remaind steady.
# starting_balance set to 0. earnings set to 0. 

winning_ticket = pick6()
starting_balance = 0
earnings = 0


# for loop that will run 100,000x taking in a ticket that will generate a new pick6 everytime it is iterated.
# matches will call the function to compare the two with two arguments and return number of matched index. 

for x in range(100000):
    ticket = pick6()
    matches = num_match(winning_ticket, ticket) 
    starting_balance -= 2
    if matches == 1:
        earnings += 4
    elif matches == 2:
        earnings += 7
    elif matches == 3:
        earnings += 100
    elif matches == 4:
        earnings += 50000
    elif matches == 5:
        earnings += 1000000
    elif matches == 6:
        earnings += 25000000
    

ending_balance = earnings + starting_balance
roi = (earnings - starting_balance) / starting_balance

print(f'''

Hello, thanks for playing pick6! 

Below you will find your results:

Your starting balance is: ${starting_balance}.

You've won: ${earnings}.

Your new blance is: ${ending_balance}

Your ROI is: {roi}%

''')





    




        
    



      
        

        


    

    





    





#import random module
import random

#defining a function called pick6 that will randomly select 6 number and put them inside of a list
def pick6():
    # created an empty list that will contain the random list of integers
    pick_six_list = []
    #for blank indices in the range of six indices 
    for _ in range(6):
        # we want to randomly select a number between 0 and 99
        # to be placed in the blank list
        random_selection = random.randint(0,99)
        #Here we append the list with the random_selection before the loop iterates again. 
        pick_six_list.append(random_selection)
    #the loop will iterate 6 times (range(6)) before completing and the function will return 
    #the newly created list
    return pick_six_list

#The function num_matches will take on the input variables ticket and winning ticket
def num_matches(ticket, winning_ticket):
    #compares the items in the same indices of ticket and winning_ticket. 
    # As long as the indices are matching in order the for loop will continue iterations until 
    #two items in the same index position do not match
    matches = 0
    for index in range(6):
        if ticket[index] == winning_ticket[index]:
            #adds a match for every index position that has the same integer
            matches += 1
    return matches

#function that takes the the total matches from a winning_ticket and ticket and provides the 
#winning amount based on the amount of matches.
def winnings(matches):
    ticket_winnings = 0
    if matches == 1:
        ticket_winnings += 4
        
    elif matches == 2:
        ticket_winnings += 7
        
    elif matches == 3:
        ticket_winnings += 100
        
    elif matches == 4:
        ticket_winnings += 50000
       
    elif matches == 5:
        ticket_winnings += 1000000
        
    elif matches == 6:
        ticket_winnings += 25000000
    
    
    return ticket_winnings
        
#winning ticket randomly selected 6 numbers from the pick6() function
#totaly is the amount of money won or withdrawn
total = 0
#playing is the amount of plays which we will have or the amount of tickets to be purchased
playing = 100000


#while loop that iterates through 1 ticket pyrchased and matches it with a winning ticket
while playing:
    #subtracts one play from the total of 100,000 each iteration until 0 which is false
    playing -= 1
    #subtracts 2 dollars for a ticket per iteration
    total -= 2
    #using the pick6 function to select a random list of 6 numbers
    ticket = pick6()
    #using the pick6 function again to select a random list of 6 numbers for the winning ticket
    winning_ticket = pick6()
    #using the num_matches function to compare the winning ticket to the purchsed ticket 
    matches = num_matches(ticket, winning_ticket)
    #takes the new total from each iteration and adds it to a running total
    total += winnings(matches)


#printing the final amount    
print(f"Total: {total}")


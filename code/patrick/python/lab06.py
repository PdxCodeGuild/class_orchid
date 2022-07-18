
import random


paid_out = {
    "1" : 4,
    "2" : 7,
    "3" : 100,
    "4" : 50000,
    "5" : 1000000,
    "6" : 25000000,
    
}


#greet the user
print(f"\nWelcome to pick six")

#user_numbers = numbers = [random.randrange(1, 99) for i in range(6)]
#winning_numbers = [random.randrange(1, 99) for i in range(6)]



#print(user_numbers)
#print(winning_numbers)

def pick6():
    #winning_numbers = [random.randint(1, 9) for _ in range(6)]

    numbers = []
    for _ in range(6):
        numbers.append(random.randint(1, 9))
    
    return numbers


winning_numbers = pick6()



balance = 0

for _ in range(10):
     user_numbers = pick6()
     user_numbers.sort()
     winning_numbers.sort()
     if user_numbers <= winning_numbers:
        balance += -2
        #print(_)
        #print(cost_of_game)
        print(balance)
        if user_numbers == winning_numbers:
            balance =+ 1000
            print(balance)

 
#print("your balance is" [balance])






    



"""
Generate a list of 6 random numbers representing the winning ticket
Start your balance at 0
Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balance

"""
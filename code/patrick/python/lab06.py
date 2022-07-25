
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


#winning_numbers = pick6()
#print(winning_numbers)


#def num_matches( winning_numbers, user_numbers:
    #matches = 0
    #match = x == y 
    #for match in match
        #matches += 1 
        #return matches







balance = 0

for _ in range(0, 100000):
     user_numbers = pick6()
     winning_numbers = pick6()
     user_numbers.sort()
     winning_numbers.sort()
     matches = 0
     if winning_numbers[0] == user_numbers[0]:
        matches += 1
     if winning_numbers[1] == user_numbers[1]:
        matches += 1  
     if winning_numbers[2] == user_numbers[2]:
        matches += 1
     if winning_numbers[3] == user_numbers[3]:
        matches += 1
     if winning_numbers[4] == user_numbers[4]:
        matches += 1
     if winning_numbers[5] == user_numbers[5]:
        matches += 1
     if user_numbers <= winning_numbers:
        balance += -2
        #print(balance)
        if matches == 1:
            balance += paid_out["1"]
        if matches == 2:
            balance += paid_out["2"]
        if matches == 3:
            balance += paid_out["3"]
        if matches == 4:
            balance += paid_out["4"] 
        if matches == 5:
            balance += paid_out["5"]
        if matches == 6:
            balance += paid_out["6"]   
            #print(balance)
            print(matches)



#def num_matches():
    #matches = 0
    #if winning_numbers(0) == user_numbers(0):
       # matches += 1
    #if winning_numbers(1) == user_numbers(1):
    #    matches += 1  
    #if winning_numbers(2) == user_numbers(2):
       # matches += 1
    #if winning_numbers(3) == user_numbers(3):
        #matches += 1
    #if winning_numbers(4) == user_numbers(4):
        #matches += 1
    #if winning_numbers(5) == user_numbers(5):
        #matches += 1
#print(user_numbers) 
#print("your balance is" [balance])
print(balance)

print(matches)



    



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
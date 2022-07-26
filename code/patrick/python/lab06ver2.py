
import random


paid_out = {
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000,
    
}


#greet the user
print(f"\nWelcome to pick six")



def pick6():
    
    numbers = []
    for _ in range(6):
        numbers.append(random.randint(1, 99))
    
    return numbers






balance = 0
def num_matches(winning_ticket, ticket):
    
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
     return matches






expenses = 0

for _ in range(0, 100000):
     user_numbers = pick6()
     winning_numbers = pick6()
     
     matches = num_matches(user_numbers, winning_numbers)
    
   
     if user_numbers != winning_numbers:
        balance += -2
        expenses += 2
     if matches == 1:
        balance += paid_out[1]
     if matches == 2:
        balance += paid_out[2]
     if matches == 3:
        balance += paid_out[3]
     if matches == 4:
        balance += paid_out[4] 
     if matches == 5:
        balance += paid_out[5]
     if matches == 6:
        balance += paid_out[6]    



earnings = balance + expenses

roi = (earnings - expenses) / expenses




print(f"your return on investment is", roi)
print(f"your balance is", balance)

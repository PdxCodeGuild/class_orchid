import random

#print a welcome to Blackjack tutorial
print("Welcome to Blackjack Tutorial!")

#dictionary that holds each card and there value
card_deck = {
    "A": 1,
    "K": 10,
    "Q": 10,
    "J": 10,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "1": 1
}
#ask the user for their first, second and third card choice
first_card = input("What is your first card choice? ")
second_card = input("What is your second card choice? ")
third_card = input("What is your third card choice? ")

#print out each of the choices selected
print(f"Your first card is: {first_card}")
print(f"Your second card is {second_card}")
print(f"Your third card is {third_card}")

#convert the entered string that was selected and convert it into the value stored in the dictionary
first_card = card_deck[first_card]
second_card = card_deck[second_card]
third_card = card_deck[third_card]

#create a variable called hand adds together the 3 card choices
hand = first_card + second_card + third_card

# if statement that handles any inputs added that are between 17 and 20 
# and informs the user of the value and to stay
if hand >= 17 and hand <= 20:
    print(f"{hand} STAY")

 # if statement that handles any inputs added that are less than 17
# and informs the user of the value and to hit  
elif hand < 17:
    print(f"{hand} HIT")
# if statement that handles any inputs added that equal to 21
# and informs the user of the value and BLACKJACK
elif hand == 21:
    print(f"{hand} BLACKJACK!")
# if statement that handles any inputs added that are over 21
# and informs the user of the value and that they busted 
else:
    print("BUSTED!")

########## lab 05 version with random cards chosen instead of user selected

#print a welcome to Blackjack tutorial
print("Welcome to Blackjack Tutorial!")


#dictionary that holds each card and there value
card_deck = {
    "A": 1,
    "K": 10,
    "Q": 10,
    "J": 10,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "1": 1
}
#ask the user for their first, second and third card choice
first_card = random.choice(list(card_deck))
second_card = random.choice(list(card_deck))
third_card = random.choice(list(card_deck))

#print out each of the choices selected
print(f"Your first card is: {first_card}")
print(f"Your second card is {second_card}")
print(f"Your third card is {third_card}")

#convert the entered string that was selected and convert it into the value stored in the dictionary
first_card = card_deck[first_card]
second_card = card_deck[second_card]
third_card = card_deck[third_card]

#create a variable called hand adds together the 3 card choices
hand = first_card + second_card + third_card

# if statement that handles any inputs added that are between 17 and 20 
# and informs the user of the value and to stay
if hand >= 17 and hand <= 20:
    print(f"{hand} STAY")

 # if statement that handles any inputs added that are less than 17
# and informs the user of the value and to hit  
elif hand < 17:
    print(f"{hand} HIT")
    
# if statement that handles any inputs added that equal to 21
# and informs the user of the value and BLACKJACK
elif hand == 21:
    print(f"{hand} BLACKJACK!")
# if statement that handles any inputs added that are over 21
# and informs the user of the value and that they busted 
else:
    print("BUSTED!")
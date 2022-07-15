# Author Andrew Luis Jaquez
# Date created: 7/15/2022 2:36pm
# Lab 5: Blackjack Advice
cards_Deck = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
   '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}
# stores users input
user_card = input("What's your first card? ")
user_second_card = input("What's your second card? ")
user_third_card = input("What's your third card? ")
# holds value of the user input
user_hand = 0
user_hand2 = 0
user_hand3 = 0
#if statment for each card
if user_card == 'A' or user_card == 'a':
    user_hand = cards_Deck['A']
elif user_card == 'J' or user_card == 'j':
    user_hand = cards_Deck['J']
elif user_card == 'Q' or user_card == 'q':
    user_hand = cards_Deck['Q']
elif user_card == 'K' or user_card == 'k':
    user_hand = cards_Deck['K']
elif user_card == '2':
    user_hand = cards_Deck['2']
elif user_card == '3':
    user_hand = cards_Deck['3']
elif user_card == '4':
    user_hand = cards_Deck['4']
elif user_card == '5':
    user_hand = cards_Deck['5']
elif user_card == '6':
    user_hand = cards_Deck['6']
elif user_card == '7':
    user_hand = cards_Deck['7']
elif user_card == '8':
    user_hand = cards_Deck['8']
elif user_card == '9':
    user_hand = cards_Deck['9']
elif user_card == '10':
    user_hand = cards_Deck['10']
##################################
if user_second_card == 'A' or user_second_card == 'a':
    user_hand2 = cards_Deck['A']
elif user_second_card == 'J' or user_second_card == 'j':
    user_hand2 = cards_Deck['J']
elif user_second_card == 'Q' or user_second_card == 'q':
    user_hand2 = cards_Deck['Q']
elif user_second_card == 'K' or user_second_card =='k':
    user_hand2 = cards_Deck['K']
elif user_second_card == '2':
    user_hand2 == cards_Deck['2']
elif user_second_card == '3':
    user_hand2 = cards_Deck['3']
elif user_second_card == '4':
    user_hand2 = cards_Deck['4']
elif user_second_card == '5':
    user_hand2 = cards_Deck['5']
elif user_second_card == '6':
    user_hand2 = cards_Deck['6']
elif user_second_card == '7':
    user_hand2 = cards_Deck['7']
elif user_second_card == '8':
    user_hand2 = cards_Deck['8']
elif user_second_card == '9':
    user_hand2 = cards_Deck['9']
elif user_second_card == '10':
    user_hand2 = cards_Deck['10']
#################################
if user_third_card == 'A' or user_third_card == 'a':
    user_hand3 = cards_Deck['A']
elif user_third_card == 'J' or user_third_card == 'j':
    user_hand3 = cards_Deck['J']
elif user_third_card == 'Q' or user_card == 'q':
    user_hand3 = cards_Deck['Q']
elif user_third_card == 'K' or user_third_card == 'k':
    user_hand3 = cards_Deck['K']
elif user_third_card == '2':
    user_hand3 = cards_Deck['2']
elif user_third_card == '3':
    user_hand3 = cards_Deck['3']
elif user_third_card == '4':
    user_hand3 = cards_Deck['4']
elif user_third_card == '5':
    user_hand3 = cards_Deck['5']
elif user_third_card == '6':
    user_hand3 = cards_Deck['6']
elif user_third_card == '7':
    user_hand3 = cards_Deck['7']
elif user_third_card == '8':
    user_hand3 = cards_Deck['8']
elif user_third_card == '9':
    user_hand3 = cards_Deck['9']
elif user_third_card == '10':
    user_hand3 = cards_Deck['10']
# the total amount for all three cards
total = user_hand + user_hand2 + user_hand3


# if statement to properly give out the best advice.
if  total < 17:
    print(total,"Hit")
elif total >= 17 and total < 21:
    print(total,"stay")
elif total == 21:
    print(total, "Blackjack!")
elif total > 21:
    print(total,"Already busted")

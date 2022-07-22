cards = {
     "ace" : 1,
     "2" : 2,
     "3" : 3,
     "4" : 4,
     "5" : 5,
     "6" : 6,
     "7" : 7,
     "8" : 8,
     "9" : 9,
     "10" : 10,
     "jack" : 10,
     "queen" : 10,
     "king" : 10,
  }
  
  
users_card1 = input("\nEnter the first card ")
users_card2 = input("\nEnter the second card ")
users_card3 = input("\nEnter the third card ")

print(cards[users_card1])
print(cards[users_card2])
print(cards[users_card3])
cards_played = cards[users_card1] + cards[users_card2] + cards[users_card3]
print(cards_played)
if cards_played <= 17 and cards_played < 21:
     print("Hit")
if cards_played >= 18 and cards_played < 21:
     print("stay")
if cards_played == 21:
     print("Blackjack!!")
if cards_played >= 22:
     print("Already Busted!")             

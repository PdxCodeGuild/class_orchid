#blackjack advice

cards = {
    'a':'a',
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'j':10,
    'q':10,
    'k':10
}

def scoring(cardTotal):
    hit = False
    if cardTotal > 21:
        print(f"{cardTotal}, Bust...")
    elif cardTotal == 21:
        print(f"{cardTotal}! BlackJack!")
    elif cardTotal < 17:
        print(f"{cardTotal}, recommend Hit.")
        hit = True
    elif cardTotal >= 17:
            print(f"{cardTotal}, recommend Stay")
    return hit

print('Welcome to BlackJack Advice, to use this tool input a number or letter corresponding to the cards in hand.')
game = 'y'

while game == 'y':

    card1 = str(input('What is your first card?\n> '))
    card2 = str(input('What is your second card?\n> '))
    card3 = str(input('What is your third card?\n> '))

    cardHand = [cards[card1], cards[card2], cards[card3]]
    cardTotal = 0
    aceTotal = 0

    for card in cardHand: #checks for aces
        if card == 'a':
            aceTotal += 1
            cardTotal += 11
        else:
            cardTotal += card

    for ace in range(aceTotal):
        if cardTotal > 21:
            cardTotal -= 10 #brings Ace value to 1 for each Ace in hand that takes total over 21

    hit = scoring(cardTotal)
    
    while hit == True:

        conTinue = str(input("Did you Hit? (y/n)\n> ")).lower()

        if conTinue == 'y':
            nextCard = str(input('What is your next card?\n> ')) #allows for another card to be drawn
            if nextCard == 'a':
                cardTotal += 1
                if cardTotal <= 11:
                    cardTotal += 10
            else:
                cardTotal += cards[nextCard]
                # print(cards[nextCard]) #its haunted
        
        hit = scoring(cardTotal)

    game = str(input("Another round? (y/n)\n> "))
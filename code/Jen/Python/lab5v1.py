'''I need tuples for all the cards. I need to set up the inputs for the cards. I need a running total'''



cards = {'K' : 10,
        'Q' : 10,
        'J' : 10, 
        '10' : 10,
        '9' : 9,
        '8' : 8,
        '7' : 7,
        '6' : 6, 
        '5' : 5,
        '4' : 4,
        '3' : 3,
        '2' : 2,
        'A' : 1,
}

runningcards = []

runningtotal = 0


def recs():
    while int(runningtotal) in range(1, 17):
        print(f"Your total equals {runningtotal}. You are advised to Hit.")
        break

    while int(runningtotal) in range (17,21):
        print(f"Your total equals {runningtotal}. You are advised to stay.")
        quit()

    while int(runningtotal) == (21):
        print("BLACKJACK!")
        quit()

    while int(runningtotal) > 21: 
        print("BUSTED!")
        quit()


first_card = input("What is your first card? ")
runningcards.append(cards.get(first_card))
first_input = int(cards.get(first_card))
runningtotal = first_input
recs()

second_card = input("What is your second card? ")
runningcards.append(cards.get(second_card))
second_input = int(cards.get(second_card))
runningtotal = runningtotal + second_input
recs()

third_card = input("What is your third card? ")
runningcards.append(cards.get(third_card))
third_input = int(cards.get(third_card))
runningtotal = runningtotal + third_input
recs()

'''Jen Williams
PDX Code Guild Bootcamp
Class Orchid
lab 8: Credit Card Validation'''


cardlist = []

startnumber = input("Please enter your credit card number. ")

for char in startnumber:
        cardlist.append(char) 
        char = int(char)
print(cardlist)

if len(cardlist) != 16: 
    print("You have entered an invalid number. Please try again.")

checkdigit = cardlist[15]
cardlist = (cardlist[:15:])
print(cardlist)

cardlist.reverse()
print(cardlist)

cardlist_ints = [int(number) for number in cardlist]
print(cardlist_ints)

for i, number in enumerate(cardlist_ints):
    odd = i
    if odd % 2 == 0 : 
        cardlist_ints[i] = cardlist_ints[i] * 2

print(cardlist_ints)

for i, number in enumerate(cardlist_ints):
    if number > 9:
        cardlist_ints[i] -= 9

print(cardlist_ints)

total = sum(cardlist_ints)

print(total)
print(checkdigit)
seconddigit = total % 10
print(seconddigit)
if int(seconddigit) == int(checkdigit):
    print("You have entered a valid card number.")
else:
    print("The card number you have entered is not valid.")


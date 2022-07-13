'''Jen Williams
PDX Code Guild Bootcamp
lab 1: Unit Converter'''





distance = input("What is the distance? ")
unitin = input("What are the input units? Choose mi for miles, ft for feet, or m for meters. ")
unitout = input("What would you like to convert to? Choose mi for miles, ft for feet, m for meter or km for kilometer. ")

if unitin == unitout: 
    x = 1

elif unitin == "mi": 
    if unitout == "m":
        x = 1609.34
    elif unitout == "km":
        x = 1.60934
    elif unitout == "ft":
        x = 1609.34 * 1/0.348

elif unitin == "ft":
    if unitout == "m":
        x = 0.3048
    elif unitout == "km":
        x = .0003048
    elif unitout == "mi":
        x = .3048 * 1/1609.34

elif unitin == "m":
    if unitout == "mi":
        x = 1/1609.34
    elif unitout == "ft":
        x = 1/0.3048
    elif unitout == "km":
        x = 1000
else:
    print("You have chosen an invalid input. Please choose from the available options")
    quit()

distance = float(distance)
output = round(distance * x, 4)

print (f"{distance} {unitin} = {output} {unitout}")




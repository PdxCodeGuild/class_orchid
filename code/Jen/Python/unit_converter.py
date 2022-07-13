'''Jen Williams
PDX Code Guild Bootcamp
lab 1: Unit Converter
Revision 1'''




distance = input("What is the distance? ")
unitin = input("What are the input units? Choose mi for miles, ft for feet, or m for meters. ")
unitout = input("What would you like to convert to? Choose mi for miles, ft for feet, m for meter or km for kilometer. ")
distance = int(distance)

if unitin == "mi": 
    meterdistance = distance * 1609.34

elif unitin == "ft":
    meterdistance = distance * .3048

elif unitin == "m":
    meterdistance = distance * 1

elif unitin == "km":
    meterdistance = distance * 1000

else:
    print("You have chosen an invalid input. Please choose from the available options")
    quit()

#distance = float(distance)
#output = round(distance * x, 4)

if unitout == "mi":
    output = meterdistance * 1/1609.334

elif unitout == "ft":
    output = meterdistance * 1/0.3048

elif unitout == "m":
    output = meterdistance * 1

elif unitout == "km":
    output = meterdistance * 1/1000

output = round(output , 4)

print (f"{distance} {unitin} = {output} {unitout}")





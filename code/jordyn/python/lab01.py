# meter = 1
# foot = 0.3048
# mile = 1609.34
# kilometer = 1000
# yard = 0.9144
# inch = 0.0254

loop = 'y'


#Feet to Meters Conversion
# while loop == 'y':

#     conversion = int(input("This is a Feet to Meters Converter.\nFeet: ")) * foot

#     print(str(conversion) + 'm')

#     loop = input("Type y to convert again.\n> ")

#Multi-Unit Conversion

# unit_select_print = "\nAvailable conversions are:\n1 - Feet\n2 - Mile\n3 - Kilometer"

# print("This is a Unit to Meter converter." + unit_select_print)

# while loop == 'y':

#     unit_select = int(input("Please make a numerical selection: "))

#     unit_count = int(input("Unit Count: "))

#     if unit_select == 1:
#         unit_convert = foot * unit_count
#         print(str(unit_convert) + 'm')

#     elif unit_select == 2:
#         unit_convert = mile * unit_count
#         print(str(unit_convert) + 'm')

#     elif unit_select == 3:
#         unit_convert = kilometer * unit_count
#         print(str(unit_convert) + 'm')

#     else:
#         print("\nSelection out of range." + unit_select_print + "\n")
    
#     loop = str(input("Would you like to convert again? (y/n)".lower()))
#     if loop == 'y':
#         print(unit_select_print)

#Multi-Unit Conversion Expanded

# unit_select_print = "\nAvailable conversions are:\n1 - Feet\n2 - Mile\n3 - Kilometer\n4 - Yard\n5 - Inch"

# print("This is a Unit to Meter converter." + unit_select_print)

# while loop == 'y':

#     unit_select = int(input("Please make a numerical selection: "))

#     unit_count = int(input("Unit Count: "))

#     if unit_select == 1:
#         unit_convert = foot * unit_count
#         print(str(unit_convert) + 'm')

#     elif unit_select == 2:
#         unit_convert = mile * unit_count
#         print(str(unit_convert) + 'm')

#     elif unit_select == 3:
#         unit_convert = kilometer * unit_count
#         print(str(unit_convert) + 'm')
    
#     elif unit_select == 4:
#         unit_convert = yard * unit_count
#         print(str(unit_convert) + 'm')

#     elif unit_select == 5:
#         unit_convert = inch * unit_count
#         print(str(unit_convert) + 'm')

#     else:
#         print("\nSelection out of range." + unit_select_print + "\n")
    
#     loop = str(input("Would you like to convert again? (y/n)".lower()))
#     if loop == 'y':
#         print(unit_select_print)

#Multi-Unit Conversion with Unit To Unit Selection

selections = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}

loop = 'y'

# selection_select = input() #Testing if plugging in an input can choose a dictionary entry.
# print(selections[selection_select]) 

unit_select_print = "\nAvailable conversions are:\n> ft\n> mi\n> km\n> yd\n> in"

print("This is a Unit to Unit converter." + unit_select_print)

while loop == 'y':

    unit_select_1 = str(input("Please make an abbreviated selection: ")).lower() #Known measurement type

    unit_select_2 = str(input("Please make another Selection: ")).lower() #Desired meansurement type

    unit_count = float(input(f'{str(unit_select_1)}' + " Count: ")) #Known measurement value

    unit_1_meters = unit_count * selections.get(unit_select_1)
    # print(str(unit_1_meters) + 'm') #testing meter conversion math
    unit_2_meters = unit_1_meters / selections.get(unit_select_2)
    unit_2_meters = "{:.3f}".format(unit_2_meters)
    # print(str(unit_2_meters) + str(unit_select_2)) #testing

    print(f'{unit_count}{unit_select_1} converts to {unit_2_meters}{unit_select_2}')

    loop = str(input("Would you like to convert again? (y/n)").lower())
    if loop == 'y':
        print(unit_select_print)
    elif loop != 'y':
        print("Thank you for using my converter! Bye!")
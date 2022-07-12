meter = 1
foot = 0.3048
mile = 1609.34
kilometer = 1000
yard = 0.9144
inch = 0.0254

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

unit_select_print = "\nAvailable conversions are:\n> ft\n> mi\n> km\n> yd\n> in"

print("This is a Unit to Unit converter." + unit_select_print)

while loop == 'y':

    unit_select_1 = str(input("Please make an abbreviated selection: ")).lower()

    unit_select_2 = str(input("Please make another Selection: ")).lower()

    unit_count = float(input(f'{str(unit_select_1)}' + " Count: "))

    if unit_select_1 == 'ft':
        unit_1_convert = unit_count * foot
        if unit_select_2 == 'ft':
            print("Why are you doing this to me")
        elif unit_select_2 == 'mi':
            unit_2_convert = unit_1_convert / mile
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "mi")
        elif unit_select_2 == 'km':
            unit_2_convert = unit_1_convert / kilometer
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "km")
        elif unit_select_2 == 'yd':
            unit_2_convert = unit_1_convert / yard
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "yd")
        elif unit_select_2 == 'in':
            unit_2_convert = unit_1_convert / inch
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "in")
    
    elif unit_select_1 == 'mi':
        unit_1_convert = unit_count * mile
        if unit_select_2 == 'ft':
            unit_2_convert = unit_1_convert / foot
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "ft")
        elif unit_select_2 == 'mi':
            print("Why are you doing this to me")
        elif unit_select_2 == 'km':
            unit_2_convert = unit_1_convert / kilometer
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "km")
        elif unit_select_2 == 'yd':
            unit_2_convert = unit_1_convert / yard
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "yd")
        elif unit_select_2 == 'in':
            unit_2_convert = unit_1_convert / inch
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "in")
        
    elif unit_select_1 == 'km':
        unit_1_convert = unit_count * kilometer
        if unit_select_2 == 'ft':
            unit_2_convert = unit_1_convert / foot
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "ft")
        elif unit_select_2 == 'mi':
            unit_2_convert = unit_1_convert / mile
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "mi")
        elif unit_select_2 == 'km':
            print("Why are you doing this to me")
        elif unit_select_2 == 'yd':
            unit_2_convert = unit_1_convert / yard
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "yd")
        elif unit_select_2 == 'in':
            unit_2_convert = unit_1_convert / inch
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "in")

    elif unit_select_1 == 'yd':
        unit_1_convert = unit_count * yard
        if unit_select_2 == 'ft':
            unit_2_convert = unit_1_convert / foot
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "ft")
        elif unit_select_2 == 'mi':
            unit_2_convert = unit_1_convert / mile
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "mi")
        elif unit_select_2 == 'km':
            unit_2_convert = unit_1_convert / kilometer
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "km")
        elif unit_select_2 == 'yd':
            print("Why are you doing this to me")
        elif unit_select_2 == 'in':
            unit_2_convert = unit_1_convert / inch
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "in")

    elif unit_select_1 == 'in':
        unit_1_convert = unit_count * inch
        if unit_select_2 == 'ft':
            unit_2_convert = unit_1_convert / foot
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "ft")
        elif unit_select_2 == 'mi':
            unit_2_convert = unit_1_convert / mile
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "mi")
        elif unit_select_2 == 'km':
            unit_2_convert = unit_1_convert / kilometer
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "km")
        elif unit_select_2 == 'yd':
            unit_2_convert = unit_1_convert / yard
            unit_2_convert = "{:.3f}".format(unit_2_convert)
            print(str(unit_2_convert) + "yd")
        elif unit_select_2 == 'in':
            print("Why are you doing this to me")
    
    else:
        print("Please make sure to use the abbreviations provided.")
    
    loop = str(input("Would you like to convert again? (y/n)".lower()))
    if loop == 'y':
        print(unit_select_print)
    elif loop != 'y':
        print("Thank you for using my converter! Bye!")
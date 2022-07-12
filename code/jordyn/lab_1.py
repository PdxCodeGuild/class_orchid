meter = 1
foot = 0.3048
mile = 1609.34
kilometer = 1000

loop = 'y'


#Feet to Meters Conversion
# while loop == 'y':

#     conversion = int(input("This is a Feet to Meters Converter.\nFeet: ")) * foot

#     print(str(conversion) + 'm')

#     loop = input("Type y to convert again.\n> ")

#Multi-Unit Conversion

unit_select_print = "\nAvailable conversions are:\n1 - Feet\n2 - Mile\n3 - Kilometer"

print("This is a Unit to Meter converter." + unit_select_print)

while loop == 'y':

    unit_select = int(input("Please make a numerical selection: "))

    unit_count = int(input("Unit Count: "))

    if unit_select == 1:
        unit_convert = foot * unit_count
        print(unit_convert)

    elif unit_select == 2:
        unit_convert = mile * unit_count
        print(unit_convert)

    elif unit_select == 3:
        unit_convert = kilometer * unit_count
        print(unit_convert)

    else:
        print("\nSelection out of range." + unit_select_print + "\n")
    
    loop = str(input("Would you like to convert again? (y/n)".lower()))
    if loop == 'y':
        print(unit_select_print)
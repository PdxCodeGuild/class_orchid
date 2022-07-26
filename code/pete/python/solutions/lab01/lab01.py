"""
Version 1
Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m.
So we can get the output in meters by multiplying the input distance by 0.3048.
"""

print('Welcome to Unit Converter Mk 1.')
# prompt user for feet (number)
distance_in_feet = input('Please enter a number of feet to be converted to meters: ')
# convert to float
distance_in_feet = float(distance_in_feet)
# multiply by feet to meters conversion amount
distance_in_meters = distance_in_feet * 0.3048
# round to 4 digits past the decimal point
distance_in_meters = round(distance_in_meters, 4)
# print the result to the user
print(f'{distance_in_feet} ft is {distance_in_meters} m')


"""
Version 2
Allow the user to also enter the units. Then depending on the units, convert the distance into meters.
The units we'll allow are feet, miles, meters, and kilometers.
"""

conversion_to_meters = {
#    key: value
    'ft': 0.3048,
    'mi': 1609.34,
    'm' : 1,
    'km': 1000,
}
print('Welcome to Unit Converter Mk 2.')
conversion_unit = input('Please enter a unit to convert to meters (ft, mi, m, km): ')
conversion_distance = float(input(f'Please enter the amount of {conversion_unit} to be converted to meters: '))
# conversion_distance = float(conversion_distance) # using another line to convert to float
conversion_multiplier = conversion_to_meters[conversion_unit] # uses the string conversion_unit ('ft', 'mi', 'm', 'km') to look up the 
# float value in the dictionary
print(conversion_unit, conversion_distance, conversion_multiplier)
# instead of a hard-coded 0.3048, this version is using a value from the dictionary
distance_in_meters = conversion_distance * conversion_multiplier
distance_in_meters = round(distance_in_meters, 4)
print(f'{conversion_distance} {conversion_unit} is {distance_in_meters} m')

"""
Version 3
Add support for yards, and inches.
"""

conversion_to_meters = {
#    key: value
    'ft': 0.3048,
    'mi': 1609.34,
    'm' : 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254,
}
print('Welcome to Unit Converter Mk 3.')
conversion_unit = input('Please enter a unit to convert to meters (ft, mi, m, km, yd, in): ')
conversion_distance = float(input(f'Please enter the amount of {conversion_unit} to be converted to meters: '))
# conversion_distance = float(conversion_distance) # using another line to convert to float
conversion_multiplier = conversion_to_meters[conversion_unit] # uses the string conversion_unit ('ft', 'mi', 'm', 'km') to look up the 
# float value in the dictionary
# instead of a hard-coded 0.3048, this version is using a value from the dictionary
distance_in_meters = conversion_distance * conversion_multiplier
distance_in_meters = round(distance_in_meters, 4)
print(f'{conversion_distance} {conversion_unit} is {distance_in_meters} m')

"""
Version 4
Now we'll ask the user for the distance, the starting units, and the units to convert to.
"""

conversion_to_meters = {
#    key: value
    'ft': 0.3048,
    'mi': 1609.34,
    'm' : 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254,
}

conversion_from_meters = {
#    key: value
    'ft': 1 / 0.3048,
    'mi': 1 / 1609.34,
    'm' : 1,
    'km': 1 / 1000,
    'yd': 1 / 0.9144,
    'in': 1 / 0.0254,
}
print('Welcome to Unit Converter Mk 4.')
input_unit = input('Please enter a unit to be converted (ft, mi, m, km, yd, in): ')
input_distance = float(input(f'Please enter the amount of {input_unit} to be converted: '))
output_unit = input(f'Please enter the unit you would like to convert {input_distance} {input_unit} to (ft, mi, m, km, yd, in): ')
# print(input_unit, input_distance, output_unit)
distance_in_meters = input_distance * conversion_to_meters[input_unit]
output_distance = round(distance_in_meters * conversion_from_meters[output_unit], 4)
print(f'{input_distance} {input_unit} is {output_distance} {output_unit}')
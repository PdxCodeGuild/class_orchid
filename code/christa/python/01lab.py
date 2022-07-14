#Version1

"""feet = 0.3048
convert = input("Enter the number of feet would you like converted: ")
convert = int(convert)

total = convert * feet
print(f'{convert} feet is {total} meters.')"""

#Version2 and #Version3
#My Dictionary of units to convert to meters
conversion_table = { 'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,}
#Added units to dictionary
conversion_table['yds'] = 0.9144
conversion_table['in'] = 0.0254
#naming the input to distance to enable conversion and identifying type as an integer
distance = input("What is the distance? ")
distance = int(distance)
#unit = input("What are the units? ") #initial input to name unit of measure to convert from
#value = conversion_table[unit] #converting the input to a value identifiable in the conversion table
#total = value * distance #converting the input and distance to meters

#print(f"{distance} {unit} is {total} meters ") #providing the answer to the user

#Version4
#naming the units of measure from and to to identify conversion formula
from_units = input("What are the input units? ")
to_units = input("What are the output units? ")
meter_d = conversion_table[from_units]*distance #convert the input distance to meters
#print(meter_d)

to_meters = meter_d*conversion_table[to_units]   #convert to meters
from_meters = meter_d/conversion_table[to_units]  #convert from meters to desired output
#Conditionals, only two are needed. Either to meters or anything else.
if from_units == 'm':
    from_meters = meter_d/conversion_table[to_units]
    message = (f"{distance} {from_units} are {from_meters}{to_units}")
else:
    to_meters = meter_d*conversion_table[to_units]
    message = (f"{distance}{from_units} are {to_meters}{to_units}")

print(message)

# Dictionary that has the units I would like to use to convert. 
units  = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254
}


distance_enter = input('what is the distance? ') # Input for user to enter a number

distance_enter = float(distance_enter) # Converts the variable to a float.

input_units = input('what are the units? enter ft, mi, m, km, yd, or in : ') # Prompt to ask for input units 

output_units = input('what are the ouput units? enter ft, mi, m, km, yd, or in : ')

meters_total = distance_enter * units[input_units] # converts line enter to meters.

result = meters_total / units[output_units]

# meters_total =   # units[output_units] / meters_total


# this line will print out the results and I used the round function to round up two decimals for easier reading. 

print(f'{distance_enter} {input_units} is {round(result, 2)} {output_units}') 

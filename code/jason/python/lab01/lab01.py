import random
import numbers

conversion_units = {
    'feet' : 0.3048,
    'miles' : 1609.34,
    'meters' : 1,
    'kilometers' : 1000,
    'yard' : 0.9144,
    'inches' : 0.0254,
}

print("\nWelcome to this Unit Converter\n")

unit_conversion = input("\n Input a distance?: ")

distance_conversion = int(unit_conversion)

user_output_unit = input("\nWhat is your ouput for unit?: ")

print (conversion_units[user_output_unit] * distance_conversion)



distance_input = input("What is the distance you want to use?: ")

conversion_to_meters = input("What is the unit of measurement you want to use?: ")

user_output_unit = input("What is the output you want to use?: " )

distance_input = int(distance_input)

meters_to_conversion = {
    'feet': 0.3048,
    'miles': 1609.34,
    'meters': 1,
    'kilometers': 1000,
    'yards': 0.9144,
    'inches': 0.0254,
}

distance_in_meters = distance_input * meters_to_conversion.get(conversion_to_meters)

final_distance = distance_in_meters / meters_to_conversion.get(user_output_unit)

print(final_distance)







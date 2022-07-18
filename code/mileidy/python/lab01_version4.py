converter = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
}

distance = input('what is the distance?: ')

units = input('what are the units?: ')

output_units = input('what are the output units?: ')

distance = int(distance)

final_distance = distance * converter[units] / converter[output_units] # 0.3048 / 1

print(f"{distance} {units} is {final_distance} {output_units}.")

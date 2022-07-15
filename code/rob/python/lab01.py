#version 1
user_input_feet = int(input('what is the distance in feet? '))
meters = round(user_input_feet * 0.3048, 4)

print(f'{user_input_feet} ft is {meters} m\n\n')


# #version 2
user_input_number = int(input('what is the distance in feet? '))
user_input_unit_v2 = input('what are the units? ')
convert_to_meters_v2 = {
    'ft': round(user_input_number * 0.3048, 4),
    'mi': round(user_input_number * 1609.34, 2),
    'm': user_input_number,
    'km': user_input_number * 1000
}

print(f'{user_input_number} {user_input_unit_v2} is {convert_to_meters_v2[user_input_unit_v2]} m\n\n')


# #version 3
user_input_number = int(input('what is the distance in feet? '))
user_input_unit = input('what are the units? ')
convert_to_meters = {
    'ft': round(user_input_number * 0.3048, 4),
    'mi': round(user_input_number * 1609.34, 2),
    'm': user_input_number,
    'km': user_input_number * 1000,
    'yd': round(user_input_number * 0.9144, 4),
    'inch': round(user_input_feet * 0.0254, 4)
}

print(f'{user_input_number} {user_input_unit} is {convert_to_meters[user_input_unit]} m\n\n')



#version 4
user_input_number = int(input('what is the distance in feet? '))
user_input_unit = input('what are the units? ')
user_output_unit = input('what are the output units? ')

convert_to_meters = {
    'ft': round(user_input_number * 0.3048, 4),
    'mi': round(user_input_number * 1609.34, 2),
    'm': user_input_number,
    'km': user_input_number * 1000,
    'yd': round(user_input_number * 0.9144, 4),
    'inch': round(user_input_number * 0.0254, 4)
}

convert_to_output = {
    'ft': round(convert_to_meters[user_input_unit] / 0.3048, 4),
    'mi': round(convert_to_meters[user_input_unit] / 1609.34, 4),
    'm': convert_to_meters[user_input_unit] / 1,
    'km': convert_to_meters[user_input_unit] / 1000,
    'yd': round(convert_to_meters[user_input_unit] / 0.9144, 4),
    'inch': round(convert_to_meters[user_input_unit])
}

print(f'{user_input_number} {user_input_unit} is {convert_to_output[user_output_unit]} {user_output_unit}\n\n')

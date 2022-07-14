units_dict = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}
user_distance = input('\nWhat is the distance?: ')
user_input_units = input('\nWhat are the input units?: ')
user_output_units  = input('\nWhat are the output units?: ')
user_distance = float(user_distance)

print(f"{user_distance} {user_input_units} is {round(units_dict[user_input_units] / units_dict[user_output_units] * user_distance, 2)} {user_output_units}")
# I did use my 102 lab as a reference, I did not complete my conversion chart in 102 though so this is new.


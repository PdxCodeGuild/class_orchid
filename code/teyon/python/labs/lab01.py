#create a dictionary with 4 units and there equivalent in meters
stored_units = {

    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000

}

#create a new dict with yards and inches
yd_in = {

    'yd': 0.9144,
    'in': 0.0254

}


#add the newly created dictionary to the previous dictionary
stored_units.update(yd_in)

#Print a welcome message to the user
print("\nWelcome to The Unit Converter!\n")

#we ask the user for the distance they are looking to have convert ro meters.
unit_distance = input("\nInput a distance? ")

#we convert the unit_distance from a string to an integer
converted_distance = int(unit_distance)

#ask the user which unit they are looking to convert into meters
ask_input_unit = input("\nWhat is your input unit? ")

#we take the stored units dict, and whichever unit the user inputs we pull the data stored in that unit
chosen_input = stored_units[ask_input_unit]


#we multiply the unit converted into meters by the distance the user chose. This gives us the data for the input unit
input_unit_data = converted_distance * chosen_input

#ask the user what output unit they are want it converted into.
ask_output_unit = input("\nWhat is your output unit? ")

#we go back into the stored unit dictionary, and pull the data from the ask_output_unit selected from the dictionary
chosen_output = stored_units[ask_output_unit]

#We are able to convert the input units into the output units, by converting the input unit and distance into meters
#Than taking the distance in meters and dividing it by data pulled from the output unit selected from the dictionary
final_outcome = input_unit_data / chosen_output

#print the final outcome
print(f"\n{unit_distance} {ask_input_unit} in {ask_output_unit} is {final_outcome} {ask_output_unit}.\n")



#  Lab 1: Unit Converter

# accept distance and perform a unit conversion
def convert(distance = None, unit_input = '', unit_output = ''):

    # dict to reference unit conversions to meters by name
    unit_conversions = {
        'ft': 0.3048,
    }

    # loop until all user input is validated
    while True:

        # catch errors and print meaningful output
        try:

            # input and validate unit of measure
            if not unit_input in unit_conversions:
                unit_input = input(f'Which measurement unit? ')
                if len(unit_input) < 1:
                    print('You must enter a value.')
                elif not unit_input in unit_conversions:
                    print(f'Conversion to "{unit_input}" is unsupported. Accepted units are {list(unit_conversions.keys())}.')
                continue   

            # input and pseudo-validate (catches error) distance
            distance = float(input(f'What is the distance in {unit_input}? '))
            break

        except ValueError:
            print('Input must be a number.')

        except KeyboardInterrupt:
            print('\nBye! :D')
            return

    # do the conversion   
    output_result = round(distance * unit_conversions[unit_input], 4)

    # print the result
    print(f'{output_result} {unit_output} in {distance} {unit_input}')

convert(unit_input = 'ft')

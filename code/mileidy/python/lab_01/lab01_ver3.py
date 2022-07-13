converter ={
    'ft': 0.3048,
    'mi': 1609.34,
    'm':1,
    'km':1000
}
#i changed the variable for this version and added in a line specifically for units
distance = input('what is the distance?: ')
units = input('what are the units?: ')
#i converted the number that the use put in to and int instead pf a string
distance = int(distance)
#i multiplied the int of distance by the integers in the dictionary and got access to the dictionaries value by adding units at the end
print(f"{distance} {units} is {distance * converter[units]} m.")

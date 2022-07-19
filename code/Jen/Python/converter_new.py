metconvtom = {
    'in' : .0254,
    'ft' : .3048,
    'y' : .9144,
    'm' : 1,
    'km' : 1000,
    'mi' : 1609.34,
}

metconvfromm = {
    'in' : 39.3700787,
    'ft' : 1/0.3048,
    'y' : 1.0936133,
    'm' : 1,
    'km' : 1/1000,
    'mi' : 1/1609.34,
}

initial_distance = input("What is the distance you would like converted? ")
unitsfrom = input("What unit of measurement are you converting from? Please choose in, ft, m, y, km, or mi. ")
unitsto = input("What unit of measurement are you converting to? Please choose in, ft, m, y, km, mi ")

start = float(metconvtom.get(unitsfrom))
to = float(metconvfromm.get(unitsto))

initconvert = float(initial_distance) * start

distance = float(initconvert) * to

print(f"{initial_distance} {unitsfrom} = {round(distance, 4)} {unitsto}")

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
    'mi' : 1/609.34,
}

distance = input("What is the distance you would like converted? ")
unitsfrom = input("What unit of measurement are you converting from? Please choose in, ft, m, y, km, or mi. ")
unitsto = input("What unit of measurement are you converting to? Please choose in, ft, m, y, km, mi ")

start = float(metconvtom.get(unitsfrom))
to = float(metconvfromm.get(unitsto))

initconvert = float(distance) * start

finalconvert = float(initconvert) * to

distance = round(start * to , 4)

print(distance)

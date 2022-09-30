const conversion = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254,
}

userDistance = prompt('What is the distance? ')
userInputUnits = prompt('What are the input units? ')
userOutputUnits  = prompt('What are the output units? ')
userDistance = Number(userDistance)

alert(`${userDistance} ${userInputUnits} is ${(conversion[userInputUnits] / conversion[userOutputUnits] * userDistance).toFixed(4)} ${userOutputUnits}`)
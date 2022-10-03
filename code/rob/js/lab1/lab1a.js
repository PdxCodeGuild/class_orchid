//version 1
userInput = prompt('what is the distance in feet?')

meters = userInput * 0.3048

alert(`distance in meters is: ${meters.toFixed(4)}`)

//verison 2
alert('version 2')
userNumber = prompt('what is the distance?')
userUints = prompt('what are the units?')

unitConverter = {
    ft: userNumber * 0.3048,
    mi: userNumber * 1609.34,
    m: userNumber * 1,
    km: userNumber * 1000,
}

meters = unitConverter[userUints]

alert(`${userNumber}${userUints} in meters is: ${meters}m`)

//version 3
alert('version 3')
userNumber = prompt('what is the distance?')
userUints = prompt('what are the units?')

unitConverter = {
    ft: userNumber * 0.3048,
    mi: userNumber * 1609.34,
    m: userNumber * 1,
    km: userNumber * 1000,
    yd: userNumber * 0.9144,
    inch: userNumber * 0.0254,
}

meters = unitConverter[userUints]

alert(`${userNumber}${userUints} in meters is: ${meters}m`)

//version 4
alert('version 4')
userNumber = prompt('what is the distance?')
userUints = prompt('what are the units?')
userToUnits = prompt('what are the output units?')

unitConverter = {
    ft: userNumber * 0.3048,
    mi: userNumber * 1609.34,
    m: userNumber * 1,
    km: userNumber * 1000,
    yd: userNumber * 0.9144,
    inch: userNumber * 0.0254,
}

outputUnits = {
    ft: unitConverter[userUints] / 0.3048,
    mi: unitConverter[userUints] / 1609.34,
    m: unitConverter[userUints] / 1,
    km: unitConverter[userUints] / 1000,
    yd: unitConverter[userUints] / 0.9144,
    inch: unitConverter[userUints] / 0.0254,
}

meters = unitConverter[userUints]

alert(`${userNumber}${userUints} in meters is: ${outputUnits[userToUnits]}${userToUnits}`)
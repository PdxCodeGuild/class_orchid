// unit converter - js lab 

const units = { "ft": 0.3048, "mi": 1609.34, "m": 1, "km": 1000, "yd": 0.9144, "in": 0.0254 }

const userInputNumDistance = prompt('what is the distance you would like to convert?')
const userInputUnits = prompt('what is the distance you would like to convert?ft, mi, m, km, yd, or in ')
const userOutputUnits = prompt('what is the distance you would like to convertft, mi, m, km, yd, or in ')

const metersTotal = userInputNumDistance * units[userInputUnits]
const result = metersTotal / units[userOutputUnits]

alert(Math.ceil(result) + " " + userOutputUnits)
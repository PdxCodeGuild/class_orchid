let units = {
    ft: 0.3048,
    mi: 1609.34,
    m: 1,
    km: 1000,
    yd: 0.9144,
    in: 0.0254,
}

let distanceEntered = prompt("What is the distance?")
let inputUnits = prompt('What was that in units? ft, mi, m, km, yd, or in ')
let outputUnits = prompt('And what would you like to convert that to? ft, mi, m, km, yd, or in ')

console.log(distanceEntered)
console.log(inputUnits)
console.log(outputUnits)

metersTotal = distanceEntered * units[inputUnits]

results = metersTotal / units[outputUnits]

console.log(results + ' ' + outputUnits)


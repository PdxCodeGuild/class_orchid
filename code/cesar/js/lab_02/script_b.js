const units = { "ft": 0.3048, "mi": 1609.34, "m": 1, "km": 1000, "yd": 0.9144, "in": 0.0254 }

// const userInputNumDistance = prompt('what is the distance you would like to convert?')
// const userInputUnits = prompt('what is the distance you would like to convert?ft, mi, m, km, yd, or in ')
// const userOutputUnits = prompt('what is the distance you would like to convertft, mi, m, km, yd, or in ')

// const metersTotal = userInputNumDistance * units[userInputUnits]
// const result = metersTotal / units[userOutputUnits]

// alert(Math.ceil(result) + " " + userOutputUnits)


let getDistance = document.getElementById('distance')
let getUnits = document.getElementById('units')
let submitBtn = document.getElementById('submit')
let getConvertUnits = document.getElementById('convertunits')

submitBtn.addEventListener('click', function () {
    let metersTotal = getDistance.value * units[getUnits.value]
    let results = metersTotal / units[getConvertUnits.value]
    alert(results + " " + getConvertUnits.value)
})



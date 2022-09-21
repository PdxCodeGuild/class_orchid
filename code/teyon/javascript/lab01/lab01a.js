const storedUnits = {ft: 0.30848, mi:1609.34, m: 1, km: 1000, yd: 0.9144, in: 0.0254}

let askUser = prompt("Input distance: ")

let convertUnit = parseInt(askUser)
let askUnit = prompt("What unit")

let chosenInput = storedUnits[askUnit]

let inputUnitdata = convertUnit * chosenInput

let askOutputunit = prompt("What is your output unit?")

let chosenOutput = storedUnits[askOutputunit]

finalOutcome = inputUnitdata / chosenOutput

alert(`the final outcome is ${finalOutcome}${askOutputunit}`)







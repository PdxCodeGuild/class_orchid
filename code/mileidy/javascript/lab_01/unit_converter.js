
const unitConverter = {'ft': 0.3048,'mi': 1609.34,'m': 1,'km': 1000,'yrd': 0.9144,'in': 0.0254}

let distance = prompt("Please enter the distance")

let units = prompt("Please enter the units")

let calculation = distance * unitConverter[units]
alert(`${distance} ${units} is ${calculation}m.`)
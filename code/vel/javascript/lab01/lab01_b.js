// add button and input 
let convert_Button = document.getElementById('run_bt')
let output_div = document.getElementById('output_div')


const conversion = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254,
}

convert_Button.addEventListener('click', function() {
    
    let userDistance = document.getElementById('distance').value
    let userInputUnits = document.getElementById('input_units').value
    let userOutputUnits  = document.getElementById('output_units').value
    output_div.innerHTML = `${userDistance} ${userInputUnits} is ${(conversion[userInputUnits] / conversion[userOutputUnits] * userDistance).toFixed(4)} ${userOutputUnits}`
    }
)

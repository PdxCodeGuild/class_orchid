const userDistance = document.querySelector('#input')
const userUnit = document.querySelector('#unit')
const userToUnit = document.querySelector('#toUnit')
const convertButton = document.querySelector('#convert')
const outputToUl = document.querySelector('#output')

convertButton.addEventListener('click', convert)

//version 4
function convert(){
    userNumber = userDistance.value
    userUints = userUnit.value
    userToUnits = userToUnit.value

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

    const outputDiv = document.createElement('div')
    outputDiv.classList.add('outputContainer')

    const output = document.createElement('li')
    output.innerText = `${userNumber}${userUints} in meters is: ${outputUnits[userToUnits]}${userToUnits}`
    outputDiv.appendChild(output)
    outputToUl.appendChild(outputDiv)
    console.log(outputDiv)

}

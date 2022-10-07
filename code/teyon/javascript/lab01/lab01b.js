
let submit = document.querySelector("#submit")

submit.addEventListener('click', function(){

    let unitDistance = document.querySelector("#distance").value;
    
    let inputUnit = document.querySelector("#firstunit").value;
    
    let outputUnit = document.querySelector("#secondunit").value;

    const storedUnits = {ft: 0.30848, mi:1609.34, m: 1, km: 1000, yd: 0.9144, in: 0.0254}
    let convertUnit = parseInt(unitDistance)
    let chosenInput = storedUnits[inputUnit]
    let inputUnitdata = convertUnit * chosenInput
    let chosenOutput = storedUnits[outputUnit]

    let finalOutcome = inputUnitdata / chosenOutput

    let finalOutput = document.querySelector("#output")
    
    finalOutput.innerHTML = finalOutcome

})

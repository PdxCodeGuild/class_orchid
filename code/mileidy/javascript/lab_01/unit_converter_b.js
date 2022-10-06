let distance = document.getElementById('distance')
let submit = document.getElementById('submit')
let units =  document.getElementById('units')
let results =  document.getElementById('results')

submit.addEventListener('click', function() {
    let calculation = distance.value * unitConverter[units.value]
    results.innerHTML = `${calculation}m.`

});

const unitConverter = {'ft': 0.3048,'mi': 1609.34,'m': 1,'km': 1000,'yrd': 0.9144,'in': 0.0254}


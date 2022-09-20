let enter = document.getElementById('enter')

enter.addEventListener('click', function(){
    let distance = document.getElementById('distance').value
    let unit = document.getElementById('unit').value
    let unit2 = document.getElementById('unit2').value
    let results = document.getElementById('result')

    
    if (unit == 'ft'){
        storeMath = 0.3048
    }
    else if (unit == 'mi') {
        storeMath = 1609.34
    }
    else if (unit == 'm') {
        storeMath = 1
    }
    else if (unit == 'km') {
        storeMath = 1000
    }
    else if (unit == 'yard') {
        storeMath = 0.9144
    }
    else if (unit == 'inch') {
        storeMath = 0.0254
    }
    
    if (unit2 == 'ft'){
        storeMath2 = 0.3048
    }
    else if (unit2 == 'mi'){
        storeMath2 = 1609.34
    }
    else if (unit2 == 'm'){
        storeMath2 = 1
    }
    else if (unit2 == 'km'){
        storeMath2 = 1000
    }
    else if (unit2 == 'yard'){
        storeMath2 = 0.9144
    }
    else if (unit2 == 'inch'){
        storeMath2 = 0.0254
    }
    let conversion = distance * storeMath
    let finalCon = conversion/storeMath2
    results.innerHTML = finalCon
    
}
)
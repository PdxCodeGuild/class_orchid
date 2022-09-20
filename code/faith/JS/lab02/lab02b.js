let enter = document.getElementById('enter')

enter.addEventListener('click', function(){
    let distance = document.getElementById('distance').value
    let unit = document.getElementById('unit').value
    let unit2 = document.getElementById('unit2').value
    let results = document.getElementById('result')

    
    if (unit == 'ft'){
        result = distance * 0.3048
    }
    else if (unit == 'mi') {
        result = distance * 1609.34
    }
    else if (unit == 'm') {
        result = distance
    }
    else if (unit == 'km') {
        result = distance * 1000
    }
    else if (unit == 'yard') {
        result = distance * 0.9144
    }
    else if (unit == 'inch') {
        result = distance * 0.0254
    }
    
    if (unit2 == 'ft'){
        result/0.3048
    }
    else if (unit2 == 'mi'){
        result/1609.34
    }
    else if (unit2 == 'm'){
        result 
    }
    else if (unit2 == 'km'){
        result/1000
    }
    else if (unit2 == 'yard'){
        result/0.9144
    }
    else if (unit2 == 'inch'){
        result/0.0254
    }
    
    results.innerHTML = result
    console.log(result)
}
)
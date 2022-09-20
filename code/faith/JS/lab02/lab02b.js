let enter = document.getElementById('enter')

enter.addEventListener('click', function(){
    let distance = document.getElementById('distance')
    let unit = document.getElementById('unit')
    let unit2 = document.getElementById('unit2')
    let result = document.getElementById('result')

    
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
        return result/0.3048
    }
    else if (unit2 == 'mi'){
        return result/1609.34
    }
    else if (unit2 == 'm'){
        return(result)
    }
    else if (unit2 == 'km'){
        return result/1000
    }
    else if (unit2 == 'yard'){
        return result/0.9144
    }
    else if (unit2 == 'inch'){
        return result/0.0254
    }
    
    result.innerHtml = result
    console.log(result)
}
)
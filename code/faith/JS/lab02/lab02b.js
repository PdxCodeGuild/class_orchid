let distance = document.getElementById('distance')
let unit = document.getElementById('unit')
let unit2 = document.getElementById('unit2')
let enter = document.getElementById('enter')


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
    console.log(result/0.3048)
}
else if (unit2 == 'mi'){
    console.log(result/1609.34)
}
else if (unit2 == 'm'){
    console.log(result)
}
else if (unit2 == 'km'){
    console.log(result/1000)
}
else if (unit2 == 'yard'){
    console.log(result/0.9144)
}
else if (unit2 == 'inch'){
    console.log(result/0.0254)
}

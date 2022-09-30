let chart = document.getElementById('chart')
let input = document.getElementById('input')

let data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
input.setAttribute('value', data.join(','))

function plot() {
    let range = (b,e)=>[...Array(e).keys()].slice(b).reverse() // build an array of values ranging from b to e
    let str = ''
    data = input.value.split(',').map(e=>parseInt(e))
    let greatest = data.slice().sort((a,b)=>b-a)[0]
    range(0,greatest).forEach(i=>{
        data.forEach((v,index)=>{
            if (v > i) { str += '█' } // plot on the chart
            else { str += ' ' } // don't plot
        })
        if (i >= 1) { str += '\n' }
    })
    chart.innerText = `${str}`
}

plot()

input.addEventListener('input',(e)=> (/^\d+(,\d+)+$/.exec(input.value)) && plot())

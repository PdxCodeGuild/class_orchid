let data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
data = prompt('From Python Lab 9 - Peaks and Valleys\nEnter a series of comma-separated integers: ', data).split(',').map(e=>parseInt(e))
let greatest = data.slice().sort((a,b)=>b-a)[0]

// build an array of values ranging from b to e
let range = (b,e)=>[...Array(e).keys()].slice(b).reverse()

let str = ''

range(0,greatest).forEach(i=>{
    data.forEach((v,index)=>{
        if (v > i) { str += '█' } // plot on the chart
        else { str += ' ' } // don't plot
    })
    if (i >= 1) { str += '\n' }
})

alert(`From Python Lab 9 - Peaks and Valleys\n${str}`)
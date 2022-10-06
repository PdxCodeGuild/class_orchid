let output = document.querySelector('#output')
let input = document.querySelector('#input')

function validateCard(num) {
    check = num.pop()
    compare = num.reverse()
        .map((v, i) => (i % 2) && v || v * 2)
        .map((v, i) => (v > 9) && v - 9 || v)
        .reduce((sum, n) => Number(n) + sum)
        .toString().split('').pop()
    return check == compare
}

function inputListener(e) {
    e.preventDefault()
    if (/^.{16}.*$/.exec(input.value)) {
        if (validateCard(input.value.split(''))) {
            output.innerHTML = '<span class="valid">VALID</span><br>'
        } else {
            output.innerHTML = '<span class="invalid">INVALID</span><br>'
        }
        input.value = ''
    }
}

input.addEventListener('input', inputListener)
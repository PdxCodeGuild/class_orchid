const button = document.querySelector('input[value="click to begin"]')

function validateCard(num) {
    check = num.pop()
    compare = num.reverse()
        .map((v, i) => (i % 2) && v || v * 2)
        .map((v, i) => (v > 9) && v - 9 || v)
        .reduce((sum, n) => Number(n) + sum)
        .toString().split('').pop()
    return check == compare
}

button.addEventListener('click', e => {
    let input = prompt('Please insert your stolen card now:\n(no spaces)')
    if (validateCard(input.split(''))) {
        alert('VALID')
    } else {
        alert('INVALID')
    }
})

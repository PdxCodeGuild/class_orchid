const hundreds = {
    0: '',
    1: 'one hundred',
    2: 'two hundred',
    3: 'three hundred',
    4: 'four hundred',
    5: 'five hundred',
    6: 'six hundred',
    7: 'seven hundred',
    8: 'eight hundred',
    9: 'nine hundred',
}

const tens = {
    0: '',
    1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'forthy',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}
const teens = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty'
}

const ones = {
    0: 'ten ',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

const numberInput = document.querySelector('#input')
const btn = document.querySelector('#btn')
btn.addEventListener('click', converter)


function converter() {
    let hundredsDigit = Math.floor(numberInput.value / 100)
    let tensDigit = Math.floor(numberInput.value / 10) % 10
    let onesDigit = numberInput.value % 10

    if (numberInput.value >= 100 && tensDigit === 1) {
        alert(hundreds[hundredsDigit] + ' ' + teens[Math.floor(numberInput.value / 100)]);
    } else if (numberInput.value >= 100 && onesDigit === 0 && tensDigit > 1) {
        alert(hundreds[hundredsDigit] + ' ' + tens[tensDigit])
    } else if (numberInput.value >= 100 && onesDigit === 0) {
        alert(hundreds[hundredsDigit])
    } else if (numberInput.value >= tensDigit === 0) {
        alert(hundreds[hundredsDigit] + ' ' + ones[onesDigit])
    } else if (numberInput.value >= 100) {
        alert(hundreds[hundredsDigit] + ' ' + tens[tensDigit] + ' ' + ones[onesDigit])
    } else if (numberInput.value >= 10 && numberInput.value <= 20) {
        alert(teens[numberInput.value % 100])
    } else if (numberInput.value > 20 && onesDigit == 0) {
        alert(tens[tensDigit])
    } else if (numberInput.value > 20) {
        alert(tens[tensDigit] + ' ' + ones[onesDigit])
    } else if (numberInput.value < 10 && numberInput.value >= 1) {
        alert(ones[onesDigit])
    } else if (numberInput.value == 0) {
        alert('Zero')
    } else {
        alert('Please enter a valid number from 0-999')
    }
}
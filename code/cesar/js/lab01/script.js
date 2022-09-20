//  Lab 1:  Numbers to Words
// Cesar Rebolled 

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

numberInput = prompt('Hello, please enter a number from 0-999 to convert into words: ')

let hundredsDigit = Math.floor(numberInput / 100)
let tensDigit = Math.floor(numberInput / 10) % 10
let onesDigit = numberInput % 10

console.log(hundredsDigit)
console.log(tensDigit)
console.log(onesDigit)

console.log('The number input was this: ' + numberInput)


if (numberInput >= 100 && tensDigit === 1) {
    console.log(hundreds[hundredsDigit] + ' ' + teens[Math.floor(numberInput / 100)]);
} else if (numberInput >= 100 && onesDigit === 0 && tensDigit > 1) {
    console.log(hundreds[hundredsDigit] + ' ' + tens[tensDigit])
} else if (numberInput >= 100 && onesDigit === 0) {
    console.log(hundreds[hundredsDigit])
} else if (numberInput >= tensDigit === 0) {
    console.log(hundreds[hundredsDigit] + ' ' + ones[onesDigit])
} else if (numberInput >= 100) {
    console.log(hundreds[hundredsDigit] + ' ' + tens[tensDigit] + ' ' + ones[onesDigit])
} else if (numberInput >= 10 && numberInput <= 20) {
    console.log(teens[numberInput % 100])
} else if (numberInput > 20 && onesDigit == 0) {
    console.log(tens[tensDigit])
} else if (numberInput > 20) {
    console.log(tens[tensDigit] + ' ' + ones[onesDigit])
} else if (numberInput < 10 && numberInput >= 1) {
    console.log(ones[onesDigit])
} else if (numberInput === 0) {
    console.log('Zero')
} else {
    console.log('Please enter a valid number from 0-999')
}




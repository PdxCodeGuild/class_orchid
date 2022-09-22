//  Lab3 - CC Validator Part A
// The credit card number to check is: 4556737586899855 i

let cardNum = document.getElementById('cardnum')
let submit = document.getElementById('submit')
let submitClick = submit.addEventListener('click', cardNum.value)

alert(submitClick.value)





function creditCardValidator(cardNum) {
    const arrayOfCardNum = Array.from(String(cardNum), Number)
    const checkDigit = arrayOfCardNum.pop()
    const reverseArrayOfCardNum = arrayOfCardNum.reverse()
    for (const [index, element] of reverseArrayOfCardNum.entries()) {
        if (index % 2 == 0) {
            let dubElement = reverseArrayOfCardNum[index] = element * 2
        }
    }
    for (const [index, element] of reverseArrayOfCardNum.entries()) {
        if (element > 9) {
            let greaterThanNineElement = reverseArrayOfCardNum[index] = element - 9
        }
    }
    const sumOfArray = reverseArrayOfCardNum.reduce((accumulator, value) => {
        return accumulator + value
    }, 0)
    const finalCheckDigit = sumOfArray % 10
    if (finalCheckDigit == checkDigit) {
        return true
    } else {
        return false
    }
}
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

const cardInputFromUser = prompt("Please enter a card number to validate")
const isCreditCardValid = creditCardValidator(cardInputFromUser)

if (isCreditCardValid) {
    alert("This credit card is VALID")
} else {
    alert("This credit card is NOT valid")
}
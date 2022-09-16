/* 
Lab 8: Credit Card Validation 
Cesar Rebolledo Class Orchid 
*/

let cardNumberInput = prompt('Enter your card number: ').split(",")
const arrayCardNumberInput = Array.from(String(cardNumberInput), Number)

function creditCardValidation(cardNumber) {
    checkDigit = cardNumber.pop()
    reverseCardNumberArray = cardNumber.reverse()
    console.log(reverseCardNumberArray)
    reverseCardNumberArray.forEach(function (num, i) {
        console.log(num, i)
    })


}

creditCardValidation(arrayCardNumberInput)
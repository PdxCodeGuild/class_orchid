let amountEntered = prompt("please enter dollar amount")

let amountInPennies = amountEntered * 100
let originalValue = amountInPennies

let quaters = Math.floor(amountInPennies / 25)
let quaterValue = quaters * 25
amountInPennies = amountInPennies - quaterValue
console.log(amountInPennies)

let dimes = Math.floor(amountInPennies / 10 )
let dimesValue = dimes * 10
amountInPennies = amountInPennies - dimesValue
console.log(amountInPennies)


let nickels = Math.floor(amountInPennies / 5)
let nickelsValue = nickels * 5
amountInPennies = amountInPennies - nickelsValue
console.log(amountInPennies)

let pennies = Math.floor(amountInPennies / 1)
console.log(pennies)
let penniesValue = pennies * 1
amountInPennies = amountInPennies - penniesValue
console.log(penniesValue)


alert(`${quaters} Quaters, ${dimes} Dimes, ${nickels} Nickels, ${pennies} Pennies`)













let submit = document.querySelector("#submit")

submit.addEventListener('click', function(){
    let amountEntered = document.querySelector("#useramount").value;

    let amountInPennies = amountEntered * 100
let originalValue = amountInPennies

let quaters = Math.floor(amountInPennies / 25)
let quaterValue = quaters * 25
amountInPennies = amountInPennies - quaterValue


let dimes = Math.floor(amountInPennies / 10 )
let dimesValue = dimes * 10
amountInPennies = amountInPennies - dimesValue


let nickels = Math.floor(amountInPennies / 5)
let nickelsValue = nickels * 5
amountInPennies = amountInPennies - nickelsValue

let pennies = Math.floor(amountInPennies / 1)
console.log(pennies)
let penniesValue = pennies * 1
amountInPennies = amountInPennies - penniesValue

finalOutput = document.querySelector("#output")
finalOutput.innerHTML = (`${quaters} Quaters, ${dimes} Dimes, ${nickels} Nickels, ${pennies} Pennies`)

})
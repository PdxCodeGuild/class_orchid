let button = document.getElementById("run_bt")
let output_div = document.getElementById("output_div")
let output = []


let myCoins = {
    "quarter": 25,
    "dime": 10,
    "nickel": 5,
    "penny": 1,
}

button.addEventListener('click', function() {
    let total = document.getElementById('text_input').value
    dollarValueInPennies = total * 100
    output = []
    for (coin in myCoins) {
        count = Math.floor(dollarValueInPennies / myCoins[coin])
        dollarValueInPennies -= (myCoins[coin] * count)
        if (count > 0) {
            output.push(`${count} ${coin}(s)`)
        }
    }
    output_div.innerHTML = `$${total} is ${output} in coins`
    
})

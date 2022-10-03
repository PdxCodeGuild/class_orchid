let myCoins = {
    "quarter": 25,
    "dime": 10,
    "nickel": 5,
    "penny": 1,
}

total = Number(prompt('Enter a dollar amount: '))

dollarValueInPennies = total * 100

output = []

for (coin in myCoins) {
    count = Math.floor(dollarValueInPennies / myCoins[coin])
    dollarValueInPennies -= (myCoins[coin] * count)
    if (count > 0) {
        output.push(`${count} ${coin}(s)`)
    }
}
alert(`$${total} is ${output} in coins`)
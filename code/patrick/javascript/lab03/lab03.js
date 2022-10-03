let totalAmount = prompt('enter a number')

let convertedTotalAmount = parseFloat(totalAmount * 100)
console.log(convertedTotalAmount)

alert(Math.round(convertedTotalAmount/25), 'quarters')
convertedTotalAmount = convertedTotalAmount%25
alert(Math.round(convertedTotalAmount/10), 'quarters')
convertedTotalAmount = convertedTotalAmount%10
alert(Math.round(convertedTotalAmount/5), 'quarters')
convertedTotalAmount = convertedTotalAmount%5
alert(Math.round(convertedTotalAmount/1), 'quarters')
convertedTotalAmount = convertedTotalAmount%1

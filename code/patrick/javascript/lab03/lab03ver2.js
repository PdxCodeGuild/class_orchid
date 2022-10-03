document.getElementById('tAmount').addEventListener('change', makeChamge)

function makeChamge() {


    let totalAmount = document.getElementById('tAmount')
    let nValue = totalAmount.value
    let convertedTotalAmount = parseFloat(nValue * 100)
    console.log(convertedTotalAmount)

    alert(Math.round(convertedTotalAmount / 25), 'quarters')
    convertedTotalAmount = convertedTotalAmount % 25
    alert(Math.round(convertedTotalAmount / 10), 'quarters')
    convertedTotalAmount = convertedTotalAmount % 10
    alert(Math.round(convertedTotalAmount / 5), 'quarters')
    convertedTotalAmount = convertedTotalAmount % 5
    alert(Math.round(convertedTotalAmount / 1), 'quarters')
    convertedTotalAmount = convertedTotalAmount % 1
}
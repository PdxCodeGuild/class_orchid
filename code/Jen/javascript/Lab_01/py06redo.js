
const winAmounts = {
    0: 0,
    1: 4.00,
    2: 7.00,
    3: 100.00,
    4: 50_000.00,
    5: 1_000_000.00,
    6: 25_000_000.00,
}

let myTicket = []

let counter = 0
while (counter < 6) {
    myTicket.push(Math.floor(Math.random() * 100))
    counter += 1
}
console.log(myTicket)
alert(`Your ticket numbers are ${myTicket}`)

function pick6() {

    let ticketDrawn = []
    let iterations = 5
    while (iterations >= 0) {
        ticketDrawn.push(Math.floor(Math.random() * 100))
        iterations -= 1
    }
    return ticketDrawn
}

function numMatches(ticketDrawn, myTicket) {
    let ticketWins = 0
    let iterations = 5
    while (iterations >= 0) {
        let winNum = ticketDrawn[iterations]
        let tickNum = myTicket[iterations]
        if (winNum == tickNum) {
            ticketWins += 1
        }
        return winAmounts[ticketWins]
    }
}

let runningTotal = 0
counter = 100000
expense = 0
while (counter > 0) {
    counter -= 1
    expense += 2
    runningTotal += numMatches(pick6(), myTicket)
}

let bank = runningTotal - expense
let ROI = bank / expense

if (bank > 0) {
    alert(`You have played these numbers 100,000 times. Your bank balance is now ${bank}. Your ROIS is ${ROI} Congratulations!`)
}
else {
    alert(`You have played these numbers 100,000 times. Your bank balance is now $${bank}. Your ROI is ${ROI} Please try again.`)
}


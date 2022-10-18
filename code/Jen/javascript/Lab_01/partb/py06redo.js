

button.addEventListener('click', get_tickets)

function get_tickets() {
    let iterations1 = 0
    let myTicket = []
    while (iterations1 < 6) {
        myTicket.push(Math.floor(Math.random() * 99) + 1)
        iterations1 += 1
    }
    console.log(myTicket)
    alert(`Your ticket numbers are ${myTicket}`)
    runit(myTicket)

    function runningTotal(myTicket) {
        let counter = 100000
        let running_total = 0
        expense = 0
        while (counter > 0) {
            counter -= 1
            expense += 2
            running_total += numMatches(pick6(), myTicket)
        }

        return running_total
    }

    function pick6() {
        let ticketDrawn = []
        let iterations2 = 5
        while (iterations2 >= 0) {
            ticketDrawn.push(Math.floor(Math.random() * 99) + 1)
            iterations2 -= 1
        }

        return ticketDrawn
    }

    function numMatches(ticketDrawn, myTicket) {
        const winAmounts = {
            0: 0,
            1: 4.00,
            2: 7.00,
            3: 100.00,
            4: 50_000.00,
            5: 1_000_000.00,
            6: 25_000_000.00,
        }

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

    function runit(myTicket) {
        let bank = (runningTotal(myTicket) - expense)
        let ROI = bank / expense
        console.log(ROI, bank)
        myTicket = []

        if (bank > 0) {
            alert(`You have played these numbers 100,000 times. Your bank balance is now ${bank}. Your ROIS is ${ROI} Congratulations!`)
        }
        else {
            alert(`You have played these numbers 100,000 times. Your bank balance is now $${bank}. Your ROI is ${ROI} Please try again.`)
        }
    }

}


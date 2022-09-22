
const cards = {
    'K': 10,
    'Q': 10,
    'J': 10,
    '10': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'A': 1,
}

let runningCards = []
console.log(cards)

function recs(runningTotal) {
    while (runningTotal >= 0 && runningTotal < 17) {
        alert(`Your total equals ${runningTotal}. You are advised to Hit.`)
        break
    }

    while (runningTotal >= 17 && runningTotal < 21) {
        alert(`Your total equals ${runningTotal}. You are advised to Stay.`)
        exit

    }

    while (runningTotal == 21) {
        alert(`BLACKJACK!`)
        exit
    }

    while (runningTotal > 21) {
        alert(`BUSTED`)
        exit
    }
}

const firstCard = prompt("What is your first card?")
runningCards.push(cards[firstCard])
let firstInput = cards[firstCard]
runningTotal = firstInput
recs(runningTotal)

const secondCard = prompt("What is your second card?")
runningCards.push(cards[secondCard])
let secondInput = cards[secondCard]
runningTotal += secondInput
recs(runningTotal)

const thirdCard = prompt("What is your third card?")
runningCards.push(cards[thirdCard])
let thirdInput = cards[thirdCard]
runningTotal += thirdInput
recs(runningTotal)
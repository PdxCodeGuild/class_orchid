const cardDeck = {A: 1, K: 10, Q: 10, J: 10, 10: 10, 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2, 1: 1
};

let firstCard = prompt("What is your first card?");
let secondCard = prompt("What is your second card");
let thirdCard = prompt("What is oyur second card");

let firstChoice = cardDeck[firstCard]
let seconChoice = cardDeck[secondCard]
let thridChoice = cardDeck[thirdCard]


const hand = firstChoice + seconChoice + thridChoice;

if (hand < 17) {
    alert(`${hand} HIT!`)
} else if(hand > 17 && hand < 21) {
    alert(`${hand} STAY!`)
} else if (hand == 21) {
    alert(`${hand} BLACKJACK!`)
} else {
    alert(`${hand} BUSTED!`)
}





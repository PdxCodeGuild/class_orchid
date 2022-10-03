let firstCard = prompt('Please enter your first card selection: ')

let secondCard = prompt('Please enter your second card selection: ')

let thirdCard = prompt('Please enter your third card selection: ')

const cardValue = {
    'a': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'j': 10,
    'q': 10,
    'k': 10,
};

let selection = cardValue[firstCard] + cardValue[secondCard] + cardValue[thirdCard]

if (selection < 17) {
    alert('Hit!');
} else if (selection >= 17 && selection < 21  ) {
    alert('Stay');
} else if (selection == 21) {
    alert('Blackjack!');
} else if (selection > 21) {
    alert('Already Busted.');
}


let addCard = document.getElementById('addCard')
let done = document.getElementById('done')
let user =  document.getElementById('user')
let results =  document.getElementById('results')

let cards = []

addCard.addEventListener('click', function() {
    cards.push(parseInt(user.value))
});

done.addEventListener('click', function() {
    let firstCard = cards[0]
    
    let secondCard = cards[1]
    
    let thirdCard = cards[2]
    
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
    console.log(selection)
    if (selection < 17) {
        results.innerHTML = 'Hit!';
    } else if (selection >= 17 && selection < 21  ) {
        results.innerHTML = 'Stay';
    } else if (selection == 21) {
        results.innerHTML ='Blackjack!';
    } else if (selection > 21) {
        results.innerHTML ='Already Busted.';
    }
});



let submit = document.querySelector("#submit")



submit.addEventListener('click', function(){
    
    let firstChoice = document.querySelector("#firstcard").value;
    
    let secondChoice = document.querySelector("#secondcard").value;
    
    let thirdChoice = document.querySelector("#thirdcard").value;
    
    const cardDeck = {A: 1, K: 10, Q: 10, J: 10, 10: 10, 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2, 1: 1}
    

    let firstCard = cardDeck[firstChoice]
    let secondCard = cardDeck[secondChoice]
    let thirdCard = cardDeck[thirdChoice]

    const hand = firstCard + secondCard + thirdCard

    if (hand < 17) {
        let finalOutcome = hand
        finalOutput = document.querySelector("#output")
        finalOutput.innerHTML = (`${finalOutcome} HIT!`)
    } else if(hand > 17 && hand < 21) {
        let finalOutcome = hand
        finalOutput = document.querySelector("#output")
        finalOutput.innerHTML = (`${finalOutcome} STAY!`)
    } else if (hand == 21) {
        let finalOutcome = hand
        finalOutput = document.querySelector("#output")
        finalOutput.innerHTML = (`${finalOutcome} BLACKJACK!`)
    } else {
        let finalOutcome = hand
        finalOutput = document.querySelector("#output")
        finalOutput.innerHTML = (`${finalOutcome} BUSTED!`)
    }

    




})
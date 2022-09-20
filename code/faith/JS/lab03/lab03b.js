let enter = document.getElementById('enter')


enter.addEventListener('click', function(){
    let firstcard = document.getElementById('fc').value
    let secondcard = document.getElementById('sc').value
    let thirdcard = document.getElementById('tc').value

    cards = {
        A:1,
        J:10,
        K:10,
        Q:10,
        2:2,
        3:3,
        4:4,
        5:5,
        6:6,
        7:7,
        8:8,
        9:9,
        10:10
        }
    
    
    let fc = cards[firstcard]
    let sc = cards[secondcard]
    let tc = cards[thirdcard]
    
    let hand = fc+sc+tc
    
    if (hand == 21) {
        alert('Blackjack')
    }
    else if (hand >= 21) {
        alert('Already busted')
    }
    else if (hand <17) {
        alert('Hit')
    }
    else if (hand >= 17 && hand < 21) {
        alert('Stay')
    }
    
})


let button = document.getElementById("button")
button.addEventListener('click', runit)

function runit() {


    let runningTotal = 0
    let runningCards = []
    card1()

    function recs(runningTotal) {

        while (runningTotal >= 0 && runningTotal < 17) {
            alert(`Your total equals ${runningTotal}. You are advised to Hit.`)
            break
        }

        while (runningTotal >= 17 && runningTotal < 21) {
            alert(`Your total equals ${runningTotal}. You are advised to Stay.`)
            button.removeEventListener("click", card2)
            exit

        }

        while (runningTotal == 21) {
            alert(`BLACKJACK!`)
            button.removeEventListener("click", card3)
            exit
        }

        while (runningTotal > 21) {
            alert(`BUSTED`)
            button.removeEventListener("click", card3)
            exit
        }
    }

    function card1() {
        const select = document.getElementById('ddl');
        const firstCard = parseInt(select.options[select.selectedIndex].value);
        runningTotal += (firstCard)
        runningCards.push(firstCard)
        console.log(runningTotal)
        console.log(runningCards)
        recs(runningTotal)
        document.getElementById("card_request").innerHTML = "What is your second card?"
        console.log("I'm waiting for the button")
        let button = document.getElementById("button")
        button.removeEventListener("click", runit)
        button.addEventListener('click', card2)

    }

    function card2(s) {
        const select2 = document.getElementById('ddl');
        const secondCard = parseInt(select2.options[select2.selectedIndex].value);
        runningCards.push(secondCard)
        runningTotal += secondCard;
        console.log("what is happening here")
        console.log(runningCards)
        console.log(runningTotal)
        recs(runningTotal)
        document.getElementById("card_request").innerHTML = "What is your third card?"
        console.log("Im waiting for the next button")
        let button = document.getElementById("button")
        button.removeEventListener("click", card2)
        button.addEventListener('click', card3)

    }

    function card3() {
        console.log("I made it here")
        console.log(runningTotal)
        console.log(runningCards)
        const select3 = document.getElementById('ddl');
        const thirdCard = parseInt(select3.options[select3.selectedIndex].value);
        runningCards.push(thirdCard)
        runningTotal += thirdCard;
        recs(runningTotal)
        alert(`Your total equals ${runningTotal} but you are out of cards.`)
        button.removeEventListener("click", card3)
    }
}
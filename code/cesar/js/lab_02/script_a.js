//  Lab 2 Javascript - Python Lab 05 - Black Jack

const deck = { "0": 0, "A": 11, "10": 10, "J": 10, "Q": 10, "K": 10, }

let card1 = prompt('What is your first card? ').toUpperCase()
let card2 = prompt('What is your second card? ').toUpperCase()
let card3 = prompt('What is your third card? ').toUpperCase()

console.log(card1, card2, card3)

const total = card1 + card2 + card3

console.log(total)




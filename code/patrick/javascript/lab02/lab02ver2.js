const paidOut = {
    0:0,
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000,
}

function pick6(){
    let numbers = []
    while (numbers.length < 6){
        let randomNum = Math.floor(Math.random() *99 )
        numbers.push(randomNum)
    }
    return numbers
}


function numMatches(winningNumbers, userNumber){
    let matches = 0
    if (winningNumbers[0] == userNumber[0]){
        matches += 1
    }
    if (winningNumbers[1] == userNumber[1]){
        matches += 1
    }
    if (winningNumbers[2] == userNumber[2]){
        matches += 1
    }
    if (winningNumbers[3] == userNumber[3]){
        matches += 1
    }
    if (winningNumbers[4] == userNumber[4]){
        matches += 1
    }
    if (winningNumbers[5] == userNumber[5]){
        matches += 1
    } 
    return matches
}

function gamlbeGame(){
    
}        
let games = 0
let earnings = 0
let expenses = 0


let winningNumbers = pick6()
let nog = document.getElementById('nog')
console.log(nog)
let numberOfGames = nog.value
parseInt(numberOfGames)
console.log(numberOfGames)


while (games < numberOfGames){
    let userNumber = pick6()
     
    games += 1
    

    let gameMatches = numMatches(winningNumbers, userNumber)
    expenses += 2
    

    
    earnings += paidOut[gameMatches]



}



let balance = earnings - expenses

let roi = balance / expenses
alert(`balance: ${balance} \n expenses: ${expenses} \n earnings: ${earnings} \n roi: ${roi}`)

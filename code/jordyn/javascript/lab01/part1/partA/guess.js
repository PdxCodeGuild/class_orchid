//This is based on a Python program I made in my first time in this class. Thought it would be more fun.

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
var correct_number = -1
let attempts = 0
let last_guess = 0
let historic_guess = [0]
let guess = 0
let absolute_difference = 0

while (true){
    correct_number = prompt('Please give a number from 1-10 for the computer to guess.')
    correct_number = parseInt(correct_number)
    if (!(numbers.includes(correct_number))){
        alert('Your number was not within the range of 1-10, the computer will only guess within this range')
    } else {
        break
    }
}

while (true){
    console.log(attempts)
    while (0 in historic_guess){
        guess = Math.floor(Math.random() * 10 + 1)
        if (!(historic_guess.includes(guess))){
            historic_guess.push(guess)
            break
        } else if (historic_guess.includes(guess)){
            continue
        }
    }
    let message1 = `Please guess a number between 1 and 10. > ${guess}`
    console.log(message1)
    absolute_difference = Math.abs(correct_number - guess)
    if (guess === correct_number){
        attempts += 1
        let message2 = `The Computer Got It! ${guess} was the correct number!\nIt guessed ${attempts} times.`
        alert(message2)
        break
    } else if (!(guess === correct_number)) {
        if (last_guess === 0){
            attempts += 1
            last_guess = absolute_difference
        } else if (absolute_difference === last_guess){
            attempts += 1
            last_guess = absolute_difference
        } else if (absolute_difference < last_guess){
            attempts += 1
            last_guess = absolute_difference
        } else if (absolute_difference > last_guess){
            attempts += 1
            last_guess = absolute_difference
        }
    }
}
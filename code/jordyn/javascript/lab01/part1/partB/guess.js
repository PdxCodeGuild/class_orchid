let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
var correct_number = -1
let attempts = 0
let last_guess = 0
let historic_guess = [0]
let guess = 0
let absolute_difference = 0

function game(){
    correct_number = document.getElementById('user-input').value
    correct_number = parseInt(correct_number)
    console.log(correct_number)
    if (!(numbers.includes(correct_number))){
        alert('Your number was not within the range of 1-10, the computer will only guess within this range')
        //I have no idea why the warning is given twice before changing the textfield to empty
        document.getElementById("user-input").value = "";
    } else {
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
    }
    setTimeout(function(){console.log('This is a delay')}, 1000)
    let message1 = `Please guess a number between 1 and 10. > ${guess}`
    console.log(message1)
    absolute_difference = Math.abs(correct_number - guess)
    // setTimeout(function(){return 0}, 1000)
    if (guess === correct_number){
        attempts += 1
        let message2 = `The Computer Got It! ${guess} was the correct number!\nIt guessed ${attempts} times.`
        alert(message2)
        correct_number = -1
        attempts = 0
        last_guess = 0
        historic_guess = [0]
        guess = 0
        absolute_difference = 0
    } else if (!(guess === correct_number)) {
        if (last_guess === 0){
            attempts += 1
            last_guess = absolute_difference
            game()
        } else if (absolute_difference === last_guess){
            attempts += 1
            last_guess = absolute_difference
            game()
        } else if (absolute_difference < last_guess){
            attempts += 1
            last_guess = absolute_difference
            game()
        } else if (absolute_difference > last_guess){
            attempts += 1
            last_guess = absolute_difference
            game()
        }
    }
}
// Lab01.a Average number

function sum(listOfNumbers) {
    let total = 0
    for (let num of listOfNumbers) {
        total = num + total
        console.log(total)
    }
    return total
}

function average(listOfNumbers) {
    let average = sum(listOfNumbers) / listOfNumbers.length
    return average
}

let nums = []

while (true) {
    let answer = prompt('Enter your number here or done if finished:')
    if (answer === 'done') {
        alert(`you entered ${nums} the sum is ${sum(nums)} the length is ${nums.length} and the average is ${average(nums)}`)
        break
    }
    answer = parseInt(answer)
    nums.push(answer)
}
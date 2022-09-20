
let nums = []

while (true) {
    let choice = prompt('Please enter a number or enter done to get results')
    if (choice == 'done'){
        break
    }else if (choice != 'done'){
        nums.push(parseInt(choice))
    }
}
let length = nums.length ;
let sum = nums.reduce((x, y)=> x + y)
let average = sum / length;
alert(`Your number average is: ${average}`)
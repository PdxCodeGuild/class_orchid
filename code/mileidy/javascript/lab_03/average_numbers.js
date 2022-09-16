
let nums = []

while (true) {
    let choice = prompt('Please enter a number or enter done to get results')
    if (choice == 'done'){
        let length = nums.length 
        let average = d3.sum(nums) / length
        alert(`Your number average is: ${average}`)
    nums.push(choice)
        break
    }
}
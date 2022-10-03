
let add_bt = document.getElementById('add')
let done = document.getElementById('done')
let user =  document.getElementById('user')
let results =  document.getElementById('results')

let nums = []
add_bt.addEventListener('click', function() {
    nums.push(parseInt(user.value))
});




done.addEventListener('click', function() {
let length = nums.length ;
let sum = nums.reduce((x, y)=> x + y)
let average = sum / length;
results.innerHTML = average
});
// adding event listeners -stopping point


// while (true) {
//     let choice = prompt('Please enter a number or enter done to get results')
//     if (choice == 'done'){
//         break
//     }else if (choice != 'done'){
//     }
// }
// let length = nums.length ;
// let sum = nums.reduce((x, y)=> x + y)
// let average = sum / length;
// alert(`Your number average is: ${average}`)
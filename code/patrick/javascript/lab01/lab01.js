let nums = []


while (true){
    userResponce = prompt('PLease enter a number or "done" to calculate')
    if (userResponce === 'done'){
        break
    } else if (userResponce != 'done'){
        nums.push(parseInt(userResponce))
    }
    
    

}
console.log(nums)
let lengthOfList = nums.length
const secondTotal = nums.reduce((x,y) => x+y)
console.log(secondTotal)
let finalTotal = (secondTotal / lengthOfList)

alert(finalTotal)
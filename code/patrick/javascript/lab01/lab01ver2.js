
document.getElementById('number').addEventListener('change', numsList )


let nums = []
function numsList(){

    
    let initialResponce = document.getElementById('number')
    let userResponce = initialResponce.value
    nums.push(parseInt(userResponce))
    console.log(nums)
    return nums
    
}
document.getElementById('calculate').addEventListener('click' , calculate )
function calculate(){
    
    let lengthOfList = nums.length
    const secondTotal = nums.reduce((x,y) => x+y)
    console.log(secondTotal)
    let finalTotal = (secondTotal / lengthOfList)
    console.log
    
    alert(finalTotal)

    
}
        
        
    
    
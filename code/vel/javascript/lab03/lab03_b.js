// lab01.b
// input and button
let button = document.getElementById("run_bt")
let done_Button = document.getElementById("done")
let nums = []
let output_div = document.getElementById('output_div')

button.addEventListener('click', function() {
    let user_Input = document.getElementById("text_input").value
    answer = parseInt(user_Input)
    nums.push(answer)
    }
) 

done_Button.addEventListener('click', function(){
    function sum(nums){
        let total = 0
        for (let num of nums) {
            total = num + total
            console.log(total)
        }
        return total
    }
    let average = sum(nums) / nums.length
    output_div.innerHTML = `you entered ${nums} the sum is ${sum(nums)} the length is ${nums.length} and the average is ${average}`
    // you entered ${nums} the sum is ${sum(nums)} the length is ${nums.length} and the average is ${average(nums)

})



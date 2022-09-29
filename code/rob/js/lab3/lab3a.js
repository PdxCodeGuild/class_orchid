console.log('lab 3 part a')

function quicksort(Arr){
    let A = Arr.slice()
    quicksort_recursive(A, 0, A.length - 1)
    return A
}

function quicksort_recursive(A, low, high){
    console.log(A)
    if(low < high){
        p = partition(A, low, high)
        quicksort_recursive(A, low, p)
        quicksort_recursive(A, p + 1, high)
    }
}

function partition(A, low, high){
    let pivot = A[low]
    let i = low - 1
    let j = high + 1
    while(true){
        do{
            i = i + 1
        }while(A[i] < pivot)
        do{
            j = j - 1
        }while(A[j] > pivot)
        if(i >= j){
            return j
        }else{
            let temp = A[i]
            A[i] = A[j]
            A[j] = temp
        }
    }
}
let Arr = []
function getNumbersFromUser(){
    while(true){
        num = prompt("Enter a number and press enter or 'exit' to exit:")
        if(num == 'exit'){
            break
        }
        
        Arr.push(parseInt(num))
    }
}

getNumbersFromUser()
sorted = quicksort(Arr)
console.log("A",Arr)
console.log('sorted', sorted)


alert(`Your unsorted list is: ${Arr}\nYour sorted list is: ${sorted}`)
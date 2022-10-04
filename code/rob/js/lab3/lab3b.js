console.log('lab 3 part b')

const numbers = document.querySelector('#numbers')
const buttonSort = document.querySelector('#buttonSort')
const unsortedPTag = document.querySelector('#unsorted')
const sortedPTag = document.querySelector('#sorted')
const sortingList = document.querySelector('#sortingList')

buttonSort.addEventListener('click', sortArr)

function unsortedToArray(){
    const unsorted = numbers.value
    const unsortedArray = []
    for (let index = 0; index < unsorted.length; index++) {
        const element = unsorted[index];
        let test = parseInt(element)
        if(Number.isInteger(test)){
            unsortedArray.push(test)
        }
    }
    return unsortedArray
}

function quicksort(Arr){
    console.log(Arr)
    let A = Arr.slice()
    quicksort_recursive(A, 0, A.length - 1)
    return A
}

function quicksort_recursive(A, low, high){
    if(low < high){
        p = partition(A, low, high)
        quicksort_recursive(A, low, p)
        quicksort_recursive(A, p + 1, high)
    }
}

function partition(A, low, high){
    const iter = document.createElement('p')
    iter.innerHTML = A
    sortingList.appendChild(iter)
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

function sortArr(){
    unsorted = unsortedToArray()
    unsortedPTag.innerHTML = 'unsorted: ' + unsorted
    sorted = quicksort(unsorted)
    sortedPTag.innerHTML = 'sorted: ' + sorted
}

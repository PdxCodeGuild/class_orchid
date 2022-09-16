// gonna a prompt for user input (text input field)
// array to store users input (push to list)
// display the array on the page (completed and add)
// adding a remove button (event listener with a click)
// add a complete button (event listener with a click)
// add items to ul



let addedItem = document.getElementById("added")
const itemList = document.getElementById('addedList')
const completedList = document.getElementById('completedList')


let addButton = document.getElementById("add-button")
addButton.addEventListener("click", add)


function add() {
    const list_item = document.createElement('li')
    itemList.append(list_item)
    const completeButton = document.createElement('button')
    completeButton.innerText='Complete'
    list_item.append(addedItem.value, completeButton)
    completeButton.addEventListener('click', complete)
    // for (const item of added) {
    //     console.log(item);
    // }
}
function complete(e) {
    completedList.append(e.target.parentNode)
    console.log(e.target.parentNode)
}
// gonna a prompt for user input (text input field)
// array to store users input (push to list)
// display the array on the page (completed and add)
// adding a remove button (event listener with a click)
// add a complete button (event listener with a click)

let completed = []

let added = []

let addedItem = document.getElementById("added")


let addButton = document.getElementById("add-button")
addButton.addEventlistener("click")


function add() {
    added.push(addedItem.value)
}



let todo = []

let addBtn = document.getElementById('addbutton')

let addItemText = document.getElementById('additem')


console.log(addBtn)
addBtn.addEventListener('click', e => {
    let item = { value: addItemText.value(), isComplete: false }
    todo.push(item)

})
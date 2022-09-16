let todo = []

let addBtn = document.getElementById('addbutton')

let addItemText = document.getElementById('additem')

let todoList = document.getElementById('todolist')

console.log(addBtn)
addBtn.addEventListener('click', e => {
    let item = { value: addItemText.value, isComplete: false }
    todo.push(item)

    var li = document.createElement("li")
    li.innerText = item.value
    todoList.appendChild(li)

    console.log(todo)
})
let todo = []

let addBtn = document.getElementById('addbutton')

let addItemText = document.getElementById('additem')

let todoList = document.getElementById('todolist')

console.log(addBtn)
addBtn.addEventListener('click', e => {
    let item = { value: addItemText.value, isComplete: false }
    todo.push(item)

    var li = document.createElement("li")
    var spanText = document.createElement('span')
    li.appendChild(spanText)
    todoList.appendChild(li)
    var spanComplete = document.createElement('span')
    li.setAttribute('style', 'list-style-type:none;')
    spanComplete.innerText = '😵☑️✅'
    // ❎❌😵☠️💀☠
    spanText.innerText = item.value
    // spanText.insertBefore(spanComplete)
    // li.insertBefore(spanComplete)
    li.appendChild(spanComplete)
    li.appendChild(spanText)

    console.log(todo)
})
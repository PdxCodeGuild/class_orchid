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
    var spanDelete = document.createElement('span')
    spanDelete.innerText = '😵'
    spanComplete.innerText = '☑️✅'
    spanText.innerText = item.value
    li.appendChild(spanDelete)

    li.appendChild(spanComplete)
    li.appendChild(spanText)

    spanDelete.onclick = function () {
        this.parentElement.remove()
        console.log(this)
    }








    // console.log(todo)
})


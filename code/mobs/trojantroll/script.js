let todo = []
// let todo = JSON.parse(localStorage.getItem('todo')) || []
let addBtn = document.getElementById('addbutton')
let addItemText = document.getElementById('additem')
let todoList = document.getElementById('todolist')
let completeList = document.getElementById('completed')

console.log(addBtn)
addBtn.addEventListener('click', e => {
    let item = { value: addItemText.value, isComplete: false, isDeleted: false }
    todo.push(item)

    var li = document.createElement("li")
    var spanText = document.createElement('span')
    li.appendChild(spanText)
    todoList.appendChild(li)
    var spanComplete = document.createElement('span')
    li.setAttribute('style', 'list-style-type:none;')
    var spanDelete = document.createElement('span')
    spanDelete.innerText = '😵'
    spanComplete.innerText = '☑️'
    spanText.innerText = item.value
    
    li.appendChild(spanComplete)
    li.appendChild(spanText)
    li.appendChild(spanDelete)

    spanDelete.onclick = function () {
        this.parentElement.remove()
        // Array(todo).filter(e=>e.isComplete)
    }

    spanComplete.onclick = function() {
        if (! item.isComplete) {
            spanComplete.innerText = '✅'
            item.isComplete = true
            completeList.appendChild(this.parentElement)
            spanText.setAttribute('style', 'text-decoration: line-through')
        }
        else {
            spanComplete.innerText = '☑️'
            item.isComplete = false
            todoList.appendChild(this.parentElement)
            spanText.setAttribute('style', 'text-decoration: normal')
        }
    }

    // localStorage.setItem('todo', JSON.stringify(todo))

})

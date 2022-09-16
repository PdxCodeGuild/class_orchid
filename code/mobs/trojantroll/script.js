let todo = JSON.parse(localStorage.getItem('todo')) || []
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
    spanComplete.innerText = '☑️'
    spanText.innerText = item.value
    
    li.appendChild(spanComplete)
    li.appendChild(spanText)
    li.appendChild(spanDelete)

    spanDelete.onclick = function () {
        this.parentElement.remove()
        console.log(this)
    }

    spanComplete.onclick = function() {
        if (! item.isComplete) {
            spanComplete.innerText = '✅'
            item.isComplete = true
            spanText.setAttribute('style', 'text-decoration: line-through')
            todo_sort()
        }
        else {
            spanComplete.innerText = '☑️'
            item.isComplete = false
            spanText.setAttribute('style', 'text-decoration: normal')
            todo_sort()
        }
    }

    localStorage.setItem('todo', JSON.stringify(todo))

    todo_sort = function() {
            todo.sort(function(x,y) {
            console.log('run')
            x = x.isComplete
            y = y.isComplete
            return (x === y)? 0 : x? 1 : -1
        })
        todoList.childNodes.forEach(e => {
            e.remove()
        })
        // rebuild
        todo.forEach(e => {
            e.appendChild(spanComplete)
            e.appendChild(spanText)
            e.appendChild(spanDelete)
        })
    }


})


const todobutton = document.querySelector(".todo-button")
const todoinput = document.querySelector(".todo-input")
const todolist = document.querySelector(".todo-list")
const completedList = document.querySelector('.completed-list')


todobutton.addEventListener("click", newItem)

const uncompleted = []
const _completed = []

function newItem(event) {
    event.preventDefault()
    var li = document.createElement('li');
    var inputData = todoinput.value;
    const deleteButton = document.createElement('button')
    deleteButton.classList.add('delete')
    deleteButton.innerText = 'delete'
    const completeButton = document.createElement('button')
    completeButton.classList.add('complete')
    completeButton.innerText = 'complete'
    li.innerText = inputData
    li.appendChild(deleteButton)
    li.appendChild(completeButton)
    
    uncompleted.push(li)

    deleteButton.addEventListener('click', removeItem)
    completeButton.addEventListener('click', completed)

    function removeItem(e){
        const liRemove = e.target.parentElement
        uncompleted.forEach(e => {
            if(e == liRemove){
                uncompleted.pop(liRemove)
            }
        })
        liRemove.remove()
    }

    function completed(e){
        const liRemove = e.target.parentElement
        uncompleted.forEach(e => {
            if(e == liRemove){
                uncompleted.pop(liRemove)
            }
        })
        _completed.push(liRemove)
        liRemove.remove()
        completedList.appendChild(liRemove)
        liRemove.children[1].innerText = 'undo'
        liRemove.style.textDecoration = 'line-through';
        completeButton.removeEventListener('click', completed)
        completeButton.addEventListener('click', undo)
    }

    function undo(event){
        const undoItem = event.target.parentElement
        undoItem.style.textDecoration = 'none';
        undoItem.children[1].innerText = 'complete'
        console.log(undoItem)
        
        temp = _completed.indexOf()
        _completed.splice(temp, 1)
        
        _completed.pop(undoItem)
        uncompleted.push(undoItem)
        console.log(_completed)
        console.log(uncompleted)
        completeButton.removeEventListener('click', undo)
        completeButton.addEventListener('click', completed)
        showAll()
    }

    function showAll(){
        uncompleted.forEach(e => {
            todolist.appendChild(e)
        })
        _completed.forEach(e => {
            completedList.appendChild(e)
        })
    }
    showAll()

    todoinput.value = ''
}

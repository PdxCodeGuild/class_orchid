const todobutton = document.querySelector(".todo-button")
const todoinput = document.querySelector(".todo-input")
const todolist = document.querySelector(".todo-list")


todobutton.addEventListener("click", newItem)

function newItem(event) {
    event.preventDefault()
    var li = document.createElement('li');
    var inputData = todoinput.value;

    li.innerText = inputData
    todolist.appendChild(li)
    console.log(li)
}

//  gather elements and assign them to variables
let userName = document.getElementById('name')
let nameInput = document.getElementById('name-input')
let nameButton = document.getElementById('name-button')
let resetButton = document.getElementById('reset-button')

// add a click event to nameButton
nameButton.addEventListener('click', e => {
    // prevent the default callback of this element's click event
    // on a submit button, this would be submitting the form as a POST request
    e.preventDefault()
    // set a key in localStorage named 'userNameString' with the value of 
    // nameInput's JSON stringified value
    localStorage.setItem('userNameString', JSON.stringify(nameInput.value))
    // change the innerText of the userName element
    userName.innerText = nameInput.value
})

// check if the localStorage key 'userNameString' has contents
if (localStorage.getItem('userNameString')) {
    // set the innerText of userName to the value of localStorage's 'userNameString' key
    userName.innerText = JSON.parse(localStorage.getItem('userNameString'))
}

// add a click event to resetButton
resetButton.addEventListener('click', _ => {
    // clear localStorage
    localStorage.clear()
    // set userName's innerText back to 'unknown'
    userName.innerText = 'unknown'
} )
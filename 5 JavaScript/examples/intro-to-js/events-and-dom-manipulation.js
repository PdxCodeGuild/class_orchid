const header = document.querySelector('h3')
// console.log(header); // notice that this changes when the element changes! 
header.innerText = 'whee!'
header.innerHTML = "<i>Class Orchid's</i> pizza"

const mushrooms = document.getElementById('mushrooms')
mushrooms.parentNode.classList.add('not-veg')

const notVeg = document.querySelectorAll('.not-veg') // returns a NodeList
console.log(notVeg.length); // NodeLists have a length attribute
// notVeg.style.fontSize = '0.7em' // can't do this, you need to either loop, or slice items out of the list
notVeg.forEach(e => e.style.fontSize = '0.7em');

const winner = document.querySelectorAll('.secret-winner')
winner[0].innerText = '29384'


const person = document.getElementById('person')
person.value = 'Danny' // you can set an intial value for inputs if you want

// event listeners
// the callback function is what happens on the specified event
person.addEventListener('mouseover', () => console.log('put your name here'))

/* Let's write our voting function! */

// these are all the elements we will need to reference
// they could get selected inside the callback, but since they are 'live' we can do it here
const checkboxes = document.querySelectorAll('input[type=checkbox]')
const warning = document.getElementById('warning')

let voters = []
const voter = () => {
    // stop people from voting twice
    if (voters.includes(person.value)) {
        warning.innerText = "You can't vote more than once"
        return
    }
    voters.push(person.value)

    // convert checkboxes to an array and then filter for checked ones
    const checked = Array.from(checkboxes).filter(e => e.checked)
    checked.forEach(e => {
        let vote = document.getElementById(e.value) // get vote field
        val = parseInt(vote.innerText) // convert contents to number
        val++ // increment it
        vote.innerText = val // reassign it back to the vote field
    })

    // clear out values after vote submission
    warning.innerText = ''
    person.value = ''
    checkboxes.forEach(e => e.checked = false)
}

// add the function as a callback on the event listener
const button = document.querySelector('input[type=button]')
button.addEventListener('click', voter)
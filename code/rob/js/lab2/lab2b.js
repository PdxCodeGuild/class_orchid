const contactList = document.querySelector('#contactList')
const blankField = document.querySelector('#blankField')
const newGame = document.querySelector('#newGame')
const newMode = document.querySelector('#newMode')
const newChamp = document.querySelector('#newChamp')
const newContactButton = document.querySelector('#newContactButton')
const keys = JSON.parse(localStorage.getItem('keys'))
let contacts = JSON.parse(localStorage.getItem('contacts'))

newContactButton.addEventListener('click', addContact)

function getContactsFromLocalStorage(){
    if(keys == null){
        const keys = ['game','mode','champ']
        localStorage.setItem('keys', JSON.stringify(keys))
    }
    
    if(contacts != null){
        contacts.forEach(e => {
            const contactDiv = document.createElement('div')
            contactDiv.classList.add('contact')
            const contactLi = document.createElement('li')
            contactLi.innerText = `game: ${e.game}, mode: ${e.mode}, champ: ${e.champ}`
            contactDiv.appendChild(contactLi)
            contactList.appendChild(contactDiv)
        })
    }else{
        contacts = []
        localStorage.setItem('contacts', JSON.stringify(contacts))
        const contactLi = document.createElement('li')
        contactLi.innerText = 'contacts is empty - refresh page'
        contactList.appendChild(contactLi)
    }
}

function addContact(){
    console.log(contacts)
    const game = newGame.value
    const mode = newMode.value
    const champ = newChamp.value
    const blankDiv = document.createElement('div')
    if(game == '' || mode == '' || champ == ''){
        blankDiv.innerText = 'Field can not be left blank'
        blankField.appendChild(blankDiv)
    }else{
        blankField.remove(blankDiv)
        let contact = {}
        contact[keys[0]] = game
        contact[keys[1]] = mode
        contact[keys[2]] = mode
        console.log(contact)
        contacts.push(contact)
        contact = {}
        localStorage.setItem('contacts', JSON.stringify(contacts))
    }
    newGame.value = ''
    newMode.value = ''
    newChamp.value = ''
    location.reload()
}

getContactsFromLocalStorage()

const setKeyNamesForContact = () => {
    alert('When prompted enter contact keys \ntype key names such as name, role, number, age ')
    
    let keys = []
    for(let i = 0; i < 3; i++){
        keyName = prompt(`Enter value for key ${i + 1}: `)
        keys.push(keyName)
    }
    
    contacts = []

    localStorage.setItem('keys', JSON.stringify(keys))
    localStorage.setItem('contacts', JSON.stringify(contacts))
}

const showKeysAndContacts = () => {
    let keys = JSON.parse(localStorage.getItem('keys'))
    let contacts = JSON.parse(localStorage.getItem('contacts'))
    if(contacts.length == 0){
        alert(`Your contact keys are ${keys[0]}, ${keys[1]}, ${keys[2]}. \nYour contacts is empty.`)
    }else{
        let contactString = ''
        for(let i = 0; i < contacts.length; i++){
            temp = ''
            for(key in contacts[i]){
                temp += `${key}: ${contacts[i][key]} `
            }
            contactString += temp + '\n'
        }
        alert(`Your contact keys are ${keys[0]}, ${keys[1]}, ${keys[2]}. \n\ncontacts:\n${contactString}`)
    }
}

const addContact = () => {
    let keys = JSON.parse(localStorage.getItem('keys'))
    let contacts = JSON.parse(localStorage.getItem('contacts'))
    let contact = {}
    for(let i = 0; i < keys.length; i++){
        value = prompt(`Add contact value for ${keys[i]}:`)
        contact[keys[i]] = value
    }
    contacts.push(contact)
    localStorage.setItem('contacts', JSON.stringify(contacts))
}

let keys = JSON.parse(localStorage.getItem('keys'))
let contacts = JSON.parse(localStorage.getItem('contacts'))
if(keys == null){
    setKeyNamesForContact()
}

while(true){
    let action = prompt("To show contacts type 'show'\nTo add a contact type 'add'\nTo exit type 'exit'")
    if(action == 'show'){
        showKeysAndContacts()
    }else if(action == 'add'){
        addContact()
    }else if(action == 'exit'){
        break
    }else{
        alert('not a valid action. try again.')
    }
}




let word = document.querySelectorAll('.f_word')
let definition = document.querySelectorAll('.f_definition')

for(let item = 0; item <word.length; item++){
    word[item].addEventListener('click', function(){
        if(definition[item].style.display == 'none'){
            definition[item].style.display = 'block'
            console.log('hello')
        }
        else{
            definition[item].style.display = 'none' 
            console.log('hello')
        }
    })
}


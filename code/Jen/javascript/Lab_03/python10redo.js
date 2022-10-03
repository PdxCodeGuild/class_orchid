


const plainMessage = prompt("Please enter the phrase you would like to encrypt. ")


let pnumbers = []
let plength = plainMessage.length;
while (plength--) {
    pnumbers.push(plainMessage.charCodeAt((plength)))
}
console.log(pnumbers)

let cypher = []

for (let i = 0; i < pnumbers.length; i++) {
    comparenum(pnumbers[i])
    cypher.push(newnum)

}

function comparenum(pnumber) {

    if (pnumber >= 65 && pnumber < 78 || pnumber >= 97 && pnumber < 110) {
        newnum = pnumber + 13
    }

    else if (pnumber == "32") {
        newnum = "32"
    }

    else if (pnumber == "44") {
        newnum = '.'
    }
    else {
        newnum = pnumber - 13
    }
    return newnum
        ;

}

const cypherMessage = cypher.map((letter) => String.fromCharCode(letter));
cypherMessage.reverse()
const cypherText = cypherMessage.join('')
console.log(cypherText)
alert(`Your encrypted text is ${cypherText}`)

/* remove the commas on the decrypt */

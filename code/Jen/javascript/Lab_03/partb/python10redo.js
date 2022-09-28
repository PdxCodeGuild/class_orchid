

let button = document.getElementById("button");
button.addEventListener('click', runit);

function runit() {
    let cypherText = convert()
    let encrypted = document.querySelector('h2');
    encrypted.innerHTML = (`Your encrypted text is: ${cypherText}`)
}

function convert() {

    const plainMessage = document.getElementById("textbox").value;
    console.log(plainMessage)
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
    console.log(cypher)
    const cypherMessage = cypher.map((letter) => String.fromCharCode(letter));
    console.log(cypherMessage)
    cypherMessage.reverse()
    const withoutComma = cypherMessage.join('')
    console.log(withoutComma)
    return withoutComma
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



/* remove the commas on the decrypt */

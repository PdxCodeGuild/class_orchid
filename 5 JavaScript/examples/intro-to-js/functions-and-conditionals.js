/* ============

Conditionals 

===============*/

const a = 0
const b = 1
const c = false
const isFalse = a == b

if (!isFalse) {
    console.log('execute this code');
} else if (a < b && true || a == b && c) {
    console.log('no, execute THIS code')
} else {
    console.log("this one won't happen");
}


// Ternary operator
// [condition] ? [output if true] : [output if false]
const output = a > b ? 'watermelon' : 'mango'
console.log(output);

//  you can replace ALL this code with a ternary
let valA
if (a > b) {
    valA = 'thing1'
} else {
    valA = 'thing2'
}

const condition = a > b && 1 > 0 || isFalse && 'whatever'

const myObj = {
    valA: condition ? 'thing3' : 'thing2'
}

console.log(myObj);


/* ============

Functions

There are a LOT of ways to write a JS function

===============*/


// standard declaration
function add(x, y) {
    return x + y
}

console.log(add(1, 3));


// assign to a variablev
const subtract = function (x, y) {
    return x - y
}

console.log(subtract(8, 5));


// ES6 arrow function, rocket function
const multiply = (x, y) => x * y

console.log(multiply(6, 4));

const divide = (x, y) => {
    console.log('this needs to be here for some reason');
    return x / y
}
console.log(divide(7, 2));


// Callback

let num_array = [1, 2, 3, 4, 5]

const filterHelper = function (x) {
    if (x > 2) {
        return x
    }
}
const filtered1 = num_array.filter(filterHelper)
console.log(filtered1);


const filtered2 = num_array.filter(x => {
    console.log('I have something important to say');
    return x > 2
})
console.log(filtered2);

const filtered3 = num_array.filter(x => x > 2)
console.log(filtered3);
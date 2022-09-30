/* ================

Declaring Variables

================ */

// snake_case
// camelCase
// PascalCase

var firstName = 'Danny'
let lastName = 'Burrow'
const className = 'Class Orchid'

firstName = 'Dan'
// className = 'something else' // Uncaught TypeError: Assignment to constant

let newVar
console.log(newVar);

if (newVar == undefined) {
    console.log('it is!');
}


/* ================

Types

================ */

// Primitive Types

let a = 'string' // string literal
let b = `template literals are like python's f${a}s`
console.log(b);
let c = 1 // number
let d = 1.5 // number 
let e = 2947223980349782340598239845789234985723459783254n // bigint
let f = true // boolean literal
let g = false
let h = null // used to clear a value
let i = undefined // when a value hasn't been assigned yet
let sym = Symbol('seed')
console.log(sym);

// Reference Types
let j = [1, 2, 'three', { key: 'four' }]
let k = { key: 'val', key2: [1, 2, 3] }
function myFunc(param1, param2) {
    return null
}

/* ================

Type Coercion

Dynamically typed: variables can change type (type is determined at runtime)
Weakly types: types can be coerced! JS will try to interpret any operation on any type

(python is dynamically and strongly typed)

================ */


let l = 8
let m = 'sense'

console.log(m + l); // sens8
console.log(m * l); // NaN (not a number)


let n = 1
let o = '1'


// use triple equals to DISALLOW type coercion in comparisons
// triple equals means same value AND same type
console.log(n == o); // true
console.log(n === o); // false

console.log(n != o); // false
console.log(n !== o); // true

// Type conversion
let p = parseInt('2')
let q = parseFloat('3.5')
let r = p.toString()

console.log(p * q); // 7
console.log(typeof r); // string
// the typeof keyword shows the type of the following symbol 

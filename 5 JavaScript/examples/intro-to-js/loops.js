/* ================

Loops

There are a LOT of ways to loop in JS

================ */

let i = 0
while (i < 5) {
    i++
    console.log(i);
}

// for(initialize; condition; increment)
for (let i = 1; i <= 5; i++) {
    console.log(i);
}

// ITERATING OVER AN ARRAY

const numArray = [1, 2, 3, 4, 5]

// 'standard'
for (i = 0; i < numArray.length; i++) {
    console.log(numArray[i])
}

// using a while loop
let x = 0
while (x < numArray.length) {
    console.log(numArray[x]);
    x++
}

// better way!
numArray.forEach(x => console.log(x))

// another better way
// for..of
for (const x of numArray) {
    console.log(x);
}

// map, filter, and reduce
// for when you want a new version of the array

const doubled = numArray.map(x => x * 2)
console.log(doubled);

const evens = numArray.filter((x) => x % 2 == 0)
console.log(evens);

const sum = numArray.reduce((x, y) => x + y)
console.log(sum);


// I don't know how to use sort for numbers!
// const sorted = numArray.sort((x, y) => x > y)
// console.log(sorted);


// ITERATING OVER OBJECTS

myObj = {
    1: 'one',
    2: 'two',
    3: 'three'
}

// for..in
// loop over the keys
for (thing in myObj) {
    console.log(myObj[thing]);
}

// loop over Object.entries
console.log(Object.entries(myObj));

Object.entries(myObj).forEach(x => console.log(x[0], x[1]))

// loop over Object.keys
console.log(Object.keys(myObj));

for (const key of Object.keys(myObj)) {
    console.log(myObj[key]);
}

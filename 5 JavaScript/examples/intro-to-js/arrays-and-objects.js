/* ================

Arrays

JS arrays are a lot like python lists!

================ */

colors = ['red', 'blue', 'yellow']
colors.push('orange', 'green', 'purple')
let popped = colors.pop()

console.log(popped);
console.log(colors[1]);
// console.log(color[1:3])
console.log(colors.slice(1));
console.log(colors.slice(1, 3));

colors[4] = 'chartreuse'
colors[5] = 'violet'
colors[7] = 'indigo'

console.log(colors);
console.log(colors[6]);
console.log(colors.length);


/* ================

Objects

A JS object is like a python dictionary AND a python object

================ */

const person = { firstName: 'Danny', lastName: 'Burrow' }
console.log(person['firstName']);
console.log(person.lastName);

person.title = 'instructor'
person['firstName'] = 'Dan'

console.log(person);

let pizza = {
    toppings: ['mushrooms', 'peppers'],
    restaurant: {
        name: 'EGPL',
        'phone number': 1234345809, // use a string key if your key is irregular or illegal
        staff: {
            owner: 'Mr. Bossman',
            chef: 'Remy',
            signWaver: 'Greg'
        }
    }
}

console.log(pizza.restaurant.staff.chef); // string dot notation to any level of nesting
console.log(pizza.restaurant['phone number']); // use bracket notation when key is a string
let res = 'restaurant'
// console.log(pizza.res.name); //TypeError: Cannot read properties of undefined
console.log(pizza[res].name); // use bracket notation when using a variable in the path

pizza.toppings.push('olives')
console.log(pizza);


// Accessing the keys of an object

const pizzaKeys = Object.keys(pizza)
console.log(pizzaKeys);

const restaurantKeys = Object.getOwnPropertyNames(pizza.restaurant)
console.log(restaurantKeys);

for (const prop in pizza) {
    console.log(`${prop}: ${pizza[prop]}`);
}


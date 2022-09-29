// Callbacks delay execution until the code is needed, or "called" for
const printStrings = () => {
    console.log('thing 1')
    setTimeout(() => console.log('thing2'), 1000)
    console.log('thing 3');
}
// printStrings()




// Promises resolve or reject once their execution is complete
const examplePromise = new Promise((resolve, reject) => {
    const condition = false
    if (condition) {
        setTimeout(() => {
            resolve('promise resolved')
        }, 1000)
    } else {
        reject('promise rejected')
    }
})

const secondPromise = () => {
    return new Promise((resolve, reject) => {
        resolve('this one always resolves')
    })
}

// console.log(examplePromise);

examplePromise
    .then(secondPromise)
    .then(msg => console.log(msg))
    .catch(msg => console.error(msg))




// Async / await are syntactic sugar for promises 

// the async keyword means this function will automatically return a Promise
async function exampleAsync() {
    return 1
}

console.log(exampleAsync()); // a Promise object
exampleAsync().then(res => console.log(res))


const exampleAwait = async () => {
    let result
    try {
        result = await examplePromise
        // await can only be used inside async functions
    } catch (err) {
        result = 'something went wrong'
    }
    return result
}

// console.log(exampleAwait());
exampleAwait().then(msg => console.log(msg))


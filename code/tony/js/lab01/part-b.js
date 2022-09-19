"use strict"

let ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',]
let teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',]
let tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety',]

let output = document.querySelector('#output')
let input = document.querySelector('#input')
let msg = 'Just start typing.<br>(Use 24-hour notation.)'
output.innerHTML = msg

function log(msg) {
    output.innerHTML += msg
}

function trans(num) {
    let quotient = Math.floor(num / 10)
    let remainder = num % 10

    // apply appropriate translations for respective ranges
    if (num < 10) {
        return `${ones[remainder]}`
    } else if (num < 20) {
        return `${teens[remainder]}`
    } else if (remainder == 0) {
        return `${tens[quotient]}`
    } else {
        return `${tens[quotient]}-${ones[remainder]}`
    }
}

function prep(s) {
    let parts = s.split(':')
    let str = ''
    let suf = ''
    let hour = Number(parts[0])
    let mins = Number(parts[1])

    let hourStr = hour > 12 ? hour % 12 : hour

    if (mins == 1) {
        str = `${trans(mins)} minute after ${trans(hourStr)}`
    } else if (mins > 0 && mins < 10) {
        str = `${trans(mins)} minutes after ${trans(hourStr)}`
    }

    if (hour == 0 && mins < 10) {
        str += 'midnight'
    } else if (hour == 0) {
        suf += 'minutes after midnight'
    }

    if (hour < 12 && hour > 0) {
        suf += 'in the morning'
    } else if (hour == 12 && mins == 0) {
        str += 'noon'
    } else if (hour < 16 && hour > 0) {
        suf += 'in the afternoon'
    } else if (hour > 0) {
        suf += 'in the evening'
    }

    if (!str) {
        str = trans(hourStr) + ((trans(hourStr) && trans(mins)) && ' ') + trans(mins)
    }
    suf = suf ? ` ${suf}` : ''
    return `It is ${str}${suf}.`
}

function inputListener(e) {
    e.preventDefault()
    let patterns = [
        '([0-1]?|2)',
        '([0-1]?[0-9]|2[0-3])',
        '([0-1]?[0-9]|2[0-3]):',
        '([0-1]?[0-9]|2[0-3]):[0-5]',
        '([0-1]?[0-9]|2[0-3]):[0-5][0-9]'
    ]
    if (RegExp(`^${patterns[patterns.length-1]}$`).exec(input.value)) {
        output.innerHTML == msg && (output.innerHTML = '')
        log(`${prep(input.value)}<br>`)
        input.value = ''
    }
    if (! RegExp(`^(${patterns.join('|')})$`).exec(input.value)) {
        let s = input.value.split('')
        s.pop()
        s = s.join('')
        input.value = s
    }
}

input.addEventListener('input', inputListener)
const output = document.querySelector('.result');
const btn = document.querySelector('.btn');

let firstNumber = prompt("Enter first number: ", 0);
const optr = prompt("Choose an operator from *, /, +, and -: ");
let secondNumber = prompt("Enter second number: ", 0);

function add (a, b) {
    return a + b;
}

function subtract (a, b) {
    return a - b;
}

function multiply (a, b) {
    return a * b;
}

function divide (a, b) {
    return a / b
}


function compute (optr, a, b) {
    // firstNumber = Number(a);
    // secondNumber = Number(b);

    if (optr === '/' && Number(b) === 0) {
        return `${Number(a)} ${optr} ${Number(b)} = Undefined`

    } else if (isNaN(a) || isNaN(b)) {
        return isNaN(a) ? `${a} is not a valid number` : `${b} is not a valid number`

    } else if (optr === '%' && Number(b) === 0) {
        return `${a} ${optr} ${b} = Undefined`

    } else if (!validOperators.includes(optr)) {
        return `${optr} is invalid operator`

    } else {
        const result = select[optr](Number(a), Number(b));
        return `${a} ${optr} ${b} = ${result}`
    }
}

const validOperators = ['*', '+', '/', '-'];

const select = {
    '*': multiply,
    '+': add,
    '/': divide,
    '-': subtract
}

output.textContent = compute(optr, firstNumber, secondNumber);

btn.addEventListener('click', () => {
    window.location.reload(true);
})
console.log(compute(optr, firstNumber, secondNumber))
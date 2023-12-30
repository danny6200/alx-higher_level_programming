#!/usr/bin/node
const { argv } = require('process');

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 1 || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const input = parseInt(argv[2]);
const result = factorial(input);

console.log(result);

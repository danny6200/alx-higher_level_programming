#!/usr/bin/node
const { argv } = require('process');

if (argv.length < 3) {
  console.log(0);
} else if (argv.length === 3) {
  console.log(0);
} else {
  let max = Number.NEGATIVE_INFINITY;
  let secondMax = Number.NEGATIVE_INFINITY;
  for (let i = 2; i < argv.length; i++) {
    if (parseInt(argv[i]) > max) {
      secondMax = max;
      max = argv[i];
    } else if (parseInt(argv[i]) > secondMax && parseInt(argv[i]) !== max) {
      secondMax = parseInt(argv[i]);
    }
  }
  console.log(secondMax);
}

#!/usr/bin/node
const { argv } = require('process');

if (argv[2] === undefined || isNaN(parseInt(argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  const num = parseInt(argv[2]);
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}

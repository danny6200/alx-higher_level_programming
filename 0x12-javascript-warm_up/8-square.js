#!/usr/bin/node
const { argv } = require('process');

if (argv[2] === undefined || isNaN(parseInt(argv[2]))) {
  console.log('Missing size');
} else {
  const num = parseInt(argv[2]);
  for (let i = 0; i < num; i++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row += 'X';
    }
    console.log(row);
  }
}

#!/usr/bin/node
const { argv } = require('process');

if (argv[2] === undefined || isNaN(parseInt(argv[2]))) {
  console.log('Not a number');
} else {
  console.log(parseInt(argv[2]));
}

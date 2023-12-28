#!/usr/bin/node
const { argv } = require('process');
let argc = 0;

for (arg of argv) {
	argc++;
}
argc -= 2;

if (argc === 0) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}

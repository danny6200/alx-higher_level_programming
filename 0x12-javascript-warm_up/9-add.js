#!/usr/bin/node
const { argv } = require('process');

function add(a, b) {
  console.log(parseInt(argv[2]) + parseInt(argv[3]));
}

add();

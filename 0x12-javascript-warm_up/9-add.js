#!/usr/bin/node
require('process');
const argv = process.argv;

const num1 = parseInt(argv[2]);
const num2 = parseInt(argv[3]);
console.log(num1 + num2);

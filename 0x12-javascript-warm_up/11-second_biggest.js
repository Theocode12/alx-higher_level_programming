#!/usr/bin/node

require('process');
const argv = process.argv;
let big = parseInt(argv[2]);
let secondBig = 0;
let counter = 2;

for (; counter <= argv.length - 1; counter++) {
  if (Math.round(parseInt(argv[counter])) > big) {
    secondBig = big;
    big = parseInt(argv[counter]);
  }
}
console.log(secondBig);

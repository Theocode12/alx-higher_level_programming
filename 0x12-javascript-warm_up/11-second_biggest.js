#!/usr/bin/node

require('process');
const argv = process.argv;
let big = argv[2];
let secondBig = 0;
let counter = 2;

for (; counter <= argv.length - 1; counter++) {
  if (argv[counter] > big) {
    secondBig = big;
    big = argv[counter];
  }
}
console.log(secondBig);

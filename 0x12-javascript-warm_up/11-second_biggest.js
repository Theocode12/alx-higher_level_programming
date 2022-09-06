#!/usr/bin/node

require('process');
const argv = process.argv;
let big = parseInt(argv[2]);
let secondBig = 0;
let counter = 2;

for (; counter <= argv.length - 1; counter++) {
  if (parseInt(argv[counter]) > big) {
    secondBig = big;
    big = parseInt(argv[counter]);
  }
  else if (parseInt(argv[counter]) > secondBig && argv.length > 3)
  {
    secondBig = parseInt(argv[counter])
  }
}
console.log(secondBig);

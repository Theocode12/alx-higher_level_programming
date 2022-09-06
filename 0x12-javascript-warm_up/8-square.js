#!/usr/bin/node

require('process');
const argv = process.argv;
let result = '';
let num; let i = 0; let j = 0;

if (argv.length === 2) {
  console.log('Missing size');
} else {
  num = parseInt(argv[2]);
  if (Number.isInteger(num)) {
    for (; i < num && num > 0; i++) {
      for (j = 0; j < num; j++) {
        result += 'X';
      }
      if (i < num - 1) { result += '\n'; }
    }
    if (result) { console.log(result); }
  } else { console.log('Missing size'); }
}

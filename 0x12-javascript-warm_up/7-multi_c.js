#!/usr/bin/node

require('process');
const argv = process.argv;
let num; let i = 0;
if (argv.length === 2) { console.log('Missing number of occurrences'); } else {
  num = parseInt(argv[2]);
  if (num > 0) {
    for (; i < num; i++) { console.log('C is fun'); }
  }
}

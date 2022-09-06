#!/usr/bin/node
require('process');
const argv = process.argv;
const num = parseInt(argv[2]);

function facto (num) {
  if (num <= 1 || Number.isNaN(num)) { return 1; }

  const result = facto(num - 1);
  return result * num;
}

console.log(facto(num));

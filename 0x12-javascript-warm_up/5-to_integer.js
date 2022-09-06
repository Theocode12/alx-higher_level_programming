#!/usr/bin/node

require('process');
const argv = process.argv;

const number = parseInt(argv[2]);
if (Number.isNaN(number)) { console.log('Not a number'); } else { console.log("My number:", number); }

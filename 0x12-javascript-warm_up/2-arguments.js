#!/usr/bin/node

require('process');

const argvLength = process.argv.length - 2;
if (argvLength > 1) { console.log('Arguments found'); } else if (argvLength === 1) { console.log('Argument found'); } else { console.log('No Argument'); }

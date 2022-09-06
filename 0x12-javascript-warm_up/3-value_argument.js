#!/usr/bin/node

require('process');

let index;
for (index = 0; process.argv[index]; index++);
if (index > 2) { console.log(process.argv[2]); } else { console.log('No argument'); }

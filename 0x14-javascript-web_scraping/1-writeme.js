#!/usr/bin/node

const process = require('process');
const fs = require('fs');

const argv = process.argv.slice(2);
fs.writeFile(argv[0], argv[1], 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});

#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);
const [fileA, fileB, fileC] = args;

fs.readFile(fileA, 'utf-8', (err, buff) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.writeFile(fileC, buff, (err) => {
    if (err) {
      console.error(err);
    }
  });
});

fs.readFile(fileB, 'utf-8', (err, buff) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.appendFile(fileC, buff, (err) => {
    if (err) {
      console.error(err);
    }
  });
});

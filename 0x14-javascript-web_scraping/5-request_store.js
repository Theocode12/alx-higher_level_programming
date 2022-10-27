#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const argv = require('process').argv.slice(2);
url = argv[0];
filename = argv[1];

request(url).pipe(fs.createWriteStream(filename));

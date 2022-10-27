#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const argv = require('process').argv.slice(2);
const url = argv[0];
const filename = argv[1];

request(url).pipe(fs.createWriteStream(filename));

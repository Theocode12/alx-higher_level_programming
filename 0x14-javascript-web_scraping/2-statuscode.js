#!/usr/bin/node

const request = require('request');
const argv = require('process').argv[2];

request.get(argv).on('response', (response) => {
  console.log('code:', response.statusCode);
});

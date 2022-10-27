#!/usr/bin/node

const request = require('request');
const argv = require('process').argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + argv;

request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(JSON.parse(body).title);
});

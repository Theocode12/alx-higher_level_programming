#!/usr/bin/node

const request = require('request');
const argv = require('process').argv.slice(2);

const url = 'https://swapi-api.hbtn.io/api/films/' + argv[0] + '/';
request.get(url, (err, resp, body) => {
  if (err) { console.error(err); }
  const charactersList = JSON.parse(body).characters;
  for (const characterUrl of charactersList) {
    request.get(characterUrl, (err, resp, body) => {
      if (err) { console.error(err); }
      console.log(JSON.parse(body).name);
    });
  }
});

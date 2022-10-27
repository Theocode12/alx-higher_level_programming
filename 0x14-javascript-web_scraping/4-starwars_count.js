#!/usr/bin/node

const request = require('request');
const argv = require('process').argv[2];

request.get(argv, (err, resp, body) => {
  if (err) {
    return console.log(err);
  }
  const films = JSON.parse(body).results;
  let filmNumber = 0;
  for (const film of films) {
    for (const character of film.characters) {
      if (character.endsWith('18/')) {
        filmNumber += 1;
        break;
      }
    }
  }
  console.log(filmNumber);
});

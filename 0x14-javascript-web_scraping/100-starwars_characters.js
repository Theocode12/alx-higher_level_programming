#!/usr/bin/node

const request = require('request');
const argv = require('process').argv.slice(2);

let url = "https://swapi-api.hbtn.io/api/films/" + argv[0] + "/";
request.get(url, (err, resp, body) => {
	charactersList = JSON.parse(body).characters;
	for (let characterUrl of charactersList){
		request.get(characterUrl, (err, resp, body) => {
			console.log(JSON.parse(body).name);
		})
	}
});

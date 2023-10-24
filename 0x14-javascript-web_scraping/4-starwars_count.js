#!/usr/bin/node
/*
Node.js script that prints the number of movies where
the character "Wedge Antilles" is present.
*/

const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (!error) {
  const films = JSON.parse(body).results;
  const count = films.filter(film => film.characters.includes(
    `https://swapi-api.alx-tools.com/api/people/${characterId}/`)).length;
  console.log(count);
  }
});

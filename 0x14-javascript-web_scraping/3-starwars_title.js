#!/usr/bin/node
/*
Node.js script that prints the title of a Star Wars movie where
the episode number matches a given integer.
*/

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) console.error(error);
  const movie = JSON.parse(body);
  console.log(movie.title);
});

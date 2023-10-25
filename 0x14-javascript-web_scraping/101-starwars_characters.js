#!/usr/bin/node
/*
Node.js script that prints all characters of a Star Wars movie
in the same order of the list "characters" in the /films/ response.
*/

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) console.error(error);
  const movie = JSON.parse(body);
  const characterUrls = movie.characters;

  for (let i = 0; i < characterUrls.length; i++) {
    const characterUrl = characterUrls[i];
    request(characterUrl, (error, response, body) => {
      if (error) console.error(error);
      const character = JSON.parse(body);
      console.log(character.name);
      i++;
    });
  }
});

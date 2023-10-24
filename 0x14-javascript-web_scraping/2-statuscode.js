#!/usr/bin/node
/*
Node.js script that displays the status code of a GET request.
*/

const request = require('request');
const url = process.argv[2];

request(url, (error, response) => {
  if (error) console.error(error);
  console.log(`code: ${response.statusCode}`);
});

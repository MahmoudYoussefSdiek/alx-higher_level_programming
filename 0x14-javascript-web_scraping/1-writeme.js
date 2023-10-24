#!/usr/bin/node
/*
Node.js script that writes a string to a file.
*/

const fs = require('fs');
const filePath = process.argv[2];
const fileContent = process.argv[3];

fs.writeFile(filePath, fileContent, 'utf-8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
});

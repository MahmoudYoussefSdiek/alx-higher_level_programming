#!/usr/bin/node
/*
Node.js script that computes the number of tasks completed by user id.
*/

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) console.error(error);
  const todos = JSON.parse(body);
  const completed = todos.filter(todo => todo.completed);
  const completedByUser = completed.reduce((acc, todo) => {
    if (acc[todo.userId]) {
      acc[todo.userId]++;
    } else {
      acc[todo.userId] = 1;
    }
    return acc;
  }, {});
  console.log(completedByUser);
});

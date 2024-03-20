#!/usr/bin/node

const request = require('request');
const myUrl = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[1];
request.get(myUrl + id).on('response', function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});

#!/usr/bin/node

const request = require('request');
const myUrl = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2]; // Corrected to use process.argv[2] for the film ID

request.get(myUrl + id + '/', (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  console.log(`Title: ${data.title}`);
});

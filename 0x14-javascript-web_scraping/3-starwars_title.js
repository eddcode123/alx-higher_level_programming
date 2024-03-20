#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

const Url = 'https://swapi-api.alx-tools.com/api';
request(Url + '/films/' + id, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});

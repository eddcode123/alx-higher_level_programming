#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const Url = 'https://swapi-api.alx-tools.com/api';
request(Url + '/films/' + argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});

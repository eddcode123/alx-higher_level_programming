#!/usr/bin/node

const request = require('request');
const myUrl = process.argv[2];
request.get(myUrl).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});

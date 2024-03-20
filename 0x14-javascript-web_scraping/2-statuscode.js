#!/usr/bin/node

const request = require('request');
const myUrl = process.argv[2];
request(myUrl, (response) => {
  console.log(`code: ${response.statusCode}`);
});

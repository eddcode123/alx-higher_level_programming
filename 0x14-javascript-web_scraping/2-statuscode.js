#!/usr/bin/node

const request = require('request');
const myUrl = process.argv[2];
const resp = request(myUrl, (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});

#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const myUrl = process.argv[2];
const path = process.argv[3];

request(myUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  fs.writeFile(path, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});

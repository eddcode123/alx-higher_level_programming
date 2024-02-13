#!/usr/bin/node
const args = process.argv;
const number = parseInt(args[2]);
if (!isNaN(number) && number >= 0) {
  for (let x = 0; x < number; x++) {
    let row = '';
    for (let y = 0; y < number; y++) {
      row += 'x';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}

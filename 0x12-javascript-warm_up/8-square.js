#!/usr/bin/node
const args = process.argv;
const number = parseInt(args[2]);

if (!isNaN(number)) {
  for (let x = 0; x < number; x++) {
    let row = '';
    for (let y = 0; y < number; y++) {
      row += 'x'; // Append 'x' to the row string
    }
    console.log(row); // Print the row
  }
} else {
  console.log('Not a number');
}

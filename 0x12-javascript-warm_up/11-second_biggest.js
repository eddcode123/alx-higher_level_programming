#!/usr/bin/node
function largeToSmallest (array) {
  const newArray = array.slice();
  newArray.sort((a, b) => b - a);
  return newArray;
}
const args = process.argv.slice(2).map(Number);
if (args.length < 2) {
  console.log('0');
} else {
  const sortedArgs = largeToSmallest(args);
  console.log(sortedArgs[1]);
}

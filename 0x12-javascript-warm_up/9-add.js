#!/usr/bin/node
const sum = (a, b) => {
  if (!isNaN(a) && !isNaN(b)) {
    return a + b;
  }
  return NaN;
};
console.log(sum(parseInt(process.argv[2]), parseInt(process.argv[3])));

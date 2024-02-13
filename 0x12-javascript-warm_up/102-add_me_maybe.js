#!/usr/bin/node
function addMeMaybe (number, myfunction) {
  number += 1;
  myfunction(number);
}
module.exports = {
  addMeMaybe
};

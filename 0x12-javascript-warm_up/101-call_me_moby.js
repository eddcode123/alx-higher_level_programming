#!/usr/bin/node
function callMeMoby (numberOfTimes, fun) {
  for (let i = 0; i < numberOfTimes; i++) {
    fun();
  }
}
module.exports = {
  callMeMoby
};

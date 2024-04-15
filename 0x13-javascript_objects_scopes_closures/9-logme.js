#!/usr/bin/node

let count = 0; // This variable is preserved in the closure of the logMe function

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++; // Increment the count for the next call
};

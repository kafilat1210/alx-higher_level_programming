#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = Object.entries(dict).reduce((acc, [userId, occurrence]) => {
  // If the occurrence key doesn't exist in the accumulator, create it
  if (!acc[occurrence]) {
    acc[occurrence] = [];
  }
  // Push the current userId to the array for this occurrence
  acc[occurrence].push(userId);
  return acc;
}, {});

// Convert the keys to numbers and sort the keys (occurrences)
const sortedDict = {};
Object.keys(newDict).sort((a, b) => a - b).forEach((key) => {
  sortedDict[key] = newDict[key].sort((a, b) => a - b);
});

console.log(sortedDict);

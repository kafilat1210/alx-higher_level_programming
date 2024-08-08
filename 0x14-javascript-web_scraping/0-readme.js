#!/usr/bin/node
// Import the fs and process modules
const fs = require('fs');
const process = require('process');

// Get the file path from the first argument
const filePath = process.argv[2];

// Read the file using the readFile method
fs.readFile(filePath, 'utf-8', (error, data) => {
  // If an error occurred, print the error object
  if (error) {
    console.error(error);
  } else {
    // Otherwise, print the data
    console.log(data);
  }
});

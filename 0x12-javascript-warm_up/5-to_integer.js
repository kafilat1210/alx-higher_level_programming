#!/usr/bin/node
// scripts that print integer

const num = Math.round(+process.argv[2]);
if (typeof num === 'number' && !isNaN(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}

#!/usr/bin/node
// script that prints the first args

const [, , firstArg] = process.argv;
if (firstArg) {
  console.log(firstArg);
} else {
  console.log('No argument');
}

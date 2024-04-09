#!/usr/bin/node
// script checks for arguments

const numArgs =process.argv.length - 2;
if (numArgs === 1){
	console.log('No argument');
} else if (numArgs === 1){
	console.log('Argument found');
} else {
	console.log('Arguments found');
}

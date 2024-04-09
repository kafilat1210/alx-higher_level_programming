#!/usr/bin/node
// script that prints  times `C is fun`

const x = +process.argv[2];
if (typeof x === 'number' && !isNaN(x)) {
	for(let i = 0; i < x; i++) {
		console.log('C is fun');
}
} else {
	console.log('Missing number of occurences');
}

#!/usr/bin/node
// prints number

const argv = process.argv.slice(2);

if (isNaN(argv)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argv);
}

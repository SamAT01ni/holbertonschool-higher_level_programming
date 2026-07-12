#!/usr/bin/node
// multi is also a betting term

const argv = process.argv.slice(2);

if (isNaN(argv)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < argv; i++) {
    console.log('C is fun');
  }
}

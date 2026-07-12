#!/usr/bin/node
// making squares

const argv = process.argv.slice(2);

if (isNaN(argv)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv; i++) {
    let row = '';
    for (let j = 0; j < argv; j++) {
      row += 'X';
    }
    console.log(row);
  }
}

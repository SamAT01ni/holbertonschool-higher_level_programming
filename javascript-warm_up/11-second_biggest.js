#!/usr/bin/node
// get 2nd biggest

const argv = process.argv.slice(2);
const argc = process.argv.length;

let biggest = -Infinity;
let second = -Infinity;

for (let i = 0; i < argc; i++) {
  if (Number(argv[i]) >= biggest) {
    second = biggest;
    biggest = argv[i];
  } else if (Number(argv[i]) >= second) {
    second = argv[i];
  }
}
if (argc <= 3) {
  console.log(0);
} else {
  console.log(second);
}

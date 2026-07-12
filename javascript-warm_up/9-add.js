#!/usr/bin/node
// addition and stuff

const argv = process.argv.slice(2);
const a = Number(argv[0]);
const b = Number(argv[1]);

function add (a, b) {
  return a + b;
}

console.log(add(a, b));

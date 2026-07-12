#!/usr/bin/node
// facorial wooo

const argv = process.argv.slice(2);

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }

  return n * factorial(n - 1);
}

console.log(factorial(argv));

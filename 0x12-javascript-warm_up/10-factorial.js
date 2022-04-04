#!/usr/bin/node
const argv = process.argv;
if (isNaN(argv[2])) {
  console.log('1');
} else {
  console.log(factorial(parseInt(argv[2])));
}

function factorial (n) {
  if (n == 0) {
    return n;
  }
  else {
    return (n + factorial(n - 1));
  }
}

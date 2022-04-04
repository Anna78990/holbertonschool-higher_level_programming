#!/usr/bin/node
const argv = process.argv;
if (argv[2]) {
  const n = argv[2];
  if (n > 0) {
    for (let i = 0; i < n; i++) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}

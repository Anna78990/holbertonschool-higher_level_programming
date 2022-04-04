#!/usr/bin/node
const argv = process.argv;
if (argv[2] && isNaN(argv[2]) === false) {
  const n = argv[2];
  if (n > 0) {
    const arr = [];
    for (let j = 0; j < n; j++) {
      arr.push('X');
    }
    const arr2 = arr.join('');
    for (let i = 0; i < n; i++) {
      console.log(arr2);
    }
  }
} else {
  console.log('Missing size');
}

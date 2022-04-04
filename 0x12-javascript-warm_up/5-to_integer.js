#!/usr/bin/node
const argv = process.argv;
let conv;
if (argv[2]) {
  conv = parseInt(argv[2]);
  if (isNaN(conv)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + conv);
  }
} else {
  console.log('Not a number');
}

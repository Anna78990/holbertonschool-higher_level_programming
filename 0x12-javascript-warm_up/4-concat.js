#!/usr/bin/node
const argv = process.argv;
let fst, sec;
if (argv[2]) {
  fst = argv[2];
} else {
  fst = 'undefined';
} if (argv[3]) {
  sec = argv[3];
} else {
  sec = 'undefined';
}
console.log(fst + ' is ' + sec);

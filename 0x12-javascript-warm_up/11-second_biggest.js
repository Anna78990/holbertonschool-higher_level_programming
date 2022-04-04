#!/usr/bin/node
const argv = process.argv;
if (argv[2] && argv[3]) {
  console.log(comp(argv));
} else {
  console.log(0);
}

function comp (args) {
  let n = parseInt(args[2]);
  let pi;
  for (let i = 3; i < args.length; i++) {
    pi = parseInt(args[i]);
    if (isNaN(pi) === false) {
      if (n < pi) {
        n = pi;
      }
    }
  }
  return (n);
}

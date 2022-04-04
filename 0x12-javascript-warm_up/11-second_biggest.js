#!/usr/bin/node
const argv = process.argv;
if (argv[2] && argv[3]) {
  const n = comp(argv);
  const arr = [NaN, NaN];
  for (let z = 2; z < argv.length; z++) {
    if (parseInt(argv[z]) !== n) {
      arr.push(parseInt(argv[z]));
    }
  }
  console.log(comp(arr));
} else {
  console.log(0);
}

function comp (args) {
  let n = parseInt(args[2]);
  let pi;
  for (let i = 3; i < args.length; i++) {
    pi = parseInt(args[i]);
    if (n < pi) {
      n = pi;
    }
  }
  return (n);
}

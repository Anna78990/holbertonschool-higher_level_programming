#!/usr/bin/node
const argv = process.argv;
if (argv[2]) {
  if (argv[3]) {
    console.log(comp(argv));
  } else if (parseInt(argv[2]) === 1) {
    console.log('0');
  } else {
    console.log(parseInt(argv[2]));
  }
} else {
  console.log(0);
}

function comp (args) {
  let n = parseInt(args[2]);
  for (let i = 3; i < args.length; i++) {
    if (n < parseInt(args[i])) {
      n = parseInt(args[i]);
    }
  }
  return (n);
}

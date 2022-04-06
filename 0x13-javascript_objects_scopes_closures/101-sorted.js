#!/usr/bin/node
const dict = require('./101-data.js').dict;
let m = 0;
const obj = {};
for (const [, value] of Object.entries(dict)) {
  if (value > m) {
    m = value;
  }
}
for (let i = 1; i <= m; i++) {
  const arr = [];
  for (const [key, value] of Object.entries(dict)) {
    if (value === i) {
      arr.push(key);
    }
  }
  obj[i] = arr;
}

console.log(obj);

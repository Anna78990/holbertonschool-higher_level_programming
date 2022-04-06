#!/usr/bin/node
const dict = require('./101-data.js').dict;
const index = [];
const obj = {};
for (const [, value] of Object.entries(dict)) {
  if (index[0]) {
    for (let i = 0; i < index.length; i++) {
      if (index[i] === value) {
        break;
      } else if (index[i] !== value && i === index.length - 1) {
        index.push(value);
      }
    }
  } else {
    index.push(value);
  }
}

for (let i = 0; i < index.length; i++) {
  const arr = [];
  for (const [key, value] of Object.entries(dict)) {
    if (value === index[i]) {
      arr.push(key);
    }
  }
  const idx = index[i];
  if (arr) {
    obj[idx] = arr;
  }
}
console.log(obj);

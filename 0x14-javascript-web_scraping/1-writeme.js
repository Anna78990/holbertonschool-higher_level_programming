#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];
const contents = process.argv[3];
fs.writeFile(path, '\ufeff' + contents, err => {
  if (err) {
    console.error(err);
  }
});

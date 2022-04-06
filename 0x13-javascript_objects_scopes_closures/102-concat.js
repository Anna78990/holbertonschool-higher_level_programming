#!/usr/bin/node
fs = require('fs');
fs.readFile('fileA', 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  }

});

#!/usr/bin/node
const https = require('https');
const path = process.argv[2];

https.get(path, function (res) {
  console.log('code: ', res.statusCode); // <======= Here's the status code
});

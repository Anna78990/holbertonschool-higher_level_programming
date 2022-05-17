#!/usr/bin/node
const axios = require('axios').default;
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

axios.get(url)
  .then(function (response) {
    const dic = response.data;
    fs.writeFileSync(file, dic);
  })
  .catch(function (error) {
    console.log(error);
  });

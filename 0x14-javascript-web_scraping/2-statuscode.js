#!/usr/bin/node
const axios = require('axios').default;
const path = process.argv[2];

axios.get(path)
  .then(function (response) {
    console.log('code:', response.status);
  })
  .catch(function (error) {
    console.log('code:', error.response.status);
  });

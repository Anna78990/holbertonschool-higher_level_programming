#!/usr/bin/node
const axios = require('axios').default;
const path = process.argv[2];

axios.get('https://swapi-api.hbtn.io/api/films/' + path)
  .then(function (response) {
    console.log(response.data.title);
  })
  .catch(function (error) {
    console.log(error);
  });

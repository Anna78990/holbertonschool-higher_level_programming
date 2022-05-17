#!/usr/bin/node
const axios = require('axios').default;

const url = process.argv[2];

axios.get(url)
  .then(function (response) {
    const list = response.data;
    const dict = {};
    for (let i = 0; i < list.length; i++) {
      if (list[i].completed === true) {
        if (!(list[i].userId in dict)) {
          dict[list[i].userId] = 1;
        } else {
          dict[list[i].userId] += 1;
        }
      }
    }
    console.log(dict);
  })
  .catch(function (error) {
    console.log(error);
  });

#!/usr/bin/node
const axios = require('axios').default;
const url = process.argv[2];

axios.get(url)
  .then(function (response) {
    let ctr = 0;
    const dic = response.data.results;
    for (let i = 0; i < dic.length; i++) {
      const charaL = dic[i].characters;
      for (let j = 0; j < charaL.length; j++) {
        if (charaL[j].includes('/18/') === true) {
          ctr++;
        }
      }
    }
    console.log(ctr);
  })
  .catch(function (error) {
    console.log(error);
  });

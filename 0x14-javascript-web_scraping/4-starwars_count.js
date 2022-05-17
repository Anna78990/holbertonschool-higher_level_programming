#!/usr/bin/node
const axios = require('axios').default;

axios.get('https://swapi-api.hbtn.io/api/films/')
  .then(function (response) {
    let ctr = 0;
    const dic = response.data.results;
    for (let i = 0; i < dic.length; i++) {
      const dicI = dic[i];
      for (const [key] of Object.entries(dicI)) {
        if (key === 'characters') {
          const charaL = dicI.characters;
          if (charaL.includes('https://swapi-api.hbtn.io/api/people/18/')) {
            ctr += 1;
          }
        }
      }
    }
    console.log(ctr);
  })
  .catch(function (error) {
    console.log(error);
  });

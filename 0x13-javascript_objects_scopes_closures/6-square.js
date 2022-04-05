#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    if (this.width !== undefined) {
      const arr = [];
      for (let i = 0; i < this.width; i++) {
        arr.push(c);
      }
      const arr2 = arr.join('');
      for (let j = 0; j < this.width; j++) {
        console.log(arr2);
      }
    }
  }
};

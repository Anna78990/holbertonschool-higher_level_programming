#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w = 0, h = 0) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width !== undefined && this.height !== undefined) {
      const arr = [];
      for (let i = 0; i < this.width; i++) {
        arr.push('X');
      }
      const arr2 = arr.join('');
      for (let j = 0; j < this.height; j++) {
        console.log(arr2);
      }
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }
};

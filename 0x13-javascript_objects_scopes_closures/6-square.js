#!/usr/bin/node
const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let p = '';
      for (let j = 0; j < this.width; j++) {
        p += c;
      }
      console.log(p);
    }
  }
}

module.exports = Square;

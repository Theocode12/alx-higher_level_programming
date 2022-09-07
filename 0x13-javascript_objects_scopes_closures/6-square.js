#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size);
    this.height = size;
    this.width = size;
  }

  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      let h, w;
      let result = '';
      for (h = 0; h < this.height; h++) {
        for (w = 0; w < this.width; w++) {
          result += c;
        }
        if (h < this.height - 1) { result += '\n'; }
      }
      console.log(result);
    }
  }
}

module.exports = Square;

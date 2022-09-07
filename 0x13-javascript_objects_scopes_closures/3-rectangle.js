#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let h, w;
    let result = '';
    for (h = 0; h < this.height; h++) {
      for (w = 0; w < this.width; w++) {
        result += 'X';
      }
      if (h < this.height - 1) { result += '\n'; }
    }
    console.log(result);
  }
};

#!/usr/bin/node
const BaseSquare = require('./5-square');
class Square extends BaseSquare {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.size; i++) {
        let row = '';
        for (let j = 0; j < this.size; j++) {
          row += c;
        }
        console.log(row);
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;

#!/usr/bin/node
exports.esrever = function (list) {
  let reverse_list = [];
  for (let i = 0, j = list.length - 1; i < list.length; i++, j--) {
    reverse_list[i] = list[j];
  }
  return reverse_list;
};

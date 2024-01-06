#!/usr/bin/node
exports.esrever = function (list) {
  const reverseList = [];
  for (let i = 0, j = list.length - 1; i < list.length; i++, j--) {
    reverseList[i] = list[j];
  }
  return reverseList;
};

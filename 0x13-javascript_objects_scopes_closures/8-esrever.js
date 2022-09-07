#!/usr/bin/node

exports.esrever = function (list) {
  let numOfItems = list.length - 1;
  for (let index = 0; index < numOfItems; index++, numOfItems--) {
    const tmp = list[index];
    list[index] = list[numOfItems];
    list[numOfItems] = tmp;
  }
  return list;
};

#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numOfSearches = 0;
  for (const element of list) {
    if (element === searchElement) { numOfSearches++; }
  }
  return numOfSearches;
};

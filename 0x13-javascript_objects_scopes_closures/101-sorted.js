#!/usr/bin/node
const dict = require('./101-data.js').dict;
const kVs = Object.entries(dict);
const newDict = {};

kVs.forEach((kV) => {
  const key = kV[0];
  const value = kV[1];
  const newKey = Object.keys(newDict);
  if (newKey.includes(value.toString())) {
    newDict[value].push(key);
  } else {
    newDict[value] = [key];
  }
});

console.log(newDict);

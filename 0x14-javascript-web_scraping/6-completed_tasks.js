#!/usr/bin/node

const request = require('request');
const argv = require('process').argv.slice(2);

const completedTask = {};
request.get(argv[0], (err, resp, body) => {
  if (err) {
    return console.log(err);
  }
  const tasks = JSON.parse(body);
  for (const task of tasks) {
    if (task.userId in completedTask) {
      if (task.completed === true) {
        completedTask[task.userId] += 1;
      }
    } else {
      if (task.completed === true) {
        completedTask[task.userId] = 1;
      }
    }
  }
  console.log(completedTask);
});

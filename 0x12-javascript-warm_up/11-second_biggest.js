#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const numbers = process.argv;
  numbers.sort(function (a, b) {
    return (a - b);
  });
  console.log(numbers[numbers.length - 2]);
}

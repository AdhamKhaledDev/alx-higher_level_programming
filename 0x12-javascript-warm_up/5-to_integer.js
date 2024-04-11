#!/usr/bin/node
function printNumber (argument) {
  if (isNaN(argument) || argument === undefined) {
    console.log('Not a number');
  } else {
    console.log('My number:', parseInt(argument));
  }
}

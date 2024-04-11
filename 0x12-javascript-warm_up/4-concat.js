#!/usr/bin/node
function printTwoArguments (arg1, arg2) {
  if (arguments.length < 2) {
    console.log('Error: Missing arguments. Please provide two arguments.');
    return;
  }

  console.log(`${arg1} is ${arg2}`);
}

printTwoArguments('This', 'that');

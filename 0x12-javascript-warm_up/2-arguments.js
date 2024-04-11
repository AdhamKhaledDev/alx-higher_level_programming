#!/usr/bin/node
function printArgumentMessage() {
    const argumentCount = arguments.length;
  
    if (argumentCount === 0) {
        console.log("No argument");
      } else if (argumentCount === 1) {
        console.log("Argument found");
      } else {
        console.log("Arguments found");
      }
    }

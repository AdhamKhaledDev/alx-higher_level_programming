function printMessage (argument) {
  if (argument === undefined) {
    console.log('Missing number of occurrences');
    return; // Exit the function if no argument
  }

  if (isNaN(parseInt(argument))) {
    console.log('Missing number of occurrences');
    return; // Exit the function if not a number
  }

  for (let i = 0; i < argument; i++) {
    console.log('C is fun');
  }
}

// Call the function with the first argument (replace with your desired input)
printMessage(process.argv[2]); // For Node.js execution

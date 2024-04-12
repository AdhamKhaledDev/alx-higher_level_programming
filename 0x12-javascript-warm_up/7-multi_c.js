function printMessage (argument) {
  if (argument === undefined) {
    console.log('Missing number of occurrences');
    return;
  }

  if (isNaN(parseInt(argument))) {
    console.log('Missing number of occurrences');
    return;
  }

  for (let i = 0; i < argument; i++) {
    console.log('C is fun');
  }
}

printMessage(process.argv[2]);

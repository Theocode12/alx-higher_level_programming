#!/usr/bin/node

require('process');
const argv = process.argv;
let result = '';
let num; let i = 0, j = 0;

if (argv.length === 2)
{
    console.log('Missing number of occurrences');
}
else {
  num = parseInt(argv[2]);
  if (typeof(num) === "number" )
  {
    for(; i<num && num > 0; i++)
    {
        for(j = 0; j<num; j++)
        {
            result += 'X'
        }
        if (i < num - 1)
            result += '\n';
    }
    if (result)
        console.log(result);
  }
  else
    console.log('Missing number of occurrences');
}

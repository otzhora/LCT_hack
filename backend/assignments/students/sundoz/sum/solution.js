var readline = require('readline');
var rl = readline.createInterface({
     input: process.stdin,
     output: process.stdout,
     terminal: false
});

rl.on('line', function(line){
	var z = line.split(' ');
	var ans =parseInt( z[0]) + parseInt(z[1]);
	console.log(ans);
	rl.close()
})




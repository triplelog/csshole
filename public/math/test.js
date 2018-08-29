var katex = require('./katex.js');

var fileString = "sine = {";
var numers = [1,5,7,11]
for (i=0;i<4;i++) {
	for (turni=-8;turni<17;turni++){
		var numer = numers[i]+12*turni;
		if (numer == 1){
			var katexString = katex.renderToString("\\sin(\\frac{\\pi}{6})", {
				throwOnError: false
			});
			fileString += "'"+numer+"pi6':'" + katexString + "',";
		}
		else if (numer == -1){
			var katexString = katex.renderToString("\\sin(\\frac{-\\pi}{6})", {
				throwOnError: false
			});
			fileString += "'n1pi6':'" + katexString + "',";
		}
		else {
			var katexString = katex.renderToString("\\sin(\\frac{"+numer+"\\pi}{6})", {
				throwOnError: false
			});
			if (numer < 0){
				fileString += "'n"+Math.abs(numer)+"pi6':'" + katexString + "',";
			}
			else {
				fileString += "'"+numer+"pi6':'" + katexString + "',";
			}
		}
	}
	
}
var numers = [1,3,5,7]
var denom = 4
for (i=0;i<4;i++) {
	for (turni=-8;turni<17;turni++){
		var numer = numers[i]+2*denom*turni;
		if (numer == 1){
			var katexString = katex.renderToString("\\sin(\\frac{\\pi}{"+denom+"})", {
				throwOnError: false
			});
			fileString += "'"+numer+"pi"+denom+"':'" + katexString + "',";
		}
		else if (numer == -1){
			var katexString = katex.renderToString("\\sin(\\frac{-\\pi}{"+denom+"})", {
				throwOnError: false
			});
			fileString += "'n1pi"+denom+"':'" + katexString + "',";
		}
		else {
			var katexString = katex.renderToString("\\sin(\\frac{"+numer+"\\pi}{"+denom+"})", {
				throwOnError: false
			});
			if (numer < 0){
				fileString += "'n"+Math.abs(numer)+"pi"+denom+"':'" + katexString + "',";
			}
			else {
				fileString += "'"+numer+"pi"+denom+"':'" + katexString + "',";
			}
		}
	}
	
}

var numers = [1,2,4,5]
var denom = 3
for (i=0;i<4;i++) {
	for (turni=-8;turni<17;turni++){
		var numer = numers[i]+2*denom*turni;
		if (numer == 1){
			var katexString = katex.renderToString("\\sin(\\frac{\\pi}{"+denom+"})", {
				throwOnError: false
			});
			fileString += "'"+numer+"pi"+denom+"':'" + katexString + "',";
		}
		else if (numer == -1){
			var katexString = katex.renderToString("\\sin(\\frac{-\\pi}{"+denom+"})", {
				throwOnError: false
			});
			fileString += "'n1pi"+denom+"':'" + katexString + "',";
		}
		else {
			var katexString = katex.renderToString("\\sin(\\frac{"+numer+"\\pi}{"+denom+"})", {
				throwOnError: false
			});
			if (numer < 0){
				fileString += "'n"+Math.abs(numer)+"pi"+denom+"':'" + katexString + "',";
			}
			else {
				fileString += "'"+numer+"pi"+denom+"':'" + katexString + "',";
			}
		}
	}
	
}

var numers = [1,3]
var denom = 2
for (i=0;i<2;i++) {
	for (turni=-8;turni<17;turni++){
		var numer = numers[i]+2*denom*turni;
		if (numer == 1){
			var katexString = katex.renderToString("\\sin(\\frac{\\pi}{"+denom+"})", {
				throwOnError: false
			});
			fileString += "'"+numer+"pi"+denom+"':'" + katexString + "',";
		}
		else if (numer == -1){
			var katexString = katex.renderToString("\\sin(\\frac{-\\pi}{"+denom+"})", {
				throwOnError: false
			});
			fileString += "'n1pi"+denom+"':'" + katexString + "',";
		}
		else {
			var katexString = katex.renderToString("\\sin(\\frac{"+numer+"\\pi}{"+denom+"})", {
				throwOnError: false
			});
			if (numer < 0){
				fileString += "'n"+Math.abs(numer)+"pi"+denom+"':'" + katexString + "',";
			}
			else {
				fileString += "'"+numer+"pi"+denom+"':'" + katexString + "',";
			}
		}
	}
	
}

var numers = [0,1]
var denom = 1
for (i=0;i<2;i++) {
	for (turni=-8;turni<17;turni++){
		var numer = numers[i]+2*denom*turni;
		if (numer == 1){
			var katexString = katex.renderToString("\\sin(\\pi)", {
				throwOnError: false
			});
			fileString += "'"+numer+"pi"+denom+"':'" + katexString + "',";
		}
		else if (numer == -1){
			var katexString = katex.renderToString("\\sin(-\\pi)", {
				throwOnError: false
			});
			fileString += "'n1pi"+denom+"':'" + katexString + "',";
		}
		else if (numer == 0){
			var katexString = katex.renderToString("\\sin(0)", {
				throwOnError: false
			});
			fileString += "'"+numer+"pi"+denom+"':'" + katexString + "',";
		}
		else {
			var katexString = katex.renderToString("\\sin("+numer+"\\pi)", {
				throwOnError: false
			});
			if (numer < 0){
				fileString += "'n"+Math.abs(numer)+"pi"+denom+"':'" + katexString + "',";
			}
			else {
				fileString += "'"+numer+"pi"+denom+"':'" + katexString + "',";
			}
		}
	}
	
}




function fortrig(trigabb) {
	var numers = [1,5,7,11]
	var denom = 6
	for (i=0;i<4;i++) {
		for (turni=-8;turni<17;turni++){
			var numer = numers[i]+12*turni;
			if (numer == 1){
				var katexString = katex.renderToString("\\"+trigabb+"(\\frac{\\pi}{6})", {
					throwOnError: false
				});
				fileString += "'"+numer+"pi6':'" + katexString + "',";
			}
			else if (numer == -1){
				var katexString = katex.renderToString("\\"+trigabb+"(\\frac{-\\pi}{"+denom+"})", {
					throwOnError: false
				});
				fileString += "'n1pi"+denom+"':'" + katexString + "',";
			}
			else {
				var katexString = katex.renderToString("\\"+trigabb+"(\\frac{"+numer+"\\pi}{6})", {
					throwOnError: false
				});
				if (numer < 0){
					fileString += "'n"+Math.abs(numer)+"pi6':'" + katexString + "',";
				}
				else {
					fileString += "'"+numer+"pi6':'" + katexString + "',";
				}
			}
		}
	
	}
	var numers = [1,3,5,7]
	var denom = 4
	for (i=0;i<4;i++) {
		for (turni=-8;turni<17;turni++){
			var numer = numers[i]+2*denom*turni;
			if (numer == 1){
				var katexString = katex.renderToString("\\"+trigabb+"(\\frac{\\pi}{"+denom+"})", {
					throwOnError: false
				});
				fileString += "'"+numer+"pi"+denom+"':'" + katexString + "',";
			}
			else if (numer == -1){
				var katexString = katex.renderToString("\\"+trigabb+"(\\frac{-\\pi}{"+denom+"})", {
					throwOnError: false
				});
				fileString += "'n1pi"+denom+"':'" + katexString + "',";
			}
			else {
				var katexString = katex.renderToString("\\"+trigabb+"(\\frac{"+numer+"\\pi}{"+denom+"})", {
					throwOnError: false
				});
				if (numer < 0){
					fileString += "'n"+Math.abs(numer)+"pi"+denom+"':'" + katexString + "',";
				}
				else {
					fileString += "'"+numer+"pi"+denom+"':'" + katexString + "',";
				}
			}
		}
	
	}

	var numers = [1,2,4,5]
	var denom = 3
	for (i=0;i<4;i++) {
		for (turni=-8;turni<17;turni++){
			var numer = numers[i]+2*denom*turni;
			if (numer == 1){
				var katexString = katex.renderToString("\\"+trigabb+"(\\frac{\\pi}{"+denom+"})", {
					throwOnError: false
				});
				fileString += "'"+numer+"pi"+denom+"':'" + katexString + "',";
			}
			else if (numer == -1){
				var katexString = katex.renderToString("\\"+trigabb+"(\\frac{-\\pi}{"+denom+"})", {
					throwOnError: false
				});
				fileString += "'n1pi"+denom+"':'" + katexString + "',";
			}
			else {
				var katexString = katex.renderToString("\\"+trigabb+"(\\frac{"+numer+"\\pi}{"+denom+"})", {
					throwOnError: false
				});
				if (numer < 0){
					fileString += "'n"+Math.abs(numer)+"pi"+denom+"':'" + katexString + "',";
				}
				else {
					fileString += "'"+numer+"pi"+denom+"':'" + katexString + "',";
				}
			}
		}
	
	}

	var numers = [1,3]
	var denom = 2
	for (i=0;i<2;i++) {
		for (turni=-8;turni<17;turni++){
			var numer = numers[i]+2*denom*turni;
			if (numer == 1){
				var katexString = katex.renderToString("\\"+trigabb+"(\\frac{\\pi}{"+denom+"})", {
					throwOnError: false
				});
				fileString += "'"+numer+"pi"+denom+"':'" + katexString + "',";
			}
			else if (numer == -1){
				var katexString = katex.renderToString("\\"+trigabb+"(\\frac{-\\pi}{"+denom+"})", {
					throwOnError: false
				});
				fileString += "'n1pi"+denom+"':'" + katexString + "',";
			}
			else {
				var katexString = katex.renderToString("\\"+trigabb+"(\\frac{"+numer+"\\pi}{"+denom+"})", {
					throwOnError: false
				});
				if (numer < 0){
					fileString += "'n"+Math.abs(numer)+"pi"+denom+"':'" + katexString + "',";
				}
				else {
					fileString += "'"+numer+"pi"+denom+"':'" + katexString + "',";
				}
			}
		}
	
	}

	var numers = [0,1]
	var denom = 1
	for (i=0;i<2;i++) {
		for (turni=-8;turni<17;turni++){
			var numer = numers[i]+2*denom*turni;
			if (numer == 1){
				var katexString = katex.renderToString("\\"+trigabb+"(\\pi)", {
					throwOnError: false
				});
				fileString += "'"+numer+"pi"+denom+"':'" + katexString + "',";
			}
			else if (numer == -1){
				var katexString = katex.renderToString("\\"+trigabb+"(-\\pi)", {
					throwOnError: false
				});
				fileString += "'n1pi"+denom+"':'" + katexString + "',";
			}
			else if (numer == 0){
				var katexString = katex.renderToString("\\"+trigabb+"(0)", {
					throwOnError: false
				});
				fileString += "'"+numer+"pi"+denom+"':'" + katexString + "',";
			}
			else {
				var katexString = katex.renderToString("\\"+trigabb+"("+numer+"\\pi)", {
					throwOnError: false
				});
				if (numer < 0){
					fileString += "'n"+Math.abs(numer)+"pi"+denom+"':'" + katexString + "',";
				}
				else {
					fileString += "'"+numer+"pi"+denom+"':'" + katexString + "',";
				}
			}
		}
	
	}
}

fileString += '}\ncosine = {';
fortrig('cos');
fileString += '}\ntangent = {';
fortrig('tan');
fileString += '}\ncotangent = {';
fortrig('cot');
fileString += '}\nsecant = {';
fortrig('sec');
fileString += '}\ncosecant = {';
fortrig('csc');


var fs = require('fs');
fs.writeFile("testOutput.txt", fileString+'}', function(err) {
    if(err) {
        return console.log(err);
    }
    console.log("The file was saved!");
}); 
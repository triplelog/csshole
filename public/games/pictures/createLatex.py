sudoku = "8.93.65.2..47589..3.......1.9.....8.5.......94.......326..3..14...6.5.......4...."

for ii in range(0,9):
	rowStr = "\setrow "
	for i in sudoku[ii*9:ii*9+9]:
		if i == ".":
			rowStr+="{ }"
		else:
			rowStr += "{"+i+"}"
	print(rowStr)
print("")
print("")
print("")
for ii in range(0,9):
	rowStr = "\setrow "
	for i in sudoku[ii*9:ii*9+9]:
		if i == ".":
			rowStr+="{ }"
		else:
			rowStr += "{\includegraphics[width=12]{farm"+i+".png}}"
	print(rowStr)
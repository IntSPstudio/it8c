#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this library!
# Plugin: Data handling
#|==============================================================|#

#|COM|==========================================================|#
#MAKE INPUT TO ONLY LETTRS AND DIGITS
def lettersdigits(input,alt):
	return str(alt).join(i for i in input if i.isalnum())
#CHECK IF IT IS NUMBER
def checkIfItIsNumber(input):
    try:
        int(input)
        return 1
    except ValueError:
        return 0
#|1D ARRAY|=====================================================|#
#MAKE 1D ARRAY
def create1Darray(arraySize,arrayContent):
	return [arrayContent for xp in range(arraySize)]
#PRINT 1D ARRAY 
def print1DarrayContent(array,separator):
	arrayWidth = len(array)
	arrayOutput =""
	for i in range(0, arrayWidth):
		point = str(array[i])
		if arrayOutput !="":
			arrayOutput = arrayOutput + separator + point
		else:
			arrayOutput = point
	return arrayOutput
#CALCULATE AVARAGE VALUE 1D ARRAY
def calcAvg1DarrayContent(array):
	arrayWidth = len(array)
	arrayOutput =0
	arrayCounter =0
	for i in range(0, arrayWidth):
		point = array[i]
		check = checkIfItIsNumber(point)
		if check == 1:
			arrayCounter = arrayCounter +1
			arrayOutput = arrayOutput + int(point)
	if arrayCounter > 0:
		return arrayOutput / arrayCounter
	else:
		return 0
#CALCULATE SUM VALUE 1D ARRAY
def calcSum1DarrayContent(array):
	arrayWidth = len(array)
	arrayOutput =0
	for i in range(0, arrayWidth):
		point = array[i]
		check = checkIfItIsNumber(point)
		if check == 1:
			arrayOutput = arrayOutput + int(point)
	return arrayOutput
#|2D ARRAY|=====================================================|#
#MAKE 2D ARRAY
def create2Darray(arrayHeight,arrayWidth,arrayContent):
	return [[arrayContent for xp in range(arrayWidth)] for yp in range(arrayHeight)]
#PRINT 2D ARRAY
def print2DarrayContent(array,separator):
	arrayHeight = len(array)
	arrayPrintMap =""
	arraySeparatorV ="\n"
	for yp in range(0, arrayHeight):
		arrayWidth = len(array[yp])
		for xp in range(0, arrayWidth):
			point = str(array[yp][xp])
			if point !="":
				if xp == 0:
					arrayPrintMap = arrayPrintMap + point
				else:
					arrayPrintMap = arrayPrintMap + separator + point
		if yp < arrayHeight -1:
			arrayPrintMap = arrayPrintMap + arraySeparatorV
	return arrayPrintMap
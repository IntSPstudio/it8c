#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this library!
# Plugin: Data handling
#|==============================================================|#

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
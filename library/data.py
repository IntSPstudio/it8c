#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this library!
# Plugin: Data handling
#|==============================================================|#

#|COM|==========================================================|#
#MAKE INPUT TO ONLY LETTRS AND DIGITS
def lettersdigits(input,alt):
	return str(alt).join(i for i in input if i.isalnum())
#CHECK IF IT IS A NUMBER
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
#MAKE 1D ARRAY TO 2D ARRAY
def make1Darray2Darray(array1Content,array2DefContent,array2Width):
	array1Width =  len(array1Content)
	array2Height =0
	xp =0
	for i in range(0, array1Width):
		xp +=1
		if xp >= array2Width:
			array2Height +=1
			xp =0
	array2Content = create2Darray(array2Height,array2Width,array2DefContent)
	xp =0
	yp =0
	for i in range(0, array1Width):
		if xp == array2Width:
			xp =0
			yp +=1
		array2Content[yp][xp] = array1Content[i]
		xp +=1
	return array2Content
#PRINT 1D ARRAY 
def print1DarrayContent(arrayContent,separator):
	arrayWidth = len(arrayContent)
	arrayOutput =""
	for i in range(0, arrayWidth):
		point = str(arrayContent[i])
		if arrayOutput !="":
			arrayOutput = arrayOutput + separator + point
		else:
			arrayOutput = point
	return arrayOutput
#CALCULATE AVARAGE VALUE
def calcAvg1DarrayContent(arrayContent):
	arrayWidth = len(arrayContent)
	arrayOutput =0
	arrayCounter =0
	for i in range(0, arrayWidth):
		point = arrayContent[i]
		check = checkIfItIsNumber(point)
		if check == 1:
			arrayCounter = arrayCounter +1
			arrayOutput = arrayOutput + int(point)
	if arrayCounter > 0:
		return arrayOutput / arrayCounter
	else:
		return 0
#CALCULATE SUM VALUE
def calcSum1DarrayContent(arrayContent):
	arrayWidth = len(arrayContent)
	arrayOutput =0
	for i in range(0, arrayWidth):
		point = arrayContent[i]
		check = checkIfItIsNumber(point)
		if check == 1:
			arrayOutput = arrayOutput + int(point)
	return arrayOutput
#CHECK MAX VALUE
def checkMaxValue1DarrayContent(arrayContent):
	arrayWidth = len(arrayContent)
	arrayOutput =0
	for i in range(0, arrayWidth):
		point = arrayContent[i]
		check = checkIfItIsNumber(point)
		if check == 1:
			point = int(point)
			if point > arrayOutput:
				arrayOutput = point
	return arrayOutput
#CHECK 1D ARRAY OBJECTS
def check1DarrayObjects(array1Content):
	array1Content = sorted(array1Content)
	array1Width = len(array1Content)
	pointa =""
	for i in range(0,2):
		if i == 1:
			checkHeight = ypb
			checkWidth =3
			checkContent = create2Darray(checkHeight,checkWidth,"")
		ypb =0
		for ypa in range(0, array1Width):
			pointb = str(array1Content[ypa])
			if pointb !="":
				if pointb != pointa:
					if i == 1:
						checkContent[ypb][0] = str(ypb +1)
						checkContent[ypb][2] = pointb
					ypb +=1
				pointa = pointb
	for ypa in range(0,checkHeight):
		checka =0
		pointa = str(checkContent[ypa][2])
		for ypb in range(0,array1Width):
			pointb = str(array1Content[ypb])
			if pointa == pointb:
				checka +=1
		checkContent[ypa][1] = str(checka)
	return checkContent
#CONTENT FORMAT
def change1DarrayContentFormat(arrayContent,arrayMode):
	arrayWidth = len(arrayContent)
	for yp in range(0, arrayWidth):
		pointa = str(arrayContent[yp])
		if arrayMode == 1:
			pointb = str.lower(pointa)
		elif arrayMode == 2:
			pointb = str.upper(pointa)
		elif arrayMode == 3:
			pointb = lettersdigits(pointa,"") 
		elif arrayMode == 4:
			check = checkIfItIsNumber(pointa)
			if check == 1:
				pointb = int(pointa)
			else:
				pointb =0
		arrayContent[yp] = pointb
	return arrayContent
#FLIP OBJECTS
def flip1DarrayObjects(array1Content):
	array1Length = len(array1Content)
	array2Content = create1Darray(array1Length,"")
	for ypa in range(0,array1Length):
		ypb = array1Length -ypa -1
		array2Content[ypa] = array1Content[ypb]
	return array2Content
#|2D ARRAY|=====================================================|#
#MAKE 2D ARRAY
def create2Darray(arrayHeight,arrayWidth,arrayContent):
	return [[arrayContent for xp in range(arrayWidth)] for yp in range(arrayHeight)]
#MAKE 2D ARRAY TO 1D ARRAY
def make2Darray1Darray(array1Content):
	array1Height = len(array1Content)
	array1Width =  len(array1Content[0])
	array1Counter =0
	array2Width = array1Height * array1Width
	array2Content = create1Darray(array2Width,"")
	for yp in range(0, array1Height):
		for xp in range(0, array1Width):
			array2Content[array1Counter] = array1Content[yp][xp]
			array1Counter +=1
	return array2Content
#PRINT 2D ARRAY
def print2DarrayContent(arrayContent,separator):
	arrayHeight = len(arrayContent)
	arrayWidth = len(arrayContent[0])
	arrayPrintMap =""
	arraySeparatorV ="\n"
	for yp in range(0, arrayHeight):
		for xp in range(0, arrayWidth):
			point = str(arrayContent[yp][xp])
			if point !="":
				if xp == 0:
					arrayPrintMap = arrayPrintMap + point
				else:
					arrayPrintMap = arrayPrintMap + separator + point
		if yp < arrayHeight -1:
			arrayPrintMap = arrayPrintMap + arraySeparatorV
	return arrayPrintMap
#SMART PRINT 2D ARRAY
def sprint2DarrayContent(array1Content,separator,fill,contentMode):
	array1Height = len(array1Content)
	array1Width = len(array1Content[0])
	arrayRowSpWidth = create1Darray(array1Width,"")
	array2Height = array1Height
	array2Width = array1Width
	array2Content = create2Darray(array2Height,array2Width,"")
	for xp in range(0,array1Width):
		contenta = extract2DarrayColumn(array1Content,xp)
		contentaLength = len(contenta)
		checka =0
		for yp in range(0,contentaLength):
			checkb = len(str(contenta[yp]))
			if checkb > checka:
				checka = checkb
		arrayRowSpWidth[xp] = checka
	for yp in range(0,array1Height):
		for xp in range(0,array1Width):
			pointa = str(array1Content[yp][xp])
			checka = len(pointa)
			checkb = arrayRowSpWidth[xp] - checka
			checkc = checkIfItIsNumber(pointa)
			if checkb > 0:
				pointb =""
				for x in range(0, checkb):
					if contentMode == 1:
						pointb = pointb + fill
					else:
						pointb = pointb + " "
				if checkc == 0:
					pointc = pointa + pointb
				else:
					pointc = pointb + pointa
			else:
				pointc = pointa
			array2Content[yp][xp] = pointc
	return print2DarrayContent(array2Content,separator)
#CALCULATE AVARAGE VALUE
def calcAvg2DarrayContent(arrayContent):
	return calcAvg1DarrayContent(make2Darray1Darray(arrayContent))
#CALCULATE SUM VALUE
def calcSum2DarrayContent(arrayContent):
	return calcSum1DarrayContent(make2Darray1Darray(arrayContent))
#CHECK MAX VALUE
def checkMaxValue2DarrayContent(arrayContent):
	return checkMaxValue1DarrayContent(make2Darray1Darray(arrayContent))
#CHECK 2D ARRAY OBJECTS
def check2DarrayObjects(arrayContent):
	return check1DarrayObjects(make2Darray1Darray(arrayContent))
#CONTENT FORMAT
def change2DarrayContentFormat(array1Content,arrayMode):
	return make1Darray2Darray(change1DarrayContentFormat(make2Darray1Darray(array1Content),arrayMode),"",len(array1Content[0]))
#EXTRACT ARRAY COLUMN
def extract2DarrayColumn(array1Content,pos):
	array1Height = len(array1Content)
	array1Width = len(array1Content[0])
	array2Content = create1Darray(array1Height,"")
	if pos < array1Width:
		for yp in range(0, array1Height):
			array2Content[yp] = array1Content[yp][pos]
	return array2Content
#ADD NEW ROW
def addRow2Darray(array1Content,array3Content):
	array1Height = len(array1Content)
	array1Width = len(array1Content[0])
	array2Height = array1Height +1
	array2Width = array1Width
	array3Width = len(array3Content)
	if array3Width > array2Width:
		checka = array3Width
	else:
		checka = array2Width
	array2Content = create2Darray(array2Height,checka,"")
	for yp in range(0,array1Height):
		for xp in range(0,array1Width):
			pointa = str(array1Content[yp][xp])
			array2Content[yp][xp] = pointa
	yp = array1Height
	for xp in range(0,array3Width):
		array2Content[yp][xp] = str(array3Content[xp])
	return array2Content
#FLIP OBJECTS
def flip2DarrayObjects(array1Content):
	array1Height = len(array1Content)
	array1Width = len(array1Content[0])
	array2Height = array1Height
	array2Width = array1Width
	array2Content = create2Darray(array2Height,array2Width,"")
	ypb = array2Height
	for ypa in range(0,array1Height):
		ypb -=1
		for xp in range(0,array1Width):
			pointa = str(array1Content[ypa][xp])
			array2Content[ypb][xp] = pointa
	return array2Content
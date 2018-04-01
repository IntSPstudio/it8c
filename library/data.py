#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this library!
# Plugin: Data handling
#|==============================================================|#

#|COM|==========================================================|#
#MAKE INPUT TO ONLY LETTRS AND DIGITS
def cfc1219294(input,alt):
	return str(alt).join(i for i in input if i.isalnum())
#CHECK IF IT IS A NUMBER
def cfc318398(input):
    try:
        int(input)
        return 1
    except ValueError:
        return 0
#|1D ARRAY|=====================================================|#
#MAKE 1D ARRAY
def cad325305(arraySize,arrayContent):
	return [arrayContent for xp in range(arraySize)]
#MAKE 1D ARRAY TO 2D ARRAY
def cad1325478(array1Content,array2DefContent,array2Width):
	array1Width =  len(array1Content)
	array2Height =0
	xp =0
	for i in range(0, array1Width):
		xp +=1
		if xp >= array2Width:
			array2Height +=1
			xp =0
	array2Content = cbd325306(array2Height,array2Width,array2DefContent)
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
def cad1620472(arrayContent,separator):
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
def cad320542(arrayContent):
	arrayWidth = len(arrayContent)
	arrayOutput =0
	arrayCounter =0
	for i in range(0, arrayWidth):
		point = arrayContent[i]
		check = cfc318398(point)
		if check == 1:
			arrayCounter = arrayCounter +1
			arrayOutput = arrayOutput + int(point)
	if arrayCounter > 0:
		return arrayOutput / arrayCounter
	else:
		return 0
#CALCULATE SUM VALUE
def cad320479(arrayContent):
	arrayWidth = len(arrayContent)
	arrayOutput =0
	for i in range(0, arrayWidth):
		point = arrayContent[i]
		check = cfc318398(point)
		if check == 1:
			arrayOutput = arrayOutput + int(point)
	return arrayOutput
#CHECK MAX VALUE
def cad320776(arrayContent):
	arrayWidth = len(arrayContent)
	arrayOutput =0
	for i in range(0, arrayWidth):
		point = arrayContent[i]
		check = cfc318398(point)
		if check == 1:
			point = int(point)
			if point > arrayOutput:
				arrayOutput = point
	return arrayOutput
#CHECK 1D ARRAY OBJECTS
def cad319492(array1Content):
	array1Content = sorted(array1Content)
	array1Width = len(array1Content)
	pointa =""
	for i in range(0,2):
		if i == 1:
			checkHeight = ypb
			checkWidth =3
			checkContent = cbd325306(checkHeight,checkWidth,"")
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
def cad320737(arrayContent,arrayMode):
	arrayWidth = len(arrayContent)
	for yp in range(0, arrayWidth):
		pointa = str(arrayContent[yp])
		if arrayMode == 1:
			pointb = str.lower(pointa)
		elif arrayMode == 2:
			pointb = str.upper(pointa)
		elif arrayMode == 3:
			pointb = cfc1219294(pointa,"") 
		elif arrayMode == 4:
			check = cfc318398(pointa)
			if check == 1:
				pointb = int(pointa)
			else:
				pointb =0
		arrayContent[yp] = pointb
	return arrayContent
#FLIP OBJECTS
def cad619467(array1Content):
	array1Length = len(array1Content)
	array2Content = cad325305(array1Length,"")
	for ypa in range(0,array1Length):
		ypb = array1Length -ypa -1
		array2Content[ypa] = array1Content[ypb]
	return array2Content
#|2D ARRAY|=====================================================|#
#MAKE 2D ARRAY
def cbd325306(arrayHeight,arrayWidth,arrayContent):
	return [[arrayContent for xp in range(arrayWidth)] for yp in range(arrayHeight)]
#MAKE 2D ARRAY TO 1D ARRAY
def cbd1325477(array1Content):
	array1Height = len(array1Content)
	array1Width =  len(array1Content[0])
	array1Counter =0
	array2Width = array1Height * array1Width
	array2Content = cad325305(array2Width,"")
	for yp in range(0, array1Height):
		for xp in range(0, array1Width):
			array2Content[array1Counter] = array1Content[yp][xp]
			array1Counter +=1
	return array2Content
#PRINT 2D ARRAY
def cbd1620473(arrayContent,separator):
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
def cbd1920575(array1Content,separator,fill,contentMode):
	array1Height = len(array1Content)
	array1Width = len(array1Content[0])
	arrayRowSpWidth = cad325305(array1Width,"")
	array2Height = array1Height
	array2Width = array1Width
	array2Content = cbd325306(array2Height,array2Width,"")
	for xp in range(0,array1Width):
		contenta = cbd514472(array1Content,xp)
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
			checkc = cfc318398(pointa)
			if checkb > 0:
				pointb =""
				for _ in range(0, checkb):
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
	return cbd1620473(array2Content,separator)
#CALCULATE AVARAGE VALUE
def cbd320543(arrayContent):
	return cad320542(cbd1325477(arrayContent))
#CALCULATE SUM VALUE
def cbd320480(arrayContent):
	return cad320479(cbd1325477(arrayContent))
#CHECK MAX VALUE
def cbd320777(arrayContent):
	return cad320776(cbd1325477(arrayContent))
#CHECK 2D ARRAY OBJECTS
def cbd319493(arrayContent):
	return cad319492(cbd1325477(arrayContent))
#CONTENT FORMAT
def cbd320738(array1Content,arrayMode):
	return cad1325478(cad320737(cbd1325477(array1Content),arrayMode),"",len(array1Content[0]))
#EXTRACT ARRAY COLUMN
def cbd514472(array1Content,pos):
	array1Height = len(array1Content)
	array1Width = len(array1Content[0])
	array2Content = cad325305(array1Height,"")
	if pos < array1Width:
		for yp in range(0, array1Height):
			array2Content[yp] = array1Content[yp][pos]
	return array2Content
#ADD COLUMN TO ARRAY
def cdb114391(array1Content, array2Content):
	array1Height = len(array1Content)
	array1Width = len(array1Content[0])
	array2Length = len(array2Content)
	array3Height = array1Height
	array3Width = array1Width +1
	if array2Length > array1Height:
		array3Height = array2Length
	array3Content = cbd325306(array3Height, array3Width, "")
	for y in range(0, array1Height):
		for x in range(0, array1Width):
			array3Content[y][x] = array1Content[y][x]
	for i in range(0, array2Length):
		array3Content[i][array3Width -1] = array2Content[i]
	return array3Content
#ADD NEW ROW
def cbd125319(array1Content,array3Content):
	array1Height = len(array1Content)
	array1Width = len(array1Content[0])
	array2Height = array1Height +1
	array2Width = array1Width
	array3Width = len(array3Content)
	if array3Width > array2Width:
		checka = array3Width
	else:
		checka = array2Width
	array2Content = cbd325306(array2Height,checka,"")
	for yp in range(0,array1Height):
		for xp in range(0,array1Width):
			pointa = str(array1Content[yp][xp])
			array2Content[yp][xp] = pointa
	yp = array1Height
	for xp in range(0,array3Width):
		array2Content[yp][xp] = str(array3Content[xp])
	return array2Content
#FLIP OBJECTS
def cbd619468(array1Content):
	array1Height = len(array1Content)
	array1Width = len(array1Content[0])
	array2Height = array1Height
	array2Width = array1Width
	array2Content = cbd325306(array2Height,array2Width,"")
	ypb = array2Height
	for ypa in range(0,array1Height):
		ypb -=1
		for xp in range(0,array1Width):
			pointa = str(array1Content[ypa][xp])
			array2Content[ypb][xp] = pointa
	return array2Content
#REMOVE TITLE
def cbd75347(array1Content):
	array1Height = len(array1Content)
	array1Width = len(array1Content[0])
	array2Content = cbd325306(array1Height -1,array1Width,"")
	for y in range(1, array1Height):
		array2Content[y-1] = array1Content[y]
	return array2Content
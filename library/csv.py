#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this library!
# Plugin: CSV
#|==============================================================|#

#IMPORT
from it8c import data
#SETTINGS
fileSeparator =";"
fileStringSep ='"'
#READ FILE
def readFile(name):
	file = name
	file = open(file, "r")
	fileContent = file.read().splitlines()
	file.close()
	return fileContent
#WRITE FILE
def writeFile(array, ifilename, separator, strsep):
	if separator == "":
		separator = fileSeparator
	arrayMaxWidth =0
	arrayHeight = len(array)
	arrayLine =""
	fileName = ifilename
	f = open(fileName,"w")
	for yp in range(0, arrayHeight):
		arrayWidth = len(array[yp])
		for xp in range(0, arrayWidth):
			point = str(array[yp][xp])
			pointTypeCheck = data.checkIfItIsNumber(point)
			if pointTypeCheck == 0:
				if strsep == 1:
					point = fileStringSep + point + fileStringSep
				else:
					point = point
			if arrayLine !="":
				arrayLine = arrayLine + separator + point
			else:
				arrayLine = point
		if yp < arrayHeight -1:
			arrayLine = arrayLine +"\n"
		f.write(arrayLine)
		arrayLine =""
	f.close()
#ARRAY WIDTH (CSV STYLE)
def getArrayWidth(array, contentFileSep):
	if contentFileSep == "":
		contentFileSep = fileSeparator
	arrayMaxWidth =0
	arrayHeight = len(array)
	for yp in range(0, arrayHeight):
		arrayWidth = len(array[yp])
		pointWidth =0
		pointCheck =0
		sepaStrPointCheck =0
		for xp in range(0, arrayWidth):
			point = str(array[yp][xp])
			if point == fileStringSep:
				if sepaStrPointCheck !=0:
					sepaStrPointCheck =0
				else:
					sepaStrPointCheck =1
			if point == contentFileSep:
				if sepaStrPointCheck == 0:
					pointCheck =0
			else:
				if pointCheck == 0:
					pointWidth +=1
					pointCheck =1
		if pointWidth > arrayMaxWidth:
			arrayMaxWidth = pointWidth
	return arrayMaxWidth
#ARRAY SIZE
def getArrayHeightWidth(array):
	arrayHeight = len(array)
	arrayWidth = len(array[0])
	arraySize = str(arrayHeight) +"x"+ str(arrayWidth)
	return arraySize
#MAKE ARRAY
def makeContentArray(contentFileName, contentFileSep):
	contentFile = readFile(contentFileName)
	contentHeight = len(contentFile)
	if contentFileSep == "":
		contentFileSep = fileSeparator
	arrayHeight = len(contentFile)
	arrayWidth = getArrayWidth(contentFile, contentFileSep)
	arrayContent = [["" for xp in range(arrayWidth)] for yp in range(arrayHeight)]
	arrayYP =0
	for yp in range(0, contentHeight):
		contentWidth = len(contentFile[yp])
		contentCheck =0
		wcl =""
		arrayXP =-1
		sepaStrPointCheck =0
		for xp in range(0, contentWidth):
			point = str(contentFile[yp][xp])
			if point == fileStringSep:
				if sepaStrPointCheck !=0:
					sepaStrPointCheck =0
				else:
					sepaStrPointCheck =1
			if point == contentFileSep and sepaStrPointCheck == 0:
				wcl =""
				contentCheck =0
			else:
				if contentCheck == 0:
					arrayXP +=1
					contentCheck =1
				wcl = wcl + point
				arrayYP = yp
				arrayContent[arrayYP][arrayXP] = wcl
	mathRe1Height = len(arrayContent)
	mathRe1Width = len(arrayContent[0])
	mathRe1Content = [["" for xp in range(mathRe1Width)] for yp in range(mathRe1Height)]
	for ypa in range(0, mathRe1Height):
		for xpa in range(0, mathRe1Width):
			pointContent = arrayContent[ypa][xpa]
			pointWidth = len(pointContent)
			wcl =""
			for xpb in range(0, pointWidth):
				pointCheck = pointContent[xpb]
				if pointCheck != fileStringSep:
					wcl = wcl + pointCheck
			mathRe1Content[ypa][xpa] = wcl
	return mathRe1Content
#PRINT ARRAY
def printContentArraySimple(array):
	arrayMaxWidth =0
	arrayHeight = len(array)
	arrayPrintMap =""
	arraySeparatorV ="\n"
	arraySeparatorH = " "
	for yp in range(0, arrayHeight):
		arrayWidth = len(array[yp])
		for xp in range(0, arrayWidth):
			point = str(array[yp][xp])
			if point !="":
				if xp == 0:
					arrayPrintMap = arrayPrintMap + point
				else:
					arrayPrintMap = arrayPrintMap + arraySeparatorH + point
		if yp < arrayHeight -1:
			arrayPrintMap = arrayPrintMap + arraySeparatorV
	return arrayPrintMap
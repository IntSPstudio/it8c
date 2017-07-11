#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this library!
# Plugin: Copa
#|==============================================================|#

#IMPORT
from it8c import csv
from it8c import data
from it8c import file
#READ FILE
def readCopaFile(fileName,separator):
	array1Content = csv.makeContentArray(fileName,separator)
	array1Height = len(array1Content)
	array1Width =  len(array1Content[0])
	checka =0
	for zp in range(0,2):
		if zp == 1:
			checkd =0
			array2Height = checka
			array2Width =2
			array2Content = data.create2Darray(array2Height,array2Width,"")
		for yp in range(0,array1Height):
			checkb = array1Content[yp][0]
			checkc = checkb[0]
			if checkc != "#":
				if zp == 0:
					checka +=1
				if zp == 1:
					array2Content[checkd][0] = array1Content[yp][0]
					array2Content[checkd][1] = array1Content[yp][1]
					checkd +=1
	return array2Content
#WRITE FILE
def writeCopaFile(fileName,array1Content,separator):
	if separator =="":
		separator ="="
	array1Length = len(array1Content)
	array1Width = len(array1Content[0])
	if array1Width >= 2:
		array2Content = data.create1Darray(array1Length,"")
		for i in range(0,array1Length):
			pointa = str(array1Content[i][0])
			pointb = str(array1Content[i][1])
			if pointa == "comment":
				pointa ="#"
				pointc = pointa + pointb
			else:
				pointc = pointa + separator + pointb
			array2Content[i] = pointc
		file.mainWriteListTextFile(array2Content,fileName)
#MODIFY FILE
def modCopaFile(fileName,parKey,parValue,copaMode,separator):
	if separator =="":
		separator ="="
	if copaMode == 0:
		if file.mainTextFileExists(fileName) == 1:
			pointc = readCopaFile(fileName,separator)
			pointaLength = len(pointc)
			success =0
			for i in range(0,pointaLength):
				pointd = pointc[i][0]
				if pointd == parKey:
					success =1
					pointc[i][1] = parValue
			if success == 0:
				pointd = data.create1Darray(2,"")
				pointd[0] = parKey
				pointd[1] = parValue
				pointe = data.addRow2Darray(pointc,pointd)
				pointc = pointe
			writeCopaFile(fileName,pointc,separator)
		else:
			pointc = data.create2Darray(1,2,"")
			pointc[0][0] = parKey
			pointc[0][1] = parValue
			writeCopaFile(fileName,pointc,separator)
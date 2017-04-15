#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this library!
# Plugin: Coba
#|==============================================================|#

#IMPORT
from it8c import csv
from it8c import data
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
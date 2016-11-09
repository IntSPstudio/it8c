#|==============================================================|#
# Made by IntSPstudio
# Main package for all of IT8c libraries
# Thank you for using this library!
# Version: 0.0.4.20161109
# ID: 980001001
#|==============================================================|#
#HELP AND INFORMATION
from it8c import help
#VISUAL
from it8c import visual
#FILE HANDLING
from it8c import file
#DATA HANDLING
from it8c import data
#CSV
from it8c import csv
#ENCRYPTION
from it8c import encryption
#|COM|==========================================================|#
#HAI VERSION
def version():
	return "0.0.4.20161109"
#HAI FEATURES
def haiFeatures():
	return help.features()
#VISUAL TERMINAL WHAT
def vslTerminalDunno(stpoint):
	return visual.comTerminalDunno(stpoint)
#VISUAL TERMINAL BACKGROUND LINE
def vslTerminalLine(width,mark):
	return visual.comTerminalBackgroundLine(width,mark)
#|FILE|=========================================================|#
#READ TEXT FILE
def fileReadText(filename):
	return file.mainReadTextFile(filename)
#PRINT TEXT FILE
def filePrintText(filename):
	return file.mainPrintTextFile(filename)
#|DATA|=========================================================|#
#CHECK IF IT IS NUMBER
def checkIfItIsNumber(input):
	return data.checkIfItIsNumber(input)
#CREATE LIST (1D ARRAY)
def dataCreateList(filearraysize,filecontent):
	return data.create1Darray(filearraysize,filecontent)
#PRINT LIST (1D ARRAY)
def dataPrintList(filearray,fileseparator):
	return data.print1DarrayContent(filearray,fileseparator)
#CALCULATE AVARAGE VALUE LIST (1D ARRAY)
def dataCalcAvgList(filearray):
	return data.calcAvg1DarrayContent(filearray)
#CALCULATE SUM VALUE LIST (1D ARRAY)
def dataCalcSumList(filearray):
	return data.calcSum1DarrayContent(filearray)
#CREATE ARRAY (2D ARRAY)
def dataCreateArray(filearrayheight,filearraywidth,filearraycontent):
	return data.create2Darray(filearrayheight,filearraywidth,filearraycontent)
#PRINT ARRAY (2D ARRAY)
def dataPrintArray(filearray,fileseparator):
	return data.print2DarrayContent(filearray,fileseparator)
#|CSV|==========================================================|#
#CSV READ FILE
def csvReadFile(filename):
	return csv.makeContentArray(filename)
#CSV WRITE FILE
def csvWriteFile(filearray, filename):
	csv.writeFile(filearray, filename)
#CSV ARRAY SIZE
def csvArraySize(filearray):
	return csv.getArrayHeightWidth(filearray)
#CSV SIMPLE ARRAY PRINT
def csvSimplePrint(filearray):
	return csv.printContentArraySimple(filearray)
#|ENCRYPTION|===================================================|#
#SHA1 ENCRYPTION UTF8
def sha1(filestring):
	return encryption.sha1Encryption(filestring)
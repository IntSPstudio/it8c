#|==============================================================|#
# Made by IntSPstudio
# Data handling library
# Thank you for using this library!
# Version: 0.2.19.20172806
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
#COPA
from it8c import copa
#CSV
from it8c import csv
#ENCRYPTION
from it8c import encryption
#|COM|==========================================================|#
#HAI VERSION
def version():
	return "0.2.19.20172806"
#HAI FEATURES
def haiFeatures():
	return help.features()
#HAI ABOUT
def haiAbout():
	return help.about()
#VISUAL TERMINAL LOGO
def vslTerminalLogo(stpoint):
	return visual.comTerminalLogo(stpoint)
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
#READ 1L TEXT FILE
def fileRead1LText(filename):
	return file.mainRead1LTextFile(filename)
#WRITE LIST TEXT FILE
def fileWriteTextList(filelist,filename):
	return file.mainWriteListTextFile(filelist,filename)
#WRITE 1L TEXT FILE
def fileWrite1LText(fileline,filename):
	return file.mainWrite1LTextFile(fileline,filename)
#FILE EXIST
def fileTextExists(filename):
	return file.mainTextFileExists(filename)
#PRINT TEXT FILE
def filePrintText(filename):
	return file.mainPrintTextFile(filename)
#|DATA COM|=====================================================|#
#LETTERS AND DIGITS
def lettersdigits(input,alt):
	return data.lettersdigits(input,alt)
#CHECK IF IT IS A NUMBER
def checkIfItIsNumber(input):
	return data.checkIfItIsNumber(input)
#|DATA 1D|======================================================|#
#CREATE LIST
def dataCreateList(filearraysize,filecontent):
	return data.create1Darray(filearraysize,filecontent)
#PRINT LIST
def dataPrintList(filearray,fileseparator):
	return data.print1DarrayContent(filearray,fileseparator)
#CALCULATE AVARAGE VALUE
def dataCalcAvgList(filearray):
	return data.calcAvg1DarrayContent(filearray)
#CALCULATE SUM VALUE 
def dataCalcSumList(filearray):
	return data.calcSum1DarrayContent(filearray)
#CHECK MAX VALUE
def dataCheckMaxValueList(filearray):
	return data.checkMaxValue1DarrayContent(filearray)
#CHECK OBJECTS
def dataCheckListObjects(filearray):
	return data.check1DarrayObjects(filearray)
#CONTENT FORMAT
def dataChangeListContentFormat(filearray,arraymode):
	return data.change1DarrayContentFormat(filearray,arraymode)
def dataFlipListObjects(filearray):
	return data.flip1DarrayObjects(filearray)
#|DATA 2D|======================================================|#
#CREATE ARRAY
def dataCreateArray(filearrayheight,filearraywidth,filecontent):
	return data.create2Darray(filearrayheight,filearraywidth,filecontent)
#PRINT ARRAY
def dataPrintArray(filearray,contentseparator):
	return data.print2DarrayContent(filearray,contentseparator)
#SMART PRINT ARRAY
def dataSmrPrintArray(filearray,contentseparator,fillcontent,contentmode):
	return data.sprint2DarrayContent(filearray,contentseparator,fillcontent,contentmode)
#MAKE 2D ARRAY TO 1D ARRAY
def dataMakeArrayToList(filearray):
	return data.make2Darray1Darray(filearray)
#CALCULATE AVARAGE VALUE 
def dataCalcAvgArray(filearray):
	return data.calcAvg2DarrayContent(filearray)
#CALCULATE SUM VALUE 
def dataCalcSumArray(filearray):
	return data.calcSum2DarrayContent(filearray)
#CHECK MAX VALUE
def dataCheckMaxValueArray(filearray):
	return data.checkMaxValue2DarrayContent(filearray)
#CHECK OBJECTS
def dataCheckArrayObjects(filearray):
	return data.check2DarrayObjects(filearray)
#CONTENT FORMAT
def dataChangeArrayContentFormat(filearray,arraymode):
	return data.change2DarrayContentFormat(filearray,arraymode)
#EXTRACT ARRAY COLUMN
def dataExtractArrayColumn(filearray,pos):
	return data.extract2DarrayColumn(filearray,pos)
#ADD NEW ROW (ROW = 1D ARRAY)
def dataAddArrayRow(filearray,addedrow):
	return data.addRow2Darray(filearray,addedrow)
#FLIP OBJECTS
def dataFlipArrayObjects(filearray):
	return data.flip2DarrayObjects(filearray)
#|COPA|=========================================================|#
#READ FILE
def copaRead(filename,fileseparator):
	return copa.readCopaFile(filename,fileseparator)
#|CSV|==========================================================|#
#CSV READ FILE
def csvReadFile(filename,fileseparator):
	return csv.makeContentArray(filename,fileseparator)
#CSV WRITE FILE
def csvWriteFile(filearray,filename,fileseparator,strseparator):
	csv.writeFile(filearray,filename,fileseparator,strseparator)
#CSV ARRAY SIZE
def csvArraySize(filearray):
	return csv.getArrayHeightWidth(filearray)
#CSV SIMPLE ARRAY PRINT
def csvSimplePrint(filearray):
	return csv.printContentArraySimple(filearray)
#|ENCRYPTION|===================================================|#
#SHA1
def encryptSha1(filestring):
	return encryption.eptnSha1(filestring)
#SHA256
def encryptSha256(filestring):
	return encryption.eptnSha256(filestring)
#MD5
def encryptMd5(filestring):
	return encryption.eptnMd5(filestring)
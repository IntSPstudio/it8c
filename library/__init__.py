#|==============================================================|#
# Made by IntSPstudio
# Data handling library
# Thank you for using this library!
# Version: 0.3.23.20180610
# ID: 980001001
#|==============================================================|#
from it8c import help
from it8c import visual
from it8c import file
from it8c import data
from it8c import copa
from it8c import encryption
#|COM|==========================================================|#
#HAI VERSION
def version():
	return "0.3.23.20180610"
#HAI FEATURES
def haiFeatures():
	help.ctb619230()
#HAI ABOUT
def haiAbout():
	help.ctb12090()
#VISUAL TERMINAL LOGO
def vslTerminalLogo(stpoint):
	return visual.cfc315323(stpoint)
#VISUAL TERMINAL WHAT
def vslTerminalDunno(stpoint):
	return visual.cfc315313(stpoint)
#VISUAL TERMINAL BACKGROUND LINE
def vslTerminalLine(width,mark):
	return visual.cfc35650(width,mark)
#|FILE|=========================================================|#
#READ TEXT FILE
def fileReadText(filename):
	return file.crf135402(filename)
#READ 1L TEXT FILE
def fileRead1LText(filename):
	return file.crf135433(filename)
#WRITE LIST TEXT FILE
def fileWriteTextList(filecontent,filename):
	return file.cwf135577(filecontent,filename)
#WRITE 1L TEXT FILE
def fileWrite1LText(filecontent,filename):
	return file.cwf135518(filecontent,filename)
#FILE EXIST
def fileTextExists(filename):
	return file.cfc1319459(filename)
#PRINT TEXT FILE
def filePrintText(filename):
	return file.cfc135410(filename)
#|CSV|==========================================================|#
#CSV READ FILE
def csvReadFile(filename,fileseparator):
	return file.crf1325420(filename,fileseparator)
#CSV WRITE FILE
def csvWriteFile(filearray,filename,fileseparator,strseparator):
	file.cwf235212(filearray,filename,fileseparator,strseparator)
#|DATA COM|=====================================================|#
#LETTERS AND DIGITS
def lettersdigits(input,alt):
	return data.cfc1219294(input,alt)
#CHECK IF IT IS A NUMBER
def checkIfItIsNumber(input):
	return data.cfc318398(input)
#|DATA 1D|======================================================|#
#CREATE LIST
def dataCreateList(filearraysize,filecontent):
	return data.cad325305(filearraysize,filecontent)
#PRINT LIST
def dataPrintList(filearray,fileseparator):
	return data.cad1620472(filearray,fileseparator)
#CALCULATE AVARAGE VALUE
def dataCalcAvgList(filearray):
	return data.cad320542(filearray)
#CALCULATE SUM VALUE 
def dataCalcSumList(filearray):
	return data.cad320479(filearray)
#CHECK MAX VALUE
def dataCheckMaxValueList(filearray):
	return data.cad320776(filearray)
#CHECK OBJECTS
def dataCheckListObjects(filearray):
	return data.cad319492(filearray)
#CONTENT FORMAT
def dataChangeListContentFormat(filearray,arraymode):
	return data.cad320737(filearray,arraymode)
#FLIP LIST
def dataFlipListObjects(filearray):
	return data.cad619467(filearray)
#|DATA 2D|======================================================|#
#CREATE ARRAY
def dataCreateArray(arrayheight,arraywidth,filecontent):
	return data.cbd325306(arrayheight,arraywidth,filecontent)
#PRINT ARRAY
def dataPrintArray(filearray,contentseparator):
	return data.cbd1620473(filearray,contentseparator)
#SMART PRINT ARRAY
def dataSmrPrintArray(filearray,contentseparator,fillcontent,contentmode):
	return data.cbd1920575(filearray,contentseparator,fillcontent,contentmode)
#MAKE 2D ARRAY TO 1D ARRAY
def dataMakeArrayToList(filearray):
	return data.cbd1325477(filearray)
#CALCULATE AVARAGE VALUE 
def dataCalcAvgArray(filearray):
	return data.cbd320543(filearray)
#CALCULATE SUM VALUE 
def dataCalcSumArray(filearray):
	return data.cbd320480(filearray)
#CHECK MAX VALUE
def dataCheckMaxValueArray(filearray):
	return data.cbd320777(filearray)
#CHECK OBJECTS
def dataCheckArrayObjects(filearray):
	return data.cbd319493(filearray)
#CONTENT FORMAT
def dataChangeArrayContentFormat(filearray,arraymode):
	return data.cbd320738(filearray,arraymode)
#EXTRACT ARRAY COLUMN
def dataExtractArrayColumn(filearray,pos):
	return data.cbd514472(filearray,pos)
#ADD COLUMN TO ARRAY
def dataAddArrayColumn(filearray,addedrow):
	return data.cdb114391(filearray,addedrow)
#ADD NEW ROW (ROW = 1D ARRAY)
def dataAddArrayRow(filearray,addedrow):
	return data.cbd125319(filearray,addedrow)
#FLIP OBJECTS
def dataFlipArrayObjects(filearray):
	return data.cbd619468(filearray)
#REMOVE TITLE
def dataExtractTitle(filearray):
	return data.cbd75347(filearray)
#|COPA|=========================================================|#
#READ FILE
def copaRead(filename,fileseparator):
	return copa.crf185319(filename,fileseparator)
#WRITE FILE
def copaWrite(filename,filearray,fileseparator):
	copa.cwf235269(filename,filearray,fileseparator)
#MODIFY FILE
def copaMod(filename,filekey,filevalue,filemode,fileseparator):
	copa.cpf135315(filename,filekey,filevalue,filemode,fileseparator)
#|ENCRYPTION|===================================================|#
#SHA1
def encryptSha1(input):
	return encryption.cpd51249(input)
#SHA256
def encryptSha256(input):
	return encryption.cpd56292(input)
#MD5
def encryptMd5(input):
	return encryption.cpd55232(input)
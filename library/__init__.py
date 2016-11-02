#|==============================================================|#
# Made by IntSPstudio
# Main package for all of IT8c libraries
# Thank you for using this library!
# Version: 0.0.2.20161103
# ID: 980001001
#|==============================================================|#

#HAI
from it8c import help
#VISUAL
from it8c import visual
#CSV PLUGIN
from it8c import csv
#ENCRYPTION
from it8c import encryption

#HAI VERSION
def version():
	return "0.0.2.20161103"
#HAI FEATURES
def haiFeatures():
	return help.features()
#VISUAL TERMINAL WHAT
def vslTerminalDunno(stpoint):
	return visual.comTerminalDunno(stpoint)
#VISUAL TERMINAL BACKGROUND LINE
def vslTerminalLine(width,mark):
	return visual.comTerminalBackgroundLine(width,mark)
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
	return csv.printContentArraySimple(filearray," ")
#CSV COMPCUS ARRAY PRINT
def csvCompcusPrint(filearray,filecompcus):
	return csv.printContentArraySimple(filearray,filecompcus)
#SHA1 ENCRYPTION UTF8
def sha1(filestring):
	return encryption.sha1Encryption(filestring)
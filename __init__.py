#|==============================================================|#
# Made by IntSPstudio
# Main package for all of IT8c libraries
# Thank you for using this library!
# Version: 0.0.1.20161026
# ID: 980001001
#|==============================================================|#

#CSV PLUGIN
from it8c import csv
#ENCRYPTION
from it8c import encryption

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
	
#SHA1 ENCRYPTION UTF8
def sha1(filestring):
	return encryption.sha1Encryption(filestring)
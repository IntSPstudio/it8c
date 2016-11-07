#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this library!
# Plugin: File handling
#|==============================================================|#

#READ TEXT FILE
def mainReadTextFile(name):
	file = name
	file = open(file, "r")
	fileContent = file.read().splitlines()
	file.close()
	return fileContent
#PRINT TEXT FILE
def mainPrintTextFile(name):
	file = name
	file = open(file, "r")
	fileContent = file.read()
	file.close()
	return fileContent
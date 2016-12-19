#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this library!
# Plugin: File handling
#|==============================================================|#

#READ TEXT FILE
def mainReadTextFile(fileName):
	file = open(fileName, "r")
	fileContent = file.read().splitlines()
	file.close()
	return fileContent
#CHECK FILE
def mainTextFileExists(fileName):
	try:
		with open(fileName) as file:
			return 1
	except IOError as e:
		return 0
#PRINT TEXT FILE
def mainPrintTextFile(fileName):
	file = open(fileName, "r")
	fileContent = file.read()
	file.close()
	return fileContent
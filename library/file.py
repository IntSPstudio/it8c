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
#READ 1L TEXT FILE
def mainRead1LTextFile(fileName):
	file = open(fileName, "r")
	fileContent = file.read()
	file.close()
	return fileContent
#WRITE LIST TEXT FILE
def mainWriteListTextFile(arrayContent, fileName):
	arrayHeight = len(arrayContent)
	f = open(fileName,"w")
	for yp in range(0, arrayHeight):
		arrayLine = arrayContent[yp]
		if yp < arrayHeight -1:
			arrayLine = arrayLine +"\n"
		f.write(arrayLine)
	f.close()
#WRITE 1L TEXT FILE
def mainWrite1LTextFile(contentLine, fileName):
	f = open(fileName,"w")
	f.write(contentLine)
	f.close()
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
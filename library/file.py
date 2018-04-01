#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this library!
# Plugin: File handling
#|==============================================================|#

#READ TEXT FILE
def crf135402(fileName):
	file = open(fileName, "r")
	fileContent = file.read().splitlines()
	file.close()
	return fileContent
#READ 1L TEXT FILE
def crf135433(fileName):
	file = open(fileName, "r")
	fileContent = file.read()
	file.close()
	return fileContent
#WRITE LIST TEXT FILE
def cwf135577(arrayContent, fileName):
	arrayHeight = len(arrayContent)
	f = open(fileName,"w")
	for yp in range(0, arrayHeight):
		arrayLine = arrayContent[yp]
		if yp < arrayHeight -1:
			arrayLine = arrayLine +"\n"
		f.write(arrayLine)
	f.close()
#WRITE 1L TEXT FILE
def cwf135518(contentLine, fileName):
	f = open(fileName,"w")
	f.write(contentLine)
	f.close()
#CHECK FILE
def cfc1319459(fileName):
	try:
		with open(fileName) as _:
			return 1
	except IOError as _:
		return 0
#PRINT TEXT FILE
def cfc135410(fileName):
	file = open(fileName, "r")
	fileContent = file.read()
	file.close()
	return fileContent
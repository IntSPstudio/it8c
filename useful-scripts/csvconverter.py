#|==============================================================|#
# Made by IntSPstudio
# Useful scripts to IT8c library
# Thank you for using this software!
# Version: 0.0.1.20170412
# ID: 980001004
#
# Twitter: @IntSPstudio
#|==============================================================|#

#IMPORT
import it8c
#START
if __name__ == "__main__":
	print(it8c.vslTerminalLine(0,""))
	checka = str(input("Filename: "))
	if it8c.fileTextExists(checka) == 1:
		checkb = str(input("Text separator: "))
		if checkb !="":
			checkc = str(input("Save file as: "))
			if checkc !="":
				checkd = str(input("New separator: ") or ";")
				if checkd !="":
					contentArray = it8c.csvReadFile(checka,checkb)
					it8c.csvWriteFile(contentArray,checkc,checkd,0)
					contentArray =0
				else:
					print("Invalid separator")
			else:
				print("Invalid filename")
		else:
			print("Invalid separator")
	else:
		print("File doesn't exists")
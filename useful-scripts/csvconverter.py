#|==============================================================|#
# Made by IntSPstudio
# Useful scripts to IT8c library
# Thank you for using this software!
# Version: 0.0.2.20250816
# ID: 980001004
#|==============================================================|#

#IMPORT
import it8c
#START
if __name__ == "__main__":
	print(it8c.vsl_tui_logo(1))
	print(it8c.vsl_tui_line(0,""))
	checka = str(input("Filename: "))
	if it8c.file_exists(checka) == 1:
		checkb = str(input("Text separator: "))
		if checkb !="":
			checkc = str(input("Save file as: "))
			if checkc !="":
				checkd = str(input("New separator: ") or ";")
				if checkd !="":
					content = it8c.file_read_csv(checka,checkb)
					it8c.file_write_csv(content,checkc,checkd,0)
					content =0
				else:
					print("Invalid separator")
			else:
				print("Invalid filename")
		else:
			print("Invalid separator")
	else:
		print("File doesn't exists")
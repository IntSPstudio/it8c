#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this library!
# Plugin: File handling
#|==============================================================|#

from it8c import data
import csv

#|BASIC|========================================================|#
#READ TEXT FILE
def crf135402(file_name):
	file = open(file_name, "r")
	file_content = file.read().splitlines()
	file.close()
	return file_content
#READ 1L TEXT FILE
def crf135433(file_name):
	file = open(file_name, "r")
	file_content = file.read()
	file.close()
	return file_content
#WRITE LIST TEXT FILE
def cwf135577(array_content, file_name):
	array_height = len(array_content)
	f = open(file_name,"w")
	for yp in range(0, array_height):
		array_line = array_content[yp]
		if yp < array_height -1:
			array_line = array_line +"\n"
		f.write(array_line)
	f.close()
#WRITE 1L TEXT FILE
def cwf135518(file_content, file_name):
	f = open(file_name,"w")
	f.write(file_content)
	f.close()
#CHECK FILE
def cfc1319459(file_name):
	try:
		with open(file_name) as _:
			return 1
	except IOError as _:
		return 0
#PRINT TEXT FILE
def cfc135410(file_name):
	file = open(file_name, "r")
	file_content = file.read()
	file.close()
	return file_content
#|CSV|==========================================================|#
#SETTINGS
file_separator =";"
string_separator ='"'
#READ CSV FILE
def crf1325420(contentfile_name, content_filesep):
	if content_filesep == "":
		content_filesep = file_separator
	file_og = open(contentfile_name, "rt")
	reader = csv.reader(file_og, delimiter = content_filesep)
	file_rlt = []
	for row in reader:
			file_rlt.append(row)
	file_og.close()
	return file_rlt
#WRITE CSV FILE
def cwf235212(array, ifile_name, separator, strsep):
	if separator == "":
		separator = file_separator
	array_height = len(array)
	array_line =""
	file_name = ifile_name
	f = open(file_name,"w")
	for yp in range(0, array_height):
		arrayWidth = len(array[yp])
		for xp in range(0, arrayWidth):
			point = str(array[yp][xp])
			point_check = data.cfc318398(point)
			if point_check == 0:
				if strsep == 1:
					point = string_separator + point + string_separator
				else:
					point = point
			if array_line !="":
				array_line = array_line + separator + point
			else:
				array_line = point
		if yp < array_height -1:
			array_line = array_line +"\n"
		f.write(array_line)
		array_line =""
	f.close()
#|COPA|=========================================================|#
#READ FILE
def crf185319(file_name,separator):
	array1_content = crf1325420(file_name,separator)
	array1_height = len(array1_content)
	checka =0
	for zp in range(0,2):
		if zp == 1:
			checkd =0
			array2_height = checka
			array2_width =2
			array2_content = data.cbd325306(array2_height,array2_width,"")
		for yp in range(0,array1_height):
			checkb = array1_content[yp][0]
			checkc = checkb[0]
			if checkc != "#":
				if zp == 0:
					checka +=1
				if zp == 1:
					array2_content[checkd][0] = array1_content[yp][0]
					array2_content[checkd][1] = array1_content[yp][1]
					checkd +=1
	return array2_content
#WRITE FILE
def cwf235269(file_name,array1_content,separator):
	if separator =="":
		separator ="="
	array1Length = len(array1_content)
	array1Width = len(array1_content[0])
	if array1Width >= 2:
		array2_content = data.cad325305(array1Length,"")
		for i in range(0,array1Length):
			pointa = str(array1_content[i][0])
			pointb = str(array1_content[i][1])
			if pointa == "comment":
				pointa ="#"
				pointc = pointa + pointb
			else:
				pointc = pointa + separator + pointb
			array2_content[i] = pointc
		cwf135577(array2_content,file_name)
#MODIFY FILE
def cpf135315(file_name,file_key,file_value,file_mode,separator):
	if separator =="":
		separator ="="
	if file_mode == 0:
		if fc1319459(file_name) == 1:
			pointc = crf185319(file_name,separator)
			pointa_length = len(pointc)
			success =0
			for i in range(0,pointa_length):
				pointd = pointc[i][0]
				if pointd == file_key:
					success =1
					pointc[i][1] = file_value
			if success == 0:
				pointd = data.cad325305(2,"")
				pointd[0] = file_key
				pointd[1] = file_value
				pointe = data.cbd125319(pointc,pointd)
				pointc = pointe
			cwf235269(file_name,pointc,separator)
		else:
			pointc = data.cbd325306(1,2,"")
			pointc[0][0] = file_key
			pointc[0][1] = file_value
			cwf235269(file_name,pointc,separator)

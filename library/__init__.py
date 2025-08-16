#|==============================================================|#
# Made by IntSPstudio
# Data handling library
# Thank you for using this library!
# Version: 0.5.1.20250816
# ID: 980001001
#|==============================================================|#
from it8c import help
from it8c import visual
from it8c import file
from it8c import data
from it8c import encryption
#|COM|==========================================================|#
#HAI VERSION
def version():
	return "0.5.1.20250816"
#HAI FEATURES
def hai_features():
	help.ctb619230()
#HAI ABOUT
def hai_about():
	help.ctb12090()
#VISUAL TERMINAL LOGO
def vsl_tui_logo(stpoint):
	return visual.cfc315323(stpoint)
#VISUAL TERMINAL WHAT
def vsl_tui_dunno(stpoint):
	return visual.cfc315313(stpoint)
#VISUAL TERMINAL BACKGROUND LINE
def vsl_tui_line(width,mark):
	return visual.cfc35650(width,mark)
#|FILE|=========================================================|#
#READ TEXT FILE
def file_read_text(filename):
	return file.crf135402(filename)
#READ 1L TEXT FILE
def file_read_line(filename):
	return file.crf135433(filename)
#WRITE LIST TEXT FILE
def file_write_text(filecontent,filename):
	return file.cwf135577(filecontent,filename)
#WRITE 1L TEXT FILE
def file_write_line(filecontent,filename):
	return file.cwf135518(filecontent,filename)
#FILE EXIST
def file_exists(filename):
	return file.cfc1319459(filename)
#FILE MODIFY
#DEF file_mod_textfile(content,options,filename)
#PRINT TEXT FILE
def file_print_text(filename):
	return file.cfc135410(filename)
#|CSV|==========================================================|#
#CSV READ FILE
def file_read_csv(filename,fileseparator):
	return file.crf1325420(filename,fileseparator)
#CSV WRITE FILE
def file_write_csv(filearray,filename,fileseparator,strseparator):
	file.cwf235212(filearray,filename,fileseparator,strseparator)
#|DATA COM|=====================================================|#
#LETTERS AND DIGITS
def lettersdigits(input,alt):
	return data.cfc1219294(input,alt)
#CHECK IF IT IS A NUMBER
def isitnumber(input):
	return data.cfc318398(input)
#|DATA 1D|======================================================|#
#CREATE LIST
def list_create(filearraysize,filecontent):
	return data.cad325305(filearraysize,filecontent)
#PRINT LIST
def list_print(filearray,fileseparator):
	return data.cad1620472(filearray,fileseparator)
#CALCULATE AVARAGE VALUE
def list_calc_avg(filearray):
	return data.cad320542(filearray)
#CALCULATE SUM VALUE
def list_calc_sum(filearray):
	return data.cad320479(filearray)
#CHECK MAX VALUE
def list_check_max_value(filearray):
	return data.cad320776(filearray)
#CHECK OBJECTS
def list_check_objects(filearray):
	return data.cad319492(filearray)
#CONTENT FORMAT
def list_format(filearray,arraymode):
	return data.cad320737(filearray,arraymode)
#FLIP LIST
def list_flip(filearray):
	return data.cad619467(filearray)
#|DATA 2D|======================================================|#
#CREATE ARRAY
def array_create(arrayheight,arraywidth,filecontent):
	return data.cbd325306(arrayheight,arraywidth,filecontent)
#PRINT ARRAY
def array_print(filearray,contentseparator):
	return data.cbd1620473(filearray,contentseparator)
#SMART PRINT ARRAY
def array_sprint(filearray,contentseparator,fillcontent,contentmode):
	return data.cbd1920575(filearray,contentseparator,fillcontent,contentmode)
#MAKE 2D ARRAY TO 1D ARRAY
def array_convert_tolist(filearray):
	return data.cbd1325477(filearray)
#CALCULATE AVARAGE VALUE 
def array_calc_avg(filearray):
	return data.cbd320543(filearray)
#CALCULATE SUM VALUE
def array_calc_sum(filearray):
	return data.cbd320480(filearray)
#CHECK MAX VALUE
def array_check_maxvalue(filearray):
	return data.cbd320777(filearray)
#CHECK OBJECTS
def array_check_objects(filearray):
	return data.cbd319493(filearray)
#CONTENT FORMAT
def array_convert_format(filearray,arraymode):
	return data.cbd320738(filearray,arraymode)
#EXTRACT ARRAY COLUMN
def array_extract_column(filearray,pos):
	return data.cbd514472(filearray,pos)
#ADD COLUMN TO ARRAY
def array_add_column(filearray,addedrow):
	return data.cdb114391(filearray,addedrow)
#ADD NEW ROW (ROW = 1D ARRAY)
def array_add_row(filearray,addedrow):
	return data.cbd125319(filearray,addedrow)
#FLIP OBJECTS
def array_flip_objects(filearray):
	return data.cbd619468(filearray)
#REMOVE TITLE
def array_extract_title(filearray):
	return data.cbd75347(filearray)
#|COPA|=========================================================|#
#READ COPA FILE
def file_read_copa(filename,fileseparator):
	return file.crf185319(filename,fileseparator)
#WRITE COPA FILE
def file_write_copa(filename,filearray,fileseparator):
	file.cwf235269(filename,filearray,fileseparator)
#MODIFY COPA FILE
def file_mod_copa(filename,filekey,filevalue,filemode,fileseparator):
	file.cpf135315(filename,filekey,filevalue,filemode,fileseparator)
#|ENCRYPTION|===================================================|#
#SHA1
def encrypt_sha1(input):
	return encryption.cpd51249(input)
#SHA256
def encrypt_sha256(input):
	return encryption.cpd56292(input)
#MD5
def encrypt_md5(input):
	return encryption.cpd55232(input)
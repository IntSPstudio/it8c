#|==============================================================|#
# Made by IntSPstudio
# Useful scripts to IT8c library
# Thank you for using this software!
# Version: 0.0.6.20250816
# ID: 980001003
#|==============================================================|#

#IMPORT 
import it8c
import os
import datetime
#OPERATING SYSTEM SETTINGS
# 1 = WINDOWS
# 2 = LINUX
sys_os =1
#BACKGROUND
tui_text_line =  it8c.vsl_tui_line(0,"")
tui_text_logo = it8c.vsl_tui_logo(1)
#DICTIONARY
tui_text_start_line1 ="]"
tui_text_start_line2 ="==" + tui_text_start_line1
tui_text_dict_select = tui_text_start_line2 +" Select the number: "
tui_text_dict_enter = tui_text_start_line2 +" Press enter to return"
#SETTINGS
library_version = it8c.version()
tui_text_dict_title = "IT8c V:"+ library_version +":"
sys_page =""
continuity =1
sys_page_features ="1"
sys_page_about ="2"
sys_page_test ="3"
sys_page_exit1 ="4"
sys_page_exit2 ="exit"
if sys_os == 1:
	sys_cmd_clear ="cls"
elif sys_os == 2:
	sys_cmd_clear ="clear"
else:
	sys_cmd_clear =""
#ASK TIME AND DATE
def sys_print_datetime(mode):
	#DATE
	sys_date_ref = datetime.datetime.now()
	sys_date_year = sys_date_ref.year
	sys_date_month = sys_date_ref.month
	sys_date_day = sys_date_ref.day
	sys_date_hour = sys_date_ref.hour
	sys_date_minute = sys_date_ref.minute
	sys_date_second = sys_date_ref.second
	if mode == 0:
		pointa = "{:04d}{:02d}{:02}{:02}{:02}{:02}".format(sys_date_year,sys_date_month,sys_date_day,sys_date_hour,sys_date_minute,sys_date_second)
	elif mode == 1:
		pointa = "{:04d}-{:02d}.{:02} {:02}:{:02}:{:02}".format(sys_date_year,sys_date_month,sys_date_day,sys_date_hour,sys_date_minute,sys_date_second)
	return pointa
#MAIN LOOP
if __name__ == "__main__":
	while continuity == 1:
		#START
		tui_text_dict_title = str(sys_print_datetime(1)) +" | IT8c V:"+ library_version +":"
		#FEATURES
		if sys_page == sys_page_features:
			#TA
			os.system(sys_cmd_clear)
			#TB
			print(tui_text_logo)
			print(tui_text_line)
			print(tui_text_start_line2, tui_text_dict_title, "Features")
			print(it8c.hai_features())
			#TC
			sys_input =input(tui_text_dict_enter)
			sys_page =0
		#ABOUT
		elif sys_page == sys_page_about:
			#TA
			os.system(sys_cmd_clear)
			#TB
			print(tui_text_logo)
			print(tui_text_line)
			print(tui_text_start_line2, tui_text_dict_title, "About")
			print(it8c.hai_about())
			#TC
			sys_input =input(tui_text_dict_enter)
			sys_page =0
		#EXIT
		elif sys_page == sys_page_exit1:
			#TA
			continuity =0
			os.system(sys_cmd_clear)
			#TB
			print(tui_text_logo)
		elif sys_page == sys_page_exit2:
			#TA
			continuity =0
			os.system(sys_cmd_clear)
			#TB
			print(tui_text_logo)
		#MENU
		else:
			#TA
			os.system(sys_cmd_clear)
			#TB
			print(tui_text_logo)
			print(tui_text_line)
			print(tui_text_start_line2, tui_text_dict_title)
			print(" 1"+ tui_text_start_line1, "Features")
			print(" 2"+ tui_text_start_line1, "About")
			print(" 4"+ tui_text_start_line1, "Exit")
			#TC
			sys_input =input(tui_text_dict_select)
			sys_page = str(sys_input)

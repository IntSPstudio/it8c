#!/usr/bin/env python3
#|==============================================================|#
# Made by IntSPstudio
# Useful scripts to IT8c library
# Thank you for using this software!
# ID: 980001003
#
# Twitter: @IntSPstudio
#|==============================================================|#

#IMPORT 
import it8c
import os
#OPERATING SYSTEM SETTINGS
# 1 = WINDOWS
# 2 = LINUX
uiusOS =1
#BACKGROUND
bgdLine =  it8c.vslTerminalLine(0,"")
#DICTIONARY
dcnyStLineAA ="]"
dcnyStLineAB ="==" + dcnyStLineAA
dcnyStLineEA = dcnyStLineAB +" Select the number: "
dcnyStLineEI = dcnyStLineAB +" Press enter to return"
#SETTINGS
libraryVersion = it8c.version()
mainTitle = "IT8c V:"+ libraryVersion +":"
mainPage =""
continuity =1
uiusBckFeatures ="1"
uiusBckAbout ="2"
exitPage ="3"
if uiusOS == 1:
	mainClearCommand ="cls"
elif uiusOS == 2:
	mainClearCommand ="clear"
#MAIN LOOP
if __name__ == "__main__":
	while continuity == 1:
		#FEATURES
		if mainPage == uiusBckFeatures:
			#TA
			os.system(mainClearCommand)
			#TB
			print(bgdLine)
			print(dcnyStLineAB, mainTitle, "Features")
			print(it8c.haiFeatures())
			#TC
			mainInput =input(dcnyStLineEI)
			mainPage =0
		#ABOUT
		elif mainPage == uiusBckAbout:
			#TA
			os.system(mainClearCommand)
			#TB
			print(bgdLine)
			print(dcnyStLineAB, mainTitle, "About")
			#TC
			mainInput =input(dcnyStLineEI)
			mainPage =0
		#EXIT
		elif mainPage == exitPage:
			#TA
			continuity =0
		#MENU
		else:
			#TA
			os.system(mainClearCommand)
			#TB
			print(bgdLine)
			print(dcnyStLineAB, mainTitle)
			print(" 1"+ dcnyStLineAA, "Features")
			print(" 2"+ dcnyStLineAA, "About")
			print(" 3"+ dcnyStLineAA, "Exit")
			#TC
			mainInput =input(dcnyStLineEA)
			mainPage = str(mainInput)
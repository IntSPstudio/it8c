#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this library!
# Plugin: Visual
#|==============================================================|#

#TERMINAL IT8C LOGO
def cfc315323(start_point):
	start_mark =""
	if start_point > 0:
		for _ in range(start_point):
			start_mark = start_mark +" "
	a = start_mark +"#############################"
	b = start_mark +"##################    ##"
	c = start_mark +"##      ##      ##    ##"
	d = start_mark +"##      ##      ########"
	e = start_mark +"##      ##      ########"
	f = start_mark +"##      ##      ##    ##"
	g = start_mark +"##      ##      ##    ##"
	h = start_mark +"##      ##      #############"
	return "\n"+ a +"\n"+ b +"\n"+ c +"\n"+ d +"\n"+ e +"\n"+ f +"\n"+ g +"\n"+ h +"\n"
#WHAT
def cfc315313(start_point):
	start_mark =""
	if start_point > 0:
		for _ in range(start_point):
			start_mark = start_mark +" "
	a = start_mark +"######            "
	b = start_mark +"#    #            "
	c = start_mark +"#    #      ######"
	d = start_mark +"#    #      #    #"
	e = start_mark +"#    #  ##  #    #"
	f = start_mark +"######  ##  ######"
	return "\n"+ a +"\n"+ b +"\n"+ c +"\n"+ d +"\n"+ e +"\n"+ f +"\n" 
#TERMINAL LINE
def cfc35650(width,mark):
	if width > 0:
		line =""
		for _ in range(width):
			line = line + mark
	else:
		line = "----------------------------------------------------------------"
	return line
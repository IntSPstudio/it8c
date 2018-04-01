#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this library!
# Plugin: Visual
#|==============================================================|#

#TERMINAL IT8C LOGO
def cfc315323(stpoint):
	stmark =""
	if stpoint > 0:
		for _ in range(stpoint):
			stmark = stmark +" "
	a = stmark +"#############################"
	b = stmark +"##################    ##"
	c = stmark +"##      ##      ##    ##"
	d = stmark +"##      ##      ########"
	e = stmark +"##      ##      ########"
	f = stmark +"##      ##      ##    ##"
	g = stmark +"##      ##      ##    ##"
	h = stmark +"##      ##      #############"
	return "\n"+ a +"\n"+ b +"\n"+ c +"\n"+ d +"\n"+ e +"\n"+ f +"\n"+ g +"\n"+ h +"\n"
#WHAT
def cfc315313(stpoint):
	stmark =""
	if stpoint > 0:
		for _ in range(stpoint):
			stmark = stmark +" "
	a = stmark +"######            "
	b = stmark +"#    #            "
	c = stmark +"#    #      ######"
	d = stmark +"#    #      #    #"
	e = stmark +"#    #  ##  #    #"
	f = stmark +"######  ##  ######"
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